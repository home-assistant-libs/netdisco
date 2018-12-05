"""Discover HF-LPB100 chip based devices."""
from netdisco.discoverables import BaseDiscoverable


class Discoverable(BaseDiscoverable):
    """HF-LPB100 chip based discoverable."""

    def __init__(self, netdis):
        """Initialize the HF-LPB100 chip based discovery."""
        self._netdis = netdis

    def get_entries(self):
        """Get all the Sunix Controller device details."""
        return self._netdis.hf_lpb100.entries
