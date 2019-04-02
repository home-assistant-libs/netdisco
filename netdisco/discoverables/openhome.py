"""Discover Openhome devices."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Openhome compliant devices."""

    def get_entries(self):
        """Get all the Openhome compliant device uPnP entries."""
        return self.find_by_st("urn:av-openhome-org:service:Product:1") + \
            self.find_by_st("urn:av-openhome-org:service:Product:2") + \
            self.find_by_st("urn:av-openhome-org:service:Product:3")
