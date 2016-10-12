"""Discover Home Assistant iOS app."""
from . import MDNSDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for discovering the Home Assistant iOS app."""

    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_hass-ios._tcp.local.')

    def info_from_entry(self, entry):
        """Returns most important info from mDNS entries."""
        return (entry.properties.get(b'buildNumber').decode('utf-8'),
                entry.properties.get(b'versionNumber').decode('utf-8'),
                entry.properties.get(b'permanentID').decode('utf-8'),
                entry.properties.get(b'bundleIdentifer').decode('utf-8'))

    def get_info(self):
        """Get details from Home Assistant iOS app instances."""
        return [self.info_from_entry(entry) for entry in self.get_entries()]
