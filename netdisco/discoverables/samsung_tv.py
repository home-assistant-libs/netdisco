"""Discover Samsung Smart TV services."""
from . import SSDPDiscoverable
from ..const import ATTR_NAME

# For some models, Samsung forces a [TV] prefix to the user-specified name.
FORCED_NAME_PREFIX = '[TV]'


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Samsung Smart TV services."""

    def get_entries(self):
        """Get all the Samsung RemoteControlReceiver entries."""
        return self.find_by_st(
            "urn:samsung.com:device:RemoteControlReceiver:1")

    def info_from_entry(self, entry):
        """Get most important info, by default the description location."""
        info = super().info_from_entry(entry)

        # Strip the forced prefix, if present
        if info[ATTR_NAME].startswith(FORCED_NAME_PREFIX):
            info[ATTR_NAME] = info[ATTR_NAME][len(FORCED_NAME_PREFIX):].strip()

        return info
