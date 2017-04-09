"""Discover devices that implement the Spotify Connect platform."""
from . import MDNSDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for discovering Spotify Connect service."""

    def __init__(self, nd):
        """Initialize the Cast discovery."""
        super(Discoverable, self).__init__(nd, '_spotify-connect._tcp.local.')
