"""Discover TiVo DVR devices providing the TCP Remote Protocol."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering TiVo Remote Protocol service."""

    def __init__(self, nd):
        """Initialize the discovery.

        Yields a dictionary with hostname, host and port along with a
        properties sub-dictionary with some device specific ids.
        """
        super(Discoverable, self).__init__(nd, '_tivo-remote._tcp.local.')
