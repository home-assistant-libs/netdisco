"""Discover Axis devices."""
from . import MDNSDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for discovering Axis devices."""

    def __init__(self, nd):
        """Initialize the Axis discovery."""
        super(Discoverable, self).__init__(nd, '_axis-video._tcp.local.')
