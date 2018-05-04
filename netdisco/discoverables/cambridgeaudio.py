""" Discover Cambridge Audio StreamMagic devices. """
from . import SSDPDiscoverable
from ..const import ATTR_NAME, ATTR_MODEL_NAME


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Cambridge Audio StreamMagic devices."""

    def get_entries(self):
        """Get all Denon AVR uPnP entries."""
        return self.find_by_device_description({
            "manufacturer": "Cambridge Audio",
            "deviceType": "urn:schemas-upnp-org:device:MediaRenderer:1"
        })

    def info_from_entry(self, entry):
        """Get most important info, which is name, model and host."""
        info = super().info_from_entry(entry)
        info[ATTR_NAME] = entry.description['device']['friendlyName']
        info[ATTR_MODEL_NAME] = entry.description['device']['modelName']
        return info
