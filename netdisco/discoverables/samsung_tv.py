"""Discover Samsung Smart TV services."""
from urllib.parse import urlparse

from . import SSDPDiscoverable

class Discoverable(SSDPDiscoverable):
    """Add support for discovering Samsung Smart TV services."""

    def get_entries(self):
        """Get all the Samsung RemoteControlReceiver entries."""
        return self.find_by_device_description({
            "deviceType": "urn:samsung.com:device:RemoteControlReceiver:1"
        })

    def info_from_entry(self, entry):
        """Get most important info, by default the description location."""
        host = urlparse(entry.values['location']).hostname
        name = entry.description['device']['friendlyName']
        model = entry.description['device']['modelName']
        return name, model, host
