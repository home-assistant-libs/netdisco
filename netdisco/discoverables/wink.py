"""Discover Wink hub devices."""
from typing import List  # noqa: F401

from . import SSDPDiscoverable
from ..ssdp import UPNPEntry  # noqa: F401


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Wink hub devices."""

    def get_entries(self):
        """Return all Wink entries."""
        results = []  # type: List[UPNPEntry]
        results.extend(self.find_by_st('urn:wink-com:device:hub2:2'))
        results.extend(self.find_by_st('urn:wink-com:device:hub:2'))
        results.extend(self.find_by_st('urn:wink-com:device:relay:2'))
        return results
