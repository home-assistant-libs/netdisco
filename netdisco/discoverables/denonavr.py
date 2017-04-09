"""Discover Denon AVR devices."""
from urllib.parse import urlparse

from . import SSDPDiscoverable
from ..const import ATTR_HOST


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Denon AVR devices."""

    def get_entries(self):
        """Get all Denon AVR uPnP entries."""
        return self.find_by_device_description({
            "manufacturer": "Denon",
            "deviceType": "urn:schemas-upnp-org:device:MediaRenderer:1"
        })

    def info_from_entry(self, entry):
        """Get most important info, which is name, model and host."""
        info = super().info_from_entry(entry)
        info[ATTR_HOST] = urlparse(
            entry.description['device']['presentationURL']).hostname
        return info
