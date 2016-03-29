""" Discovers Panasonic Viera TV devices. """

from . import SSDPDiscoverable

try:
    from urlparse import urlparse  # Py2
except ImportError:
    from urllib.parse import urlparse  # Py3


# pylint: disable=too-few-public-methods
class Discoverable(SSDPDiscoverable):
    """ Adds support for discovering Viera TV devices. """

    def info_from_entry(self, entry):
        """ Returns the most important info from a uPnP entry. """
        return '{}:{}'.format(urlparse(entry.values['location']).hostname,
                         urlparse(entry.values['location']).port)

    def get_entries(self):
        """ Get all the Viera TV device uPnP entries. """
        return self.find_by_st("urn:panasonic-com:service:p00NetworkControl:1")
