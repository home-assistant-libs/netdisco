""" Discovers Belkin Wemo devices. """

from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """ Adds support for discovering Belkin WeMo platform devices. """

    def info_from_entry(self, entry):
        """ Returns most important info from a uPnP entry. """
        device = entry.description.find('device')

        return (device.find('friendlyName').text,
                device.find('modelName').text,
                entry.values['location'])

    def get_entries(self):
        """ Returns all Belkin Wemo entries. """
        return self.find_by_st('urn:Belkin:service:manufacture:1')
