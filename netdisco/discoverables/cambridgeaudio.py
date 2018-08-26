""" Discover Cambridge Audio StreamMagic devices. """
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Cambridge Audio StreamMagic devices."""

    def get_entries(self):
        """Get all Cambridge Audio MediaRenderer uPnP entries."""
        return self.find_by_device_description({
            "manufacturer": "Cambridge Audio",
            "deviceType": "urn:schemas-upnp-org:device:MediaRenderer:1"
        })
