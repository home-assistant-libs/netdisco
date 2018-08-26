"""Discover Canon Printers"""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Support for the discovery of Canon Printers"""

    def get_entries(self):
        """Get all the Canon Printer uPnP entries."""
        return self.find_by_device_description({
            "manufacturer": "CANON INC.",
            "deviceType": "urn:schemas-cipa-jp:device:DPSPrinter:1"
        })
