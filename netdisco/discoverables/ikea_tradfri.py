"""Discover devices that implement the Ikea Tradfri platform."""
from . import MDNSDiscoverable


class Discoverable(MDNSDiscoverable):
    """Add support for discovering Ikea Tradfri devices."""

    def __init__(self, nd):
        """Initialize the Cast discovery."""
        super(Discoverable, self).__init__(nd, '_coap._udp.local.')
