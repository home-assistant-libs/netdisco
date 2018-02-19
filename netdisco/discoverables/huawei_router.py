"""Discover Huawei routers."""
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Huawei routers."""

    def get_entries(self):
        """Get all the Huawei uPnP entries."""
        return self.find_by_device_description({
            "manufacturer": "Huawei Technologies Co., Ltd.",
            "deviceType": "urn:schemas-upnp-org:device:InternetGatewayDevice:1"
        })
