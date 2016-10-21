"""Discover Yamaha Receivers."""
from netdisco.util import urlparse
from . import SSDPDiscoverable


class Discoverable(SSDPDiscoverable):
    """Add support for discovering Yamaha Receivers."""

    def info_from_entry(self, entry):
        """Return the most important info from a uPnP entry."""
        descurl = entry.values['location']
        url = urlparse(entry.values['location'])
        yam = entry.description['X_device']
        ctrlurl = "%s://%s%s" % (
            url.scheme,
            url.netloc,
            yam['X_serviceList']['X_service']['X_controlURL'])
        device = entry.description['device']

        return (device['friendlyName'], ctrlurl, descurl)

    def get_entries(self):
        """Get all the Yamaha uPnP entries."""
        return self.find_by_device_description({
            "manufacturer": "Yamaha Corporation",
            "deviceType": "urn:schemas-upnp-org:device:MediaRenderer:1"
        })
