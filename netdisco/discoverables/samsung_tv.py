"""Discover Samsung Smart TV services."""
from urllib.parse import urlparse

from . import SSDPDiscoverable

# For some models, Samsung forces a [TV] prefix to the user-specified name.
FORCED_NAME_PREFIX = '[TV]'


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Samsung Smart TV services."""

    def get_entries(self):
        """Get all the Samsung RemoteControlReceiver entries."""
        return self.find_by_device_description({
            "deviceType": "urn:samsung.com:device:RemoteControlReceiver:1"
        })

    def info_from_entry(self, entry):
        """Get most important info, by default the description location."""

        name = entry.description['device']['friendlyName']
        # Strip the forced prefix, if present
        if name.startswith(FORCED_NAME_PREFIX):
            name = name[len(FORCED_NAME_PREFIX):]

        model = entry.description['device']['modelName']

        # Extract the IP address from the location; it is not given in the XML.
        host = urlparse(entry.values['location']).hostname

        return name, model, host
