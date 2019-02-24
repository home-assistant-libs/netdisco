"""Discover digitalSTROM server IP (dss-ip)  devices."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering digitalSTROM server IP (dss-ip) devices."""

    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_http._tcp.local.')

    def get_entries(self):
        return self.find_by_device_name('dss-ip')
