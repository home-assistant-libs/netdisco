"""Discover deCONZ gateways."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering deCONZ Wireless Light Control gateways."""

    def get_entries(self):
        """Get all the deCONZ uPnP entries."""
        return self.find_by_device_description({
            "manufacturerURL": "http://www.dresden-elektronik.de",
            "modelDescription": "dresden elektronik Wireless Light Control"
        })
