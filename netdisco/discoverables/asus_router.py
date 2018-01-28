"""Discover ASUS routers."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering ASUS routers."""

    def get_entries(self):
        """Get all the ASUS uPnP entries."""
        return self.find_by_device_description({
            "manufacturer": "ASUSTeK Computer Inc.",
            "deviceType": "urn:schemas-upnp-org:device:InternetGatewayDevice:1"
        })
