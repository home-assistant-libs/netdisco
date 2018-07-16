"""Discover Yeelight bulbs, based on Kodi discoverable."""
from . import MDNSDiscoverable
from ..const import ATTR_DEVICE_TYPE

DEVICE_NAME_PREFIX = 'yeelink-light-'


class Discoverable(MDNSDiscoverable):
    """Add support for discovering Yeelight."""

    def __init__(self, nd):
        """Initialize the Yeelight discovery."""
        super(Discoverable, self).__init__(nd, '_miio._udp.local.')

    def info_from_entry(self, entry):
        """Return most important info from mDNS entries."""
        info = super().info_from_entry(entry)

        # Example name: yeelink-light-ceiling4_mibt72799069._miio._udp.local.
        info[ATTR_DEVICE_TYPE] = \
            entry.name.replace(DEVICE_NAME_PREFIX, '').split('_', 1)[0]

        return info

    def get_entries(self):
        """ Return yeelight devices. """
        return self.find_by_device_name(DEVICE_NAME_PREFIX)
