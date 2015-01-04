""" Provides helpful stuff for discoverables. """


class BaseDiscoverable(object):
    """ Base class for discoverable services or device types. """

    def is_discovered(self):
        """ Returns True if it is discovered. """
        return len(self.get_entries()) > 0

    def get_info(self):
        """
        Return a list with the important info for each item.
        Uses self.info_from_entry internally.
        """
        return [self.info_from_entry(entry) for entry in self.get_entries()]

    # pylint: disable=no-self-use
    def info_from_entry(self, entry):
        """ Return an object with important info from the entry. """
        return entry

    # pylint: disable=no-self-use
    def get_entries(self):
        """ Returns all the discovered entries. """
        return []
