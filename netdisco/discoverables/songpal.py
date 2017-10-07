"""Discover Songpal devices."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Support for Songpal devices.
    Supported devices: http://vssupport.sony.net/en_ww/device.html."""

    def get_entries(self):
        """Get all the Songpal devices."""
        return self.find_by_st(
            "urn:schemas-sony-com:service:ScalarWebAPI:1")

    def info_from_entry(self, entry):
        """Get information for a device.."""
        info = super().info_from_entry(entry)

        return info
