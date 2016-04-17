"""Discovers Tellstick devices."""

from . import BaseDiscoverable


class Discoverable(BaseDiscoverable):
    """Adds support for discovering a Tellstick device."""

    def __init__(self, netdis):
        self._netdis = netdis

    def get_entries(self):
        return self._netdis.tellstick.entries
