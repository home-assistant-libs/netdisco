"""Discover OctoPrint Servers."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering OctoPrint servers."""

    def get_entries(self):
        """Get all the OctoPrint uPnP entries."""
        return self.find_by_device_description({
            "manufacturer": "The OctoPrint Project"
        })
