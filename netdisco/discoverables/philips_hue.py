"""Discover Philips Hue bridges."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Philips Hue bridges."""

    def get_entries(self):
        """Get all the Hue bridge uPnP entries."""
        return self.find_by_device_description({
            "manufacturer": "Royal Philips Electronics",
            "modelNumber": ["929000226503", "BSB002"]
        })
