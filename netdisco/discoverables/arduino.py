"""Discover Arduino devices."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering Arduino devices."""

    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_arduino._tcp.local.')
