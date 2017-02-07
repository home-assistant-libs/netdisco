"""Discover frontier silicon devices."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering frontier silicon devices."""

    def get_entries(self):
        """Get all the frontier silicon uPnP entries."""
        return [entry for entry in self.netdis.ssdp.all()
                if entry.st and 'fsapi' in entry.st and
                'urn:schemas-frontier-silicon-com' in entry.st]
