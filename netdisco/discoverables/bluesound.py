"""Discover devices that implement the Bluesound platform."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering Bluesound service."""

    def __init__(self, nd):
        """Initialize the Bluesound discovery."""
        super(Discoverable, self).__init__(nd, '_musc._tcp.local.')
