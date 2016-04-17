""" Discovers LG WebOS TV devices. """

from . import SSDPDiscoverable

try:
    from urlparse import urlparse  # Py2
except ImportError:
    from urllib.parse import urlparse  # Py3


# pylint: disable=too-few-public-methods
class Discoverable(SSDPDiscoverable):
    """ Adds support for discovering LG WebOS TV devices. """

    def info_from_entry(self, entry):
        """ Returns the most important info from a uPnP entry. """
        return urlparse(entry.values['location']).hostname

    def get_entries(self):
        """ Get all the LG WebOS TV device uPnP entries. """
        return self.find_by_device_description({
            "deviceType": "urn:dial-multiscreen-org:device:dial:1",
            "friendlyName": "[LG] webOS TV"
        })
