"""Discover Home Assistant servers."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering mobile apps that support Home Assistant."""

    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_hass-mobile-app._tcp.local.')
