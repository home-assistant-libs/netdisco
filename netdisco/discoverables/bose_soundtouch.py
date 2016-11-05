"""Discover Bose SoundTouch devices."""
from . import MDNSDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for discovering Bose SoundTouch devices."""

    def __init__(self, nd):
        """Initialize the Bose SoundTouch discovery."""
        super(Discoverable, self).__init__(nd, '_soundtouch._tcp.local.')
