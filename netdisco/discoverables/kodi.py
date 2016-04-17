from . import MDNSDiscoverable


# pylint: disable=too-few-public-methods
class Discoverable(MDNSDiscoverable):
    """ Adds support for discovering KODI via ssdp and mdns """
    def __init__(self, nd):
        super(Discoverable, self).__init__(nd, '_http._tcp.local.')
        self.ssdp = self.netdis.ssdp

    def info_from_entry(self, entry):
        """ Returns the most important info from mDNS entries.
            Example: (name, url)
        """
        url = 'http://%s:%s' % (self.ip_from_host(entry.server), entry.port)
        return (entry.name.replace('._http._tcp.local', ''), url)

    def get_info(self):
        """ Returns found kodi via ssdp and mdns """
        seen_ssdp = []

        mdns = filter(None, [self.info_from_entry(entry) for entry
                      in self.get_entries() if entry.name.startswith('Kodi ')])

        # Lets see if we can find kodi via ssdp
        for k in self.ssdp.find_by_device_description({"manufacturer": "XBMC Foundation"}):
            des = k.description
            t = (des['device']['friendlyName'], des['device']['presentationURL'])
            seen_ssdp.append(t)


        return list(set(mdns + seen_ssdp))
