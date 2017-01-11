"""Discover Yeelight bulbs, based on Kodi discoverable."""
import logging
from . import MDNSDiscoverable
from ..const import (
    ATTR_HOST, ATTR_PORT, ATTR_HOSTNAME, ATTR_DEVICE_TYPE, ATTR_PROPERTIES)


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

        def _decode_properties(props):
            return {x.decode("utf-8"): props[x].decode("utf-8")
                    for x in props}

        return {
            ATTR_HOST: self.ip_from_host(entry.server),
            ATTR_PORT: entry.port,
            ATTR_HOSTNAME: entry.server,
            ATTR_DEVICE_TYPE: device_type,
            ATTR_PROPERTIES: _decode_properties(entry.properties)
        }

    def get_entries(self):
        """ Return yeelight devices. """
        return self.find_by_device_name('yeelink-light-')
