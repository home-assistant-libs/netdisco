"""Discover PlexMediaServer."""
from . import GDMDiscoverable
from ..const import ATTR_NAME, ATTR_HOST, ATTR_PORT, ATTR_URLBASE


class Discoverable(GDMDiscoverable):
    """Add support for discovering Plex Media Server."""

    def info_from_entry(self, entry):
        """Return most important info from a GDM entry."""
        return {
            ATTR_NAME: entry['data']['Name'],
            ATTR_HOST: entry['from'][0],
            ATTR_PORT: entry['data']['Port'],
            ATTR_URLBASE: 'https://%s:%s' % (entry['from'][0],
                                             entry['data']['Port'])
        }

    def get_entries(self):
        """Return all PMS entries."""
        return self.find_by_data({'Content-Type': 'plex/media-server'})
