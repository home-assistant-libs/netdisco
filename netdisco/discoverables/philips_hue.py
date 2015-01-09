""" Discovers Philips Hue bridges. """

from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """ Adds support for discovering Philips Hue bridges. """

    def info_from_entry(self, entry):
        """ Returns the most important info from a uPnP entry. """
        device = entry.description.find('device')

        return (device.find('friendlyName').text,
                entry.description.find('URLBase').text)

    def get_entries(self):
        """ Get all the Hue bridge uPnP entries. """
        return self.find_by_device_description({
            "manufacturer": "Royal Philips Electronics",
            "modelNumber": "929000226503"
        })
