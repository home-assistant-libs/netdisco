"""XLED Twinkly device discovery."""
import ipaddress
import socket
from datetime import timedelta

from .const import ATTR_HOST, ATTR_NAME


DISCOVERY_PORT = 5555
DISCOVERY_ADDRESS_BCAST = '<broadcast>'
DISCOVERY_REQUEST = b'\x01discover'
DISCOVERY_TIMEOUT = timedelta(seconds=2)


class XLED:
    """Base class to discover XLED Twinkly devices."""

    def __init__(self):
        """Initialize the XLED discovery."""
        self.entries = []
        self.last_scan = None

    @staticmethod
    def parse_discovery_response(data):
        """Parse discovery response."""

        # First four bytes in reversed order
        ip_address_data = data[3::-1]
        ip_address_data = bytes(ip_address_data)

        ip_address_obj = ipaddress.ip_address(ip_address_data)
        ip_address_exploded = ip_address_obj.exploded
        if not isinstance(ip_address_exploded, bytes):
            ip_address_exploded = bytes(ip_address_exploded, 'utf-8')

        device_name = data[6:-1]
        device_name = bytes(device_name)

        return {ATTR_NAME: device_name.decode('utf-8')}

    def scan(self):
        """Scan the network for Twinkly devices."""
        self.update()

    def all(self):
        """Scan and return all found entries."""
        self.scan()
        return self.entries

    @staticmethod
    def verify_packet(data):
        """Parse packet if it has correct magic"""
        if len(data) < 7:
            return None

        if data[4:6] != b'OK':
            return None

        if data[-1] != 0:
            return None

        return XLED.parse_discovery_response(data)

    def update(self):
        """Scan network for XLED Twinkly devices."""
        entries = []
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,
                             socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(DISCOVERY_TIMEOUT.seconds)

        sock.sendto(DISCOVERY_REQUEST, 0, (DISCOVERY_ADDRESS_BCAST,
                                           DISCOVERY_PORT))

        while True:
            try:
                data, (address, _) = sock.recvfrom(1024)

                response = self.verify_packet(data)
                if response:
                    if response == DISCOVERY_REQUEST:
                        continue
                    entries.append({
                        ATTR_HOST: address,
                        ATTR_NAME: response[ATTR_NAME]
                    })

            except socket.timeout:
                break

        self.entries = entries

        sock.close()


def main():
    """Test XLED Twinkly discovery."""
    from pprint import pprint

    xled = XLED()

    pprint("Scanning for XLED devices..")
    xled.update()
    pprint(xled.entries)


if __name__ == "__main__":
    main()
