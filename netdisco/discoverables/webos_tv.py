"""Discover LG WebOS TV devices."""
from . import SSDPDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(SSDPDiscoverable):
    """Add support for discovering LG WebOS TV devices."""

    def get_entries(self):
        """Get all the LG WebOS TV device uPnP entries."""
        return self.find_by_device_description(
            {
                "deviceType": "urn:schemas-upnp-org:device:Basic:1",
                "modelName": "LG Smart TV"
            }
        )
