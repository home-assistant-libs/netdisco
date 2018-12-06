"""Discover Twinkly devices."""
from . import BaseDiscoverable


class Discoverable(BaseDiscoverable):
    """Add support for discovering a Twinkly device."""

    def __init__(self, netdis):
        """Initialize the Twinkly discovery."""
        self._netdis = netdis

    def get_entries(self):
        """Get all the twinkly details."""
        return self._netdis.xled.entries
