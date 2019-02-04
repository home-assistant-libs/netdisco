"""
Discover Sercomm network cameras.
These are rebranded as iControl and many others, and are usually
distributed as part of an ADT or Comcast/Xfinity monitoring package.
https://github.com/edent/Sercomm-API
"""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering camera services."""

    def get_entries(self):
        """Get all Sercomm iControl devices."""
        return self.find_by_device_description({'manufacturer': 'iControl'})
