"""Discover Axis devices."""
from . import MDNSDiscoverable

from ..const import (
    ATTR_HOST, ATTR_PORT, ATTR_HOSTNAME, ATTR_PROPERTIES)


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for discovering Axis devices."""

    def info_from_entry(self, entry):
        """Return most important info from mDNS entries."""
        properties = {}

        for key, value in entry.properties.items():
            if isinstance(value, bytes):
                value = value.decode('utf-8')
            properties[key.decode('utf-8')] = value

        return {
            ATTR_HOST: self.ip_from_host(entry.server),
            ATTR_PORT: entry.port,
            ATTR_HOSTNAME: entry.server,
            ATTR_PROPERTIES: properties,
        }

    def __init__(self, nd):
        """Initialize the Axis discovery."""
        super(Discoverable, self).__init__(nd, '_axis-video._tcp.local.')

    def ip_from_host(self, host):
        """Attempt to return the ip address from an mDNS host.

        Return host if failed.
        """
        ips = self.netdis.mdns.zeroconf.cache.entries_with_name(host.lower())

        try:
            return repr(ips[0]) if ips else host
        except TypeError:
            return host
