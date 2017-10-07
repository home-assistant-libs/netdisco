"""Discover Songpal devices."""
from . import SSDPDiscoverable
from . import ATTR_PROPERTIES


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

        device_info_element = "X_ScalarWebAPI_DeviceInfo"
        device_element = "device"
        if device_element in cached_descs:
            if device_info_element in cached_descs[device_element]:
                scalarweb = cached_descs[device_element][device_info_element]

        properties = {"scalarwebapi": scalarweb,
                      "endpoint": scalarweb["X_ScalarWebAPI_BaseURL"]}
        info[ATTR_PROPERTIES] = properties

        return info
