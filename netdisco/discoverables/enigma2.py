"""Discover Enigma2 servers."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering Enigma2 boxes."""

    def __init__(self, nd):
        """Initialize the Enigma2 discovery."""
        super(Discoverable, self).__init__(nd, '_e2stream._tcp.local.')
