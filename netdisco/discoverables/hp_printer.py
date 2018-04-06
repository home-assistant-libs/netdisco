"""Discover HP Printers"""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Support for the discovery of HP Printers"""

    def __init__(self, nd):
        """Initialize the HP Printer discovery"""
        super(Discoverable, self).__init__(nd, '_printer._tcp.local.')

    def get_entries(self):
        return self.find_by_device_name('HP ')
