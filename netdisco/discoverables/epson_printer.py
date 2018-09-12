"""Discover Epson Printers"""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Support for the discovery of Epson printers"""

    def __init__(self, nd):
        """Initialize the Epson printer discovery"""
        super(Discoverable, self).__init__(nd, '_printer._tcp.local.')

    def get_entries(self):
        return self.find_by_device_name('EPSON ')
