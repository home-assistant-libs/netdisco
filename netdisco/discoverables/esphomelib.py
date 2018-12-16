"""Discover Arduino devices."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering esphomelib devices."""

    def __init__(self, nd):
        super().__init__(nd, '_esphomelib._tcp.local.')
