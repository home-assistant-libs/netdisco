"""Discovers Orvibo switches."""

import binascii

from . import BaseDiscoverable


class Discoverable(BaseDiscoverable):
    """Adds support for discovering Orvibo switches."""

    def __init__(self, netdis):
        self.netdis = netdis

    def get_entries(self):
        return [(key, binascii.hexlify(vals['mac']))
                for key, vals in self.netdis.orvibo.entries.items()]
