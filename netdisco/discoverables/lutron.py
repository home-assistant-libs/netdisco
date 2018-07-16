"""Discover Lutron Caseta Smart Bridge and Smart Bridge Pro devices."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering Lutron Caseta Smart Bridge
    and Smart Bridge Pro devices."""

    def __init__(self, nd):
        """Initialize the Lutron Smart Bridge discovery."""
        super(Discoverable, self).__init__(nd, '_lutron._tcp.local.')
