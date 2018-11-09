"""Discover Buderus KM200 gateways."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering Buderus KM200."""

    def __init__(self, nd):
        """Initialize the Buderus KM200 discovery."""
        super(Discoverable, self).__init__(nd, '_http._tcp.local.')

    def get_entries(self):
        return self.find_by_device_name('iCom ')