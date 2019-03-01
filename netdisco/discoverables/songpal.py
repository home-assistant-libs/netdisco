"""Discover Songpal devices."""
import logging
from . import SSDPDiscoverable
from . import ATTR_PROPERTIES


class Discoverable(SSDPDiscoverable):
    """Support for Songpal devices.
    Supported devices: http://vssupport.sony.net/en_ww/device.html."""

    def get_entries(self):
        """Get all the Songpal devices."""
        devs = self.find_by_st(
            "urn:schemas-sony-com:service:ScalarWebAPI:1")

        # At least some Bravia televisions use the same API for communication,
        # but are handled by another platforms, so we filter them out here.
        supported = []
        for dev in devs:
            if 'device' in dev.description:
                device = dev.description['device']
                scalarweb_info = device.get("X_ScalarWebAPI_DeviceInfo", None)

                if scalarweb_info:
                    services = scalarweb_info["X_ScalarWebAPI_ServiceList"]
                    service_types = services["X_ScalarWebAPI_ServiceType"]
                    # Sony Bravias offer videoScreen service, soundbars do not
                    if 'videoScreen' in service_types:
                        continue

                supported.append(dev)

        return supported

    def info_from_entry(self, entry):
        """Get information for a device.."""
        info = super().info_from_entry(entry)

        cached_descs = entry.DESCRIPTION_CACHE[entry.location]

        device_info_element = "X_ScalarWebAPI_DeviceInfo"
        baseurl_element = "X_ScalarWebAPI_BaseURL"
        device_element = "device"
        if device_element in cached_descs and \
                device_info_element in cached_descs[device_element]:
            scalarweb = cached_descs[device_element][device_info_element]

            properties = {"scalarwebapi": scalarweb}
            if baseurl_element in scalarweb:
                properties["endpoint"] = scalarweb[baseurl_element]
            else:
                logging.warning("Unable to find %s", baseurl_element)
            info[ATTR_PROPERTIES] = properties
        else:
            logging.warning("Unable to find ScalarWeb element from desc.")

        return info
