"""Discovers Logitech Media Server."""

from . import BaseDiscoverable


class Discoverable(BaseDiscoverable):
    """Adds support for discovering Logitech Media Server."""

    def __init__(self, netdis):
        self.netdis = netdis

    def get_entries(self):
        return [entry['from'] for entry in self.netdis.lms.entries]
