""" Adds support for discovering mDNS services. """
import zeroconf

from netdisco.discoverables import BaseDiscoverable


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


class MDNSDiscoverable(BaseDiscoverable):
    """ mDNS Discoverable base class. """

    def __init__(self, netdis, typ):
        self.netdis = netdis

        self.services = {}

        zeroconf.ServiceBrowser(netdis.mdns.zeroconf, typ, self)

    def is_discovered(self):
        """ Returns True if any device has been discovered. """
        return len(self.services) > 0

    # pylint: disable=unused-argument
    def remove_service(self, zconf, typ, name):
        """ Callback when a service is removed. """
        self.services.pop(name)

    def add_service(self, zconf, typ, name):
        """ Callback when a service is found. """
        self.services[name] = zconf.get_service_info(typ, name)

    def get_entries(self):
        """ Return all found services. """
        return self.services.values()

    # To be overwritten
    def info_from_entry(self, entry):
        """ Return most important info from a mDNS service entry. """
        return entry
