"""Discover Heos devices."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering DLNA services."""

    def get_entries(self):
        """Get all the HEOS devices."""
        return self.find_by_st("urn:schemas-denon-com:device:ACT-Denon:1")
