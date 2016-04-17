"""Discover SabNZBD servers."""
from . import MDNSDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Adds support for discovering sabnzbd """

    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_http._tcp.local.')

    def info_from_entry(self, entry):
        """Returns most important info from mDNS entries."""
        return (self.ip_from_host(entry.server), entry.port,
                entry.properties.get('path', '/sabnzbd/'))

    def get_info(self):
        """We just want SABnzbd, filter everything else """
        return [self.info_from_entry(entry) for entry in self.get_entries()
                if entry.name.startswith('SABnzbd on')]
