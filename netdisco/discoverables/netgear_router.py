"""Discover Netgear routers."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Netgear routers."""

    def get_entries(self):
        """Get all the Netgear uPnP entries."""
        return self.find_by_device_description({
            "manufacturer": "NETGEAR, Inc.",
            "deviceType": "urn:schemas-upnp-org:device:InternetGatewayDevice:1"
        })
