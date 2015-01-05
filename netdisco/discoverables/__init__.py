""" Provides helpful stuff for discoverables. """
import zeroconf


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


class SSDPDiscoverable(BaseDiscoverable):
    """ uPnP discoverable base class. """

    def __init__(self, netdis):
        self.netdis = netdis

    def get_info(self):
        """ Gets most important info, by default the description location. """
        return list(set(
            entry.values['location'] for entry in self.get_entries()))

    # Helper functions

    # pylint: disable=invalid-name
    def find_by_st(self, st):
        """ Find entries by ST (the device identifier). """
        return self.netdis.ssdp.find_by_st(st)

    def find_by_device_description(self, values):
        """ Find entries based on values from their description. """
        return self.netdis.ssdp.find_by_device_description(values)


class MDNSDiscoverable(BaseDiscoverable):
    """ mDNS Discoverable base class. """

    def __init__(self, netdis, typ):
        self.netdis = netdis

        self.services = {}

        # TODO track ServiceBrowser in MDNS class, call .cancel on each on stop
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
