"""Discover Xbox One SmartGlass devices."""
from . import BaseDiscoverable


class Discoverable(BaseDiscoverable):
    """Add support for discovering a Xbox One SmartGlass device."""

    def __init__(self, netdis):
        """Initialize the Xbox One SmartGlass discovery."""
        self._netdis = netdis

    def get_entries(self):
        """Get all the Xbox One SmartGlass details."""
        return self._netdis.xboxone.entries
