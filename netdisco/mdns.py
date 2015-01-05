""" Adds support for discovering mDNS services. """
import zeroconf


class MDNS(object):
    """ Base class to discover mDNS services. """
    def __init__(self):
        self.zeroconf = zeroconf.Zeroconf()

    def stop(self):
        """ Stop discovering. """
        self.zeroconf.close()
        self.zeroconf = None

    @property
    def entries(self):
        """ Return all entries in the cache. """
        return self.zeroconf.cache.entries()
