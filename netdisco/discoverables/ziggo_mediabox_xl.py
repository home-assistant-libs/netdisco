"""Discover Ziggo Mediabox XL devices."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Ziggo Mediabox XL devices."""

    def get_entries(self):
        """Return all Ziggo (UPC) Mediabox XL entries."""
        return self.find_by_device_description(
            {'modelDescription': 'UPC Hzn Gateway',
             'deviceType': 'urn:schemas-upnp-org:device:RemoteUIServer:2'})
