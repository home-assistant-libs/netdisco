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

        cached_descs = entry.DESCRIPTION_CACHE[entry.location]

        DEVICEINFO = "X_ScalarWebAPI_DeviceInfo"
        DEVICE = "device"
        if DEVICE in cached_descs:
            if DEVICEINFO in cached_descs[DEVICE]:
                scalarweb = cached_descs[DEVICE][DEVICEINFO]

        info["scalarwebapi"] = scalarweb
        info["endpoint"] = scalarweb["X_ScalarWebAPI_BaseURL"]

        return info
