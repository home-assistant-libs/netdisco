"""Discover Roku players."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Roku media players."""

    def get_entries(self):
        """Get all the Roku entries."""
        return self.find_by_st("roku:ecp")
