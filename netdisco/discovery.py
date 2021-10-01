"""Combine all the different protocols into a simple interface."""
import logging
import os
import importlib

from .ssdp import SSDP
from .mdns import MDNS

_LOGGER = logging.getLogger(__name__)


class NetworkDiscovery:
    """Scan the network for devices.

    mDNS scans in a background thread.
    SSDP scans in the foreground.

    start: is ready to scan
    scan: scan the network
    discover: parse scanned data
    get_in
    """

    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        """Initialize the discovery."""

        self.mdns = None
        self.ssdp = None

        self.is_discovering = False
        self.discoverables = None

    def scan(self, zeroconf_instance=None, suppress_mdns_types=None):
        """Start and tells scanners to scan."""
        self.is_discovering = True

        self.mdns = MDNS(zeroconf_instance)

        # Needs to be after MDNS init
        self._load_device_support()

        if suppress_mdns_types:
            for type_ in suppress_mdns_types:
                self.mdns.unregister_type(type_)

        self.mdns.start()

        self.ssdp = SSDP()
        self.ssdp.scan()

    def stop(self):
        """Turn discovery off."""
        if not self.is_discovering:
            return

        self.mdns.stop()

        # Not removing SSDP because it tracks state
        self.mdns = None
        self.discoverables = None
        self.is_discovering = False

    def discover(self):
        """Return a list of discovered devices and services."""
        if not self.is_discovering:
            raise RuntimeError("Needs to be called after start, before stop")

        return [dis for dis, checker in self.discoverables.items()
                if checker.is_discovered()]

    def get_info(self, dis):
        """Get a list with the most important info about discovered type."""
        return self.discoverables[dis].get_info()

    def get_entries(self, dis):
        """Get a list with all info about a discovered type."""
        return self.discoverables[dis].get_entries()

    def _load_device_support(self):
        """Load the devices and services that can be discovered."""
        self.discoverables = {}

        discoverables_format = __name__.rsplit('.', 1)[0] + '.discoverables.{}'

        for module_name in os.listdir(os.path.join(os.path.dirname(__file__),
                                                   'discoverables')):
            if module_name[-3:] != '.py' or module_name == '__init__.py':
                continue

            module_name = module_name[:-3]

            module = importlib.import_module(
                discoverables_format.format(module_name))

            self.discoverables[module_name] = \
                getattr(module, 'Discoverable')(self)

    def print_raw_data(self):
        """Helper method to show what is discovered in your network."""
        from pprint import pprint

        print("Zeroconf")
        pprint(self.mdns.entries)
        print("")
        print("SSDP")
        pprint(self.ssdp.entries)
