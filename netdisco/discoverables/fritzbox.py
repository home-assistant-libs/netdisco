"""Discover AVM FRITZ devices."""
from . import SSDPDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(SSDPDiscoverable):
    """Add support for discovering AVM FRITZ devices."""

    def get_entries(self):
        """Get all AVM FRITZ entries."""
        return self.find_by_st("urn:schemas-upnp-org:device:fritzbox:1")
