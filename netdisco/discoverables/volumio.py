"""Discover Volumio servers."""
from . import MDNSDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for discovering Volumio."""

    def __init__(self, nd):
        """Initialize the Volumio discovery."""
        super(Discoverable, self).__init__(nd, '_Volumio._tcp.local.')
