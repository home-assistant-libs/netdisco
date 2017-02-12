"""Philips Hue bridge discovery using N-UPnP.

Philips Hue bridge limits how many SSDP lookups you can make. To work
around this they recommend to do N-UPnP lookup simultaneously with
SSDP lookup: https://developers.meethue.com/documentation/hue-bridge-discovery

"""

import xml.etree.ElementTree as ElementTree

import requests

from netdisco.util import etree_to_dict


# pylint: disable=too-few-public-methods
class PHueBridge(object):
    """Parses Philips Hue bridge description XML into an
    object similar to UPNPEntry.

    """

    def __init__(self, description_xml):
        tree = ElementTree.fromstring(description_xml)
        self.description = etree_to_dict(tree).get("root", {})

    def __repr__(self):
        friendly_name = self.description['device']['friendlyName']
        url_base = self.description['URLBase']

        return str((friendly_name, url_base))


class PHueNUPnPDiscovery(object):
    """Philips Hue bridge discovery using N-UPnP."""

    PHUE_NUPNP_URL = "https://www.meethue.com/api/nupnp"
    DESCRIPTION_URL_TMPL = "http://{}/description.xml"

    def __init__(self):
        self.entries = []

    def scan(self):
        """Scan the network."""
        response = requests.get(self.PHUE_NUPNP_URL)
        if response.status_code == 200:
            bridges = response.json()
            for bridge in bridges:
                entry = self.fetch_description(bridge)
                if entry:
                    self.entries.append(entry)

    def fetch_description(self, bridge):
        """Fetches description XML of a Philips Hue bridge."""
        url = self.bridge_description_url(bridge)
        response = requests.get(url)
        if response.status_code == 200:
            return PHueBridge(response.text)

    def bridge_description_url(self, bridge):
        """Returns URL for fetching description XML"""
        ipaddr = bridge["internalipaddress"]
        return self.DESCRIPTION_URL_TMPL.format(ipaddr)


def main():
    """Test N-UPnP discovery."""
    from pprint import pprint

    disco = PHueNUPnPDiscovery()
    disco.scan()
    pprint(disco.entries)


if __name__ == "__main__":
    main()
