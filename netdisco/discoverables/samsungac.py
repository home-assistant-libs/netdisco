"""Discover Samsung Smart AC devices."""
from . import BaseDiscoverable


class Discoverable(BaseDiscoverable):
    """Add support for discovering a Samsung Smart AC device."""

    def __init__(self, netdis):
        """Initialize the Samsung Smart AC discovery."""
        self._netdis = netdis

    def get_entries(self):
        """Get all the Samsung Smart AC details."""
        return []
        # return self._netdis.samsungac.entries
