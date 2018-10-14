"""Discover LG smart devices."""
from . import MDNSDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for discovering LG smart devices."""

    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_lg-smart-device._tcp.local.')
