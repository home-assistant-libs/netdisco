"""Discover Brother printers"""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Support for discovery Brother printers"""

    def __init__(self, nd):
        """Initialize Brother printers discovery"""
        super(Discoverable, self).__init__(nd, '_printer._tcp.local.')

    def get_entries(self):
        return self.find_by_device_name('Brother')
