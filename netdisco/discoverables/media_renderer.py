"""Discover UPNP media renderer."""
from . import SSDPDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(SSDPDiscoverable):
    """Add support for discovering UPNP media renderer."""

    def get_entries(self):
        """Get all the DLNA service uPnP entries."""
        return self.find_by_st("urn:schemas-upnp-org:device:MediaRenderer:1")
