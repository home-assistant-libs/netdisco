"""Discover Wink hub devices."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Wink hub devices."""

    def get_entries(self):
        """Return all Wink entries."""
        results = []
        results.extend(self.find_by_st('urn:wink-com:device:hub2:2'))
        results.extend(self.find_by_st('urn:wink-com:device:hub:2'))
        results.extend(self.find_by_st('urn:wink-com:device:relay:2'))
        return results
