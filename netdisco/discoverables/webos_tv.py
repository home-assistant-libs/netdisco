"""Discover LG WebOS TV devices."""
from netdisco.util import urlparse
from . import SSDPDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(SSDPDiscoverable):
    """Add support for discovering LG WebOS TV devices."""

    def info_from_entry(self, entry):
        """Get most important info, which is name, model and host."""
        name = entry.description['device']['friendlyName']
        model = entry.description['device']['modelName']
        host = urlparse(entry.values['location']).hostname

        return name, model, host

    def get_entries(self):
        """Get all the LG WebOS TV device uPnP entries."""
        return self.find_by_device_description(
            {
                "deviceType": "urn:schemas-upnp-org:device:Basic:1",
                "modelName": "LG Smart TV"
            }
        )
