"""Discover Samsung Printers"""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Support for the discovery of Samsung Printers"""

    def get_entries(self):
        """Get all the Samsung Printer uPnP entries."""
        return self.find_by_device_description({
            "manufacturer": "Samsung Electronics",
            "deviceType": "urn:schemas-upnp-org:device:Printer:1"
        })
