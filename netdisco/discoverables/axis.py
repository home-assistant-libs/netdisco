"""Discover Axis devices."""
import ipaddress
from . import MDNSDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for discovering Axis devices."""

    def info_from_entry(self, entry):
        """Returns most important info from mDNS entries."""
        info = {
            'host': self.ip_from_host(entry.server),
            'name': entry.name.replace('.' + entry.type, ''),
            'serialnumber':  entry.properties[b'macaddress'].decode('utf-8')
            }
        return info

    def __init__(self, nd):
        """Initialize the Axis discovery."""
        super(Discoverable, self).__init__(nd, '_axis-video._tcp.local.')
