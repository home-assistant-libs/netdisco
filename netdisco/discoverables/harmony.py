"""Discover Netgear routers."""
from netdisco.util import urlparse
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Harmony Hub remotes"""

    def info_from_entry(self, entry):
        """Return the most important info from a uPnP entry."""
        url = urlparse(entry.values['location'])
        return (entry.description['device']['friendlyName'], url.hostname)

    def get_entries(self):
        """Get all the Harmony uPnP entries."""
        return self.find_by_device_description({
            "manufacturer": "Logitech",
            "deviceType": "urn:myharmony-com:device:harmony:1"
        })
