"""Discover myStrom devices."""
from . import MDNSDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for discovering myStrom switches."""

    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_hap._tcp.local.')
