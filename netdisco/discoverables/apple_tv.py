"""Discover Apple TV media players."""
import ipaddress
from . import MDNSDiscoverable
from ..const import ATTR_HOST, ATTR_NAME, ATTR_PROPERTIES


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for Apple TV devices."""

    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_appletv-v2._tcp.local.')

    def info_from_entry(self, entry):
        """Returns most important info from mDNS entries."""
        info = super().info_from_entry(entry)
        info[ATTR_HOST] = str(ipaddress.ip_address(entry.address))
        info[ATTR_NAME] = info[ATTR_PROPERTIES]['Name'].replace('\xa0', ' ')
        return info
