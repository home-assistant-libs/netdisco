"""Discover Denon AVR devices."""
from urllib.parse import urlparse

from . import SSDPDiscoverable


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
        name = entry.description['device']['friendlyName']
        model = entry.description['device']['modelName']
        host = urlparse(
            entry.description['device']['presentationURL']).hostname

        return (host, name, model)
