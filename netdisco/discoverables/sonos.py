""" Discovers Sonos devices. """

from . import SSDPDiscoverable

try:
    from urlparse import urlparse  # Py2
except ImportError:
    from urllib.parse import urlparse  # Py3


# pylint: disable=too-few-public-methods
class Discoverable(SSDPDiscoverable):
    """ Adds support for discovering Sonos devices. """

    def info_from_entry(self, entry):
        """ Returns the most important info from a uPnP entry. """
        return urlparse(entry.values['location']).hostname

    def get_entries(self):
        """ Get all the Sonos device uPnP entries. """
        return self.find_by_st("urn:schemas-upnp-org:device:ZonePlayer:1")
