"""Discover Sonos devices."""
from . import SSDPDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(SSDPDiscoverable):
    """Add support for discovering Sonos devices."""

    def get_entries(self):
        """Get all the Sonos device uPnP entries."""
        return self.find_by_st("urn:schemas-upnp-org:device:ZonePlayer:1")
