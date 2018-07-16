"""Discover Freebox routers."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering Freebox routers."""

    def __init__(self, nd):
        """Initialize the Freebox discovery."""
        super(Discoverable, self).__init__(nd, '_fbx-api._tcp.local.')
