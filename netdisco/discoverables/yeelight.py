"""Discover Yeelight bulbs, based on Kodi discoverable."""
from . import MDNSDiscoverable
from ..const import ATTR_DEVICE_TYPE

DEVICE_NAME_PREFIX = 'yeelink-light-'


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for discovering Yeelight."""

    def __init__(self, nd):
        """Initialize the Yeelight discovery."""
        super(Discoverable, self).__init__(nd, '_miio._udp.local.')

    def info_from_entry(self, entry):
        """Return most important info from mDNS entries."""
        info = super().info_from_entry(entry)

        # Example name: yeelink-light-ceiling4_mibt72799069._miio._udp.local.
        if entry.name.startswith("yeelink-light-color1_"):
            device_type = "rgb"
        elif entry.name.startswith("yeelink-light-mono1_"):
            device_type = "white"
        elif entry.name.startswith("yeelink-light-strip1_"):
            device_type = "strip"
        elif entry.name.startswith("yeelink-light-bslamp1_"):
            device_type = "bedside"
        elif entry.name.startswith("yeelink-light-ceiling1_"):
            device_type = "ceiling"
        elif entry.name.startswith("yeelink-light-ceiling2_"):
            device_type = "ceiling2"
        else:
            device_type = \
            entry.name.replace(DEVICE_NAME_PREFIX, '').rsplit('_', 1)[0]

        info[ATTR_DEVICE_TYPE] = device_type
        return info

    def get_entries(self):
        """ Return yeelight devices. """
        return self.find_by_device_name(DEVICE_NAME_PREFIX)
