"""Discover Home Assistant servers."""
from . import MDNSDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for discovering Home Assistant instances."""

    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_home-assistant._tcp.local.')
