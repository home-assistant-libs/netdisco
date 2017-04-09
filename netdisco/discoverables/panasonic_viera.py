"""Discover Panasonic Viera TV devices."""
from . import SSDPDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(SSDPDiscoverable):
    """Add support for discovering Viera TV devices."""

    def get_entries(self):
        """Get all the Viera TV device uPnP entries."""
        return self.find_by_st("urn:panasonic-com:service:p00NetworkControl:1")
