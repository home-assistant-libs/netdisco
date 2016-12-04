"""Discover SABnzbd servers."""
from . import MDNSDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for discovering SABnzbd."""

    def __init__(self, nd):
        """Initialize the SABnzbd discovery."""
        super(Discoverable, self).__init__(nd, '_http._tcp.local.')

    def info_from_entry(self, entry):
        """Return most important info from mDNS entries."""
        return (self.ip_from_host(entry.server), entry.port,
                entry.properties.get('path', '/sabnzbd/'))

    def get_entries(self):
        return self.find_by_device_name('SABnzbd on')
