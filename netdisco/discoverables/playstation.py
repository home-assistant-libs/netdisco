"""Discover devices."""
from . import BaseDiscoverable

PLAYSTATION3_BLUETOOTH_CLASS = '2883848'


class Discoverable(BaseDiscoverable):
    """Add support for discovering a device."""

    def __init__(self, netdis):
        """Initialize discovery."""
        self._netdis = netdis

    def get_entries(self):
        """Get all details."""
        # Could also use class: 0x2c0108
        # (props.Get("org.bluez.Device1", "Class"))
        ps3s = [entry for entry in self._netdis.bluetooth.entries
                if entry.bluetooth_class == PLAYSTATION3_BLUETOOTH_CLASS]
        return ps3s
