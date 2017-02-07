"""Fluxled device discovery.

Ideally this would be done using broadcast. But some fluxled
devices do not respond well to broadcast. So instead we send
a packet to every device in the network. This is the way the
offical app 'Magic Home' does it as well.

"""

# pylint:disable=wrong-import-order
import ipaddress
import logging
import socket
import sys
import threading
from datetime import timedelta

from netdisco.util import interface_networks

DISCOVERY_PORT = 48899
DISCOVERY_PAYLOAD = "HF-A11ASSISTHREAD".encode('ascii')
DISCOVERY_TIMEOUT = timedelta(seconds=5)

LOG = logging.getLogger(__name__)


class FluxLed(object):
    """Base class to discover Fluxled devices."""

    def __init__(self, networks=None):
        """Initialize the flux_led discovery."""
        self.entries = []
        self._lock = threading.RLock()

        # if not explicitly specified determine network from interfaces
        if networks:
            self.networks = set(networks)
        else:
            self.networks = set(interface_networks())

    def scan(self):
        """Scan the network."""
        with self._lock:
            self.update()

    def all(self):
        """Scan and return all found entries."""
        self.scan()
        return self.entries

    def update(self):
        """Scan network for Fluxled devices."""

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', DISCOVERY_PORT))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(DISCOVERY_TIMEOUT.seconds)

        # send query to every device in every network connected to
        LOG.debug('querying hosts on networks: %s', self.networks)
        for network in self.networks:
            for address in network.hosts():
                try:
                    sock.sendto(DISCOVERY_PAYLOAD,
                                (str(address), DISCOVERY_PORT))
                except OSError as exc:
                    LOG.debug('failed to send request', exc_info=exc)
                    continue

        # wait for responses
        while True:
            try:
                data, _ = sock.recvfrom(64)
            except socket.timeout:
                # no (more) responses received
                break

            # skip our own outgoing packet
            if data == DISCOVERY_PAYLOAD:
                continue

            # data = ip_address,id,model
            data = data.decode('ascii').split(',')
            if len(data) < 3:
                continue

            entry = tuple(data)

            if entry not in self.entries:
                self.entries.append(entry)

        sock.close()


def main():
    """Test Fluxled discovery."""
    from pprint import pprint

    if len(sys.argv) >= 2:
        networks = [ipaddress.IPv4Network(n) for n in sys.argv[1:]]
    else:
        networks = None

    logging.basicConfig(level=logging.DEBUG)

    flux_led = FluxLed(networks=networks)
    pprint("Scanning for FluxLed devices..")
    flux_led.update()
    pprint(flux_led.entries)


if __name__ == "__main__":
    main()
