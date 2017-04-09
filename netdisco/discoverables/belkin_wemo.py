"""Discover Belkin Wemo devices."""
from . import SSDPDiscoverable
from ..const import ATTR_MAC_ADDRESS


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Belkin WeMo platform devices."""

    def info_from_entry(self, entry):
        """Return most important info from a uPnP entry."""
        info = super().info_from_entry(entry)
        device = entry.description['device']
        info[ATTR_MAC_ADDRESS] = device.get('macAddress', '')
        return info

    def get_entries(self):
        """Return all Belkin Wemo entries."""
        return self.find_by_device_description(
            {'manufacturer': 'Belkin International Inc.'})
