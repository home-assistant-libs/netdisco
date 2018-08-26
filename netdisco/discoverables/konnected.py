"""Discover Konnected Security devices."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Konnected Security devices."""

    def get_entries(self):
        """Return all Konnected entries."""
        return self.find_by_st('urn:schemas-konnected-io:device:Security:1')
