"""Discover Yeelight bulbs, based on Kodi discoverable."""
import logging
from . import MDNSDiscoverable
from ..const import ATTR_DEVICE_TYPE


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for discovering Yeelight."""

    def __init__(self, nd):
        """Initialize the Yeelight discovery."""
        super(Discoverable, self).__init__(nd, '_miio._udp.local.')

    def info_from_entry(self, entry):
        """Return most important info from mDNS entries."""
        info = super().info_from_entry(entry)

        device_type = "UNKNOWN"
        if entry.name.startswith("yeelink-light-color1_"):
            device_type = "rgb"
        elif entry.name.startswith("yeelink-light-mono1_"):
            device_type = "white"
        elif entry.name.startswith("yeelink-light-strip1_"):
            device_type = "strip"
        else:
            logging.warning("Unknown miio device found: %s", entry)

        info[ATTR_DEVICE_TYPE] = device_type
        return info

    def get_entries(self):
        """ Return yeelight devices. """
        return self.find_by_device_name('yeelink-light-')
