"""Discover Home Assistant iOS app."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering the Home Assistant iOS app."""

    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_hass-ios._tcp.local.')
