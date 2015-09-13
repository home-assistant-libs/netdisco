""" Discovers Netgear routers. """

from . import SSDPDiscoverable

try:
    from urlparse import urlparse  # Py2
except ImportError:
    from urllib.parse import urlparse  # Py3


class Discoverable(SSDPDiscoverable):
    """ Adds support for discovering Philips Hue bridges. """

    def info_from_entry(self, entry):
        """ Returns the most important info from a uPnP entry. """
        url = urlparse(entry.values['location'])

        return (entry.description['device']['modelNumber'], url.hostname)

    def get_entries(self):
        """ Get all the Hue bridge uPnP entries. """
        return self.find_by_device_description({
            "manufacturer": "NETGEAR, Inc.",
            "deviceType": "urn:schemas-upnp-org:device:InternetGatewayDevice:1"
        })
