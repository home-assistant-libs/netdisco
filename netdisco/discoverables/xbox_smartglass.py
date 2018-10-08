"""Discover Xbox SmartGlass devices."""
from . import BaseDiscoverable


class Discoverable(BaseDiscoverable):
    """Add support for discovering a Xbox SmartGlass device."""

    def __init__(self, netdis):
        """Initialize the Xbox SmartGlass discovery."""
        self._netdis = netdis

    def get_entries(self):
        """Get all the Xbox SmartGlass details."""
        return self._netdis.xbox_smartglass.entries
