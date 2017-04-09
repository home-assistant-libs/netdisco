"""Discover Apple TV media players."""
import ipaddress
from . import MDNSDiscoverable
from ..const import ATTR_HOST, ATTR_NAME


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for Apple TV devices."""

    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_appletv-v2._tcp.local.')

    def info_from_entry(self, entry):
        """Returns most important info from mDNS entries."""
        props = entry.properties
        return {
            ATTR_HOST: str(ipaddress.ip_address(entry.address)),
            ATTR_NAME: props.get(b'Name').decode('utf-8').replace('\xa0', ' '),
            'hsgid': props.get(b'hG').decode('utf-8')
            }
