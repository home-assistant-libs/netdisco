"""Discover Fluxled devices."""
from . import BaseDiscoverable


class Discoverable(BaseDiscoverable):
    """Add support for discovering a Fluxled device."""

    def __init__(self, netdis):
        """Initialize the Fluxled discovery."""
        self._netdis = netdis

    def get_entries(self):
        """Get all the Fluxled details."""
        return self._netdis.fluxled.entries
