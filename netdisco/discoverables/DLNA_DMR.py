"""Discover DLNA services."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering DLNA services."""

    def get_entries(self):
        """Get all the DLNA service uPnP entries."""
        return \
            self.find_by_st("urn:schemas-upnp-org:device:MediaRenderer:1") + \
            self.find_by_st("urn:schemas-upnp-org:device:MediaRenderer:2") + \
            self.find_by_st("urn:schemas-upnp-org:device:MediaRenderer:3")
