"""Discover LG WebOS TV devices."""
from netdisco.util import urlparse
from . import SSDPDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(SSDPDiscoverable):
    """Add support for discovering LG WebOS TV devices."""

    def info_from_entry(self, entry):
        """Return the most important info from a uPnP entry."""
        return urlparse(entry.values['location']).hostname

    def get_entries(self):
        """Get all the LG WebOS TV device uPnP entries."""

        # Lookup for webos3
        webos_entry = self.find_by_device_description(
            {
                "deviceType": "urn:schemas-upnp-org:device:MediaRenderer:1",
                "manufacturer": "LG Electronics.",
                "modelName": "LG TV"
            }
        )

        if not len(webos_entry):
            # If not found look for older versions as before
            webos_entry = self.find_by_device_description({
                "deviceType": "urn:dial-multiscreen-org:device:dial:1",
                "friendlyName": "[LG] webOS TV"
            })

        return webos_entry
