"""
Combines all the different protocols into a simple interface.
"""
from __future__ import print_function
import logging
import os
import importlib

from .ssdp import SSDP
from .mdns import MDNS

_LOGGER = logging.getLogger(__name__)


class NetworkDiscovery(object):
    """
    Scans the network for devices.

    mDNS scans in a background thread.
    SSDP scans in the foreground.

    start: is ready to scan
    scan: scan the network
    discover: parse scanned data
    get_in

    """

    def __init__(self, limit_discovery=None):
        self.limit_discovery = limit_discovery

        self.mdns = MDNS()
        self.ssdp = SSDP()
        self.discoverables = {}

        self._load_device_support()

        self.is_discovering = False

    def scan(self):
        """ Starts and tells scanners to scan. """
        if not self.is_discovering:
            self.mdns.start()
            self.is_discovering = True

        self.ssdp.scan()

    def stop(self):
        """ Turn discovery off. """
        if not self.is_discovering:
            return

        self.mdns.stop()

        self.is_discovering = False

    def discover(self):
        """ Return a list of discovered devices and services. """
        self._check_enabled()

        return [dis for dis, checker in self.discoverables.items()
                if checker.is_discovered()]

    def get_info(self, dis):
        """
        Get a list with the most important info about discovered service or
        device type.
        """
        return self.discoverables[dis].get_info()

    def get_entries(self, dis):
        """
        Get a list with all info about a discovered service or device type.
        """
        return self.discoverables[dis].get_entries()

    def _check_enabled(self):
        """ Raises RuntimeError if discovery is disabled. """
        if not self.is_discovering:
            raise RuntimeError("NetworkDiscovery is disabled")

    def _load_device_support(self):
        """ Load the devices and services that can be discovered. """
        self.discoverables = {}

        discoverables_format = __name__.rsplit('.', 1)[0] + '.discoverables.{}'

        for module_name in os.listdir(os.path.join(os.path.dirname(__file__),
                                                   'discoverables')):
            if module_name[-3:] != '.py' or module_name == '__init__.py':
                continue

            module_name = module_name[:-3]

            if self.limit_discovery is not None and \
               module_name not in self.limit_discovery:
                continue

            module = importlib.import_module(
                discoverables_format.format(module_name))

            self.discoverables[module_name] = module.Discoverable(self)

    def print_raw_data(self):
        """ Helper method to show what is discovered in your network. """
        from pprint import pprint

        print("Zeroconf")
        pprint(self.mdns.entries)
        print("")
        print("SSDP")
        pprint(self.ssdp.entries)
