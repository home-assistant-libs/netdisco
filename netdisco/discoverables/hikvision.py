"""Discover Hikvision cameras."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering Hikvision cameras."""

    def __init__(self, nd):
        """Initialize Hikvision camera discovery."""
        super(Discoverable, self).__init__(nd, '_http._tcp.local.')

    def get_entries(self):
        return self.find_by_device_name('HIKVISION')
