""" Discovers devices that implement the Google Cast platform. """

from . import MDNSDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """ Adds support for discovering Google Cast platform devices. """

    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_googlecast._tcp.local.')
