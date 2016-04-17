"""Discovers PlexMediaServer."""

from . import GDMDiscoverable


class Discoverable(GDMDiscoverable):
    """Adds support for discovering Plex Media Server."""

    def info_from_entry(self, entry):
        """Returns most important info from a GDM entry."""
        return entry['data']['Name'], \
            'https://%s:%s' % (entry['from'][0], entry['data']['Port'])

    def get_entries(self):
        """Returns all PMS entries."""
        return self.find_by_data({'Content-Type': 'plex/media-server'})
