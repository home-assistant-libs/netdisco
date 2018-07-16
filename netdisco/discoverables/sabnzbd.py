"""Discover SABnzbd servers."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering SABnzbd."""

    def __init__(self, nd):
        """Initialize the SABnzbd discovery."""
        super(Discoverable, self).__init__(nd, '_http._tcp.local.')

    def get_entries(self):
        return self.find_by_device_name('SABnzbd on')
