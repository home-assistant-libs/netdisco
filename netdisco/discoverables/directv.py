"""Discover DirecTV Receivers."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering DirecTV Receivers."""

    def get_entries(self):
        """Get all the DirecTV uPnP entries."""
        return self.find_by_device_description({
            "manufacturer": "DIRECTV",
            "deviceType": "urn:schemas-upnp-org:device:MediaServer:1"
        })
