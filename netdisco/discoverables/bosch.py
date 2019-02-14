"""Discover Bosch gateways."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering Bosch gateways"""

    def __init__(self, nd):
        """Initialize the Bosch gateways discovery."""
        super(Discoverable, self).__init__(nd, '_http._tcp.local.')

    def get_entries(self):
        return self.find_by_device_name('iCom ')
