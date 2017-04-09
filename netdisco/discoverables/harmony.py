"""Discover Netgear routers."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Harmony Hub remotes"""

    def get_entries(self):
        """Get all the Harmony uPnP entries."""
        return self.find_by_device_description({
            "manufacturer": "Logitech",
            "deviceType": "urn:myharmony-com:device:harmony:1"
        })
