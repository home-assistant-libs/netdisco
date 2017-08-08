"""Discover tplink devices."""
from . import BaseDiscoverable


class Discoverable(BaseDiscoverable):
    """Add support for discovering a tplink device."""

    def __init__(self, netdis):
        """Initialize the tplink discovery."""
        self._netdis = netdis

    def get_entries(self):
        """Get all the tplink details."""
        return self._netdis.tplink_light.entries
