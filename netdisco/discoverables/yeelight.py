"""Discover Yeelight devices."""
from . import SSDPDiscoverable
from ..const import ATTR_DEVICE_TYPE, ATTR_SERIAL

ATTR_FIRMWARE_VERSION = 'firmware_version'
ATTR_SUPPORT = 'support'


# pylint: disable=too-few-public-methods
class Discoverable(SSDPDiscoverable):
    """Add support for discovering Yeelight."""

    def info_from_entry(self, entry):
        """Return most important info from SSDP entries."""
        info = super().info_from_entry(entry)

        # The model doesn't align with the mDNS model names (color vs. color1)
        info[ATTR_DEVICE_TYPE] = entry.model
        info[ATTR_SERIAL] = entry.id
        info[ATTR_FIRMWARE_VERSION] = entry.fw_ver
        info[ATTR_SUPPORT] = entry.support

        return info

    def get_entries(self):
        """Get all the Yeelight compliant device SSDP entries."""
        return self.find_by_location("yeelight://")
