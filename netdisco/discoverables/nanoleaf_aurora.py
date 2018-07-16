"""Discover Nanoleaf Aurora devices."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering Nanoleaf Aurora devices."""

    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_nanoleafapi._tcp.local.')
