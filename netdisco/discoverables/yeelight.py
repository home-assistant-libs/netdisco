"""Discover Yeelight bulbs, based on Kodi discoverable."""
from . import MDNSDiscoverable
import logging


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for discovering Yeelight."""

    def __init__(self, nd):
        """Initialize the Yeelight discovery."""
        super(Discoverable, self).__init__(nd, '_miio._udp.local.')

    def info_from_entry(self, entry):
        """Return most important info from mDNS entries."""

        device_type = "UNKNOWN"
        if entry.name.startswith("yeelink-light-color1_"):
            device_type = "rgb"
        elif entry.name.startswith("yeelink-light-mono1_"):
            device_type = "white"
        else:
            logging.warning("Unknown miio device found: %s", entry)

        return {"host": self.ip_from_host(entry.server),
                "port": entry.port,
                "hostname": entry.server,
                "device_type": device_type,
                "properties": entry.properties}

    def get_entries(self):
        return self.find_by_device_name('yeelink-light-')
