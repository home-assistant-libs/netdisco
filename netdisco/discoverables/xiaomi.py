"""Discover Xiaomi Gateway devices."""
from . import BaseDiscoverable

from ..const import (
    ATTR_HOST, ATTR_PORT, ATTR_MAC_ADDRESS, ATTR_PROPERTIES)


class Discoverable(BaseDiscoverable):
    """Add support for discovering a Xiaomi GW device."""

    def __init__(self, netdis):
        """Initialize the discovery."""
        self._netdis = netdis

    def get_entries(self):
        """Get discovery results."""
        return self._netdis.xiaomi_gw.entries

    def info_from_entry(self, entry):
        info = {
            ATTR_HOST: entry["ip"],
            ATTR_PORT: int(entry["port"]),
            ATTR_MAC_ADDRESS: entry["sid"],
            ATTR_PROPERTIES: entry,
        }

        return info
