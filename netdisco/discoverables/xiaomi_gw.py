"""Discover Xiaomi Mi Home (aka Lumi) Gateways."""
from . import MDNSDiscoverable
from ..const import ATTR_MAC_ADDRESS, ATTR_PROPERTIES


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """Add support for discovering Xiaomi Gateway"""

    def __init__(self, nd):
        """Initialize the discovery."""
        super(Discoverable, self).__init__(nd, '_miio._udp.local.')

    def info_from_entry(self, entry):
        """Return most important info from mDNS entries."""
        info = super().info_from_entry(entry)

        # Workaround of misparsing of mDNS properties. It's unclear
        # whether it's bug in zeroconf module or in the Gateway, but
        # returned properties look like:
        # {b'poch': b'0:mac=286c07aaaaaa\x00'} instead of expected:
        # {b'epoch': b'0', b'mac': '286c07aaaaaa'}
        if "poch" in info[ATTR_PROPERTIES]:
            misparsed = info[ATTR_PROPERTIES]["poch"]
            misparsed = misparsed.rstrip("\0")
            for val in misparsed.split(":"):
                if val.startswith("mac="):
                    info[ATTR_MAC_ADDRESS] = val[len("mac="):]

        return info

    def get_entries(self):
        """Return Xiaomi Gateway devices."""
        return self.find_by_device_name('lumi-gateway-')
