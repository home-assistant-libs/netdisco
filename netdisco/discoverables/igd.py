"""Discover IGD services."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering IGD services."""

    def get_entries(self):
        """Get all the IGD service uPnP entries."""
        return \
            self.find_by_st(
                "urn:schemas-upnp-org:device:InternetGatewayDevice:1") + \
            self.find_by_st(
                "urn:schemas-upnp-org:device:InternetGatewayDevice:2")
