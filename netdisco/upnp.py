"""
Module that implements UPNP protocol
"""
import re
import select
import socket
import logging
from datetime import datetime, timedelta
import threading

import requests
import xmltodict

from netdisco.discoverables import BaseDiscoverable

SSDP_ADDR = "239.255.255.250"
SSDP_PORT = 1900
SSDP_MX = 5

SSDP_REQUEST = 'M-SEARCH * HTTP/1.1\r\n' + \
               'HOST: {}:{:d}\r\n'.format(SSDP_ADDR, SSDP_PORT) + \
               'MAN: "ssdp:discover"\r\n' + \
               'MX: {:d}\r\n'.format(SSDP_MX) + \
               'ST: ssdp:all\r\n' + \
               '\r\n'

RESPONSE_REGEX = re.compile(r'\n(.*)\: (.*)\r')

MIN_TIME_BETWEEN_SCANS = timedelta(seconds=59)

DISCOVER_TIMEOUT = SSDP_MX


def _setup_entry_description_cache():
    """ Resets the entry description cache. """
    UPNPEntry.DESCRIPTION_CACHE = {'_NO_LOCATION': {}}


class UPNP(object):
    """ Controls the scanning of uPnP devices and services. """

    def __init__(self):
        self.entries = []
        self.last_scan = None
        self._lock = threading.RLock()

    # pylint: disable=no-self-use
    def stop(self):
        """ Clears the description cache. """
        _setup_entry_description_cache()

    def all(self):
        """ Returns all found entries. """
        with self._lock:
            self.update()

            return list(self.entries)

    # pylint: disable=invalid-name
    def find_by_st(self, st):
        """ Return a list of entries that match the ST. """
        with self._lock:
            self.update()

            return [entry for entry in self.entries
                    if entry.values.get('st') == st]

    def find_by_device_description(self, values):
        """
        Return a list of entries that match the description.
        Pass in a dict with values to match against the device tag in the
        description.
        """
        with self._lock:
            self.update()

            return [entry for entry in self.entries
                    if entry.match_device_description(values)]

    def update(self, force_update=False):
        """ Scans for new uPnP devices and services. """
        with self._lock:
            if self.last_scan is None or force_update or \
               datetime.now()-self.last_scan > MIN_TIME_BETWEEN_SCANS:

                self.remove_expired()

                self.entries.extend(entry for entry in scan()
                                    if entry not in self.entries)

                self.last_scan = datetime.now()

    def remove_expired(self):
        """ Filter out expired entries. """
        with self._lock:
            self.entries = [entry for entry in self.entries
                            if not entry.is_expired]


class UPNPEntry(object):
    """ Found uPnP entry. """

    def __init__(self, values):
        self.values = values
        self.created = datetime.now()

        if 'cache-control' in self.values:
            cache_seconds = int(self.values['cache-control'].split('=')[1])

            self.expires = self.created + timedelta(seconds=cache_seconds)
        else:
            self.expires = None

    @property
    def is_expired(self):
        """ Returns if the entry is expired or not. """
        return self.expires is not None and datetime.now() > self.expires

    @property
    def description(self):
        """ Returns the description from the uPnP entry. """
        url = self.values.get('location', '_NO_LOCATION')

        if url not in UPNPEntry.DESCRIPTION_CACHE:
            UPNPEntry.DESCRIPTION_CACHE[url] = xmltodict.parse(
                requests.get(url).text)['root']

        return UPNPEntry.DESCRIPTION_CACHE[url]

    def match_device_description(self, values):
        """
        Fetches description and matches against it.
        values should only contain lowercase keys.
        """
        device = self.description.get('device')

        if device is None:
            return False

        return all(val == device.get(key)
                   for key, val in values.items())

    @classmethod
    def from_response(cls, response):
        """ Creates a uPnP entry from a response. """
        return UPNPEntry({key.lower(): item for key, item
                          in RESPONSE_REGEX.findall(response)})

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and
                self.values == other.values)

    def __repr__(self):
        return "<UPNPEntry {} - {}>".format(
            self.values.get('st', ''), self.values.get('location', ''))


_setup_entry_description_cache()


def scan(timeout=DISCOVER_TIMEOUT, max_entries=None):
    """
    Sends a message over the network to discover upnp devices.

    Inspired by Crimsdings
    https://github.com/crimsdings/ChromeCast/blob/master/cc_discovery.py
    """
    entries = []

    calc_now = datetime.now
    start = calc_now()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.sendto(SSDP_REQUEST.encode("ascii"), (SSDP_ADDR, SSDP_PORT))

        sock.setblocking(0)

        while True:
            time_diff = calc_now() - start

            # pylint: disable=maybe-no-member
            seconds_left = timeout - time_diff.seconds

            if seconds_left <= 0:
                return entries

            ready = select.select([sock], [], [], seconds_left)[0]

            if ready:
                response = sock.recv(1024).decode("ascii")

                entry = UPNPEntry.from_response(response)

                if entry not in entries:
                    entries.append(entry)

                    if max_entries and len(entries) == max_entries:
                        return entries

    except socket.error:
        logging.getLogger(__name__).exception(
            "Socket error while discovering Chromecasts")

    finally:
        sock.close()

    return entries


class UPNPDiscoverable(BaseDiscoverable):
    """ uPnP discoverable base class. """

    def __init__(self, netdis):
        self.netdis = netdis

    def get_info(self):
        """ Gets most important info, by default the description location. """
        return list(set(
            (entry.values['location'])
            for entry in self.get_entries()))

    # Helper functions

    # pylint: disable=invalid-name
    def find_by_st(self, st):
        """ Find entries by ST (the device identifier). """
        return self.netdis.upnp.find_by_st(st)

    def find_by_device_description(self, values):
        """ Find entries based on values from their description. """
        return self.netdis.upnp.find_by_device_description(values)


if __name__ == "__main__":
    from pprint import pprint

    pprint("Scanning UPNP..")
    pprint(scan())
