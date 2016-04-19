"""Discover Kodi servers."""
from . import MDNSDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Adds support for discovering Kodi."""

    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_http._tcp.local.')

    def info_from_entry(self, entry):
        """Returns most important info from mDNS entries."""
        return (self.ip_from_host(entry.server), entry.port)

    def get_info(self):
        return [self.info_from_entry(entry) for entry in self.get_entries()
                if entry.name.startswith('Kodi ')]
