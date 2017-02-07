"""Discover Apple TV media players."""
import ipaddress
from . import MDNSDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for Apple TV devices."""

    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_appletv-v2._tcp.local.')

    def info_from_entry(self, entry):
        """Returns most important info from mDNS entries."""
        props = entry.properties
        info = {
            'host': str(ipaddress.ip_address(entry.address)),
            'name': props.get(b'Name').decode('utf-8').replace('\xa0', ' '),
            'hsgid': props.get(b'hG').decode('utf-8')
            }
        return info

    def get_info(self):
        """Get details from Apple TV instances."""
        return [self.info_from_entry(entry) for entry in self.get_entries()]
