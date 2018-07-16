"""Discover Homekit devices."""
from . import MDNSDiscoverable

from ..const import ATTR_NAME


class Discoverable(MDNSDiscoverable):
    """Add support for discovering HomeKit devices."""

    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_hap._tcp.local.')

    def info_from_entry(self, entry):
        info = super(Discoverable, self).info_from_entry(entry)
        name = entry.name
        name = name.replace('._hap._tcp.local.', '')
        info[ATTR_NAME] = name
        return info
