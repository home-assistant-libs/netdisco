"""Xiaomi Mi Home (aka Lumi) Gateway discovery."""
import socket
import json
from datetime import timedelta


DISCOVERY_PORT = 4321
DISCOVERY_ADDRESS = "224.0.0.50"
DISCOVERY_PAYLOAD = b'{"cmd":"whois"}'
DISCOVERY_TIMEOUT = timedelta(seconds=2)


class XiaomiGw(object):
    """Base class to discover Xiaomi Gateway devices."""

    def __init__(self):
        """Initialize the discovery."""
        self.entries = []

    def scan(self):
        """Scan the network."""
        self.update()

    def all(self):
        """Scan and return all found entries."""
        self.scan()
        return self.entries

    def update(self):
        """Scan network for devices."""
        entries = []

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(DISCOVERY_TIMEOUT.seconds)
        sock.sendto(DISCOVERY_PAYLOAD, (DISCOVERY_ADDRESS, DISCOVERY_PORT))

        while True:
            try:
                data, (address, _) = sock.recvfrom(1024)
                #print(data, address)
                try:
                    entry = json.loads(data.decode("utf-8"))
                except:  # pylint: disable=bare-except
                    continue
                if entry.get("model") == "gateway":
                    entries.append(entry)

            except socket.timeout:
                break

            self.entries = entries

        sock.close()


def main():
    """Test Xiaomi GW discovery."""
    from pprint import pprint
    xiaomi = XiaomiGw()
    pprint("Scanning for Xiaomi GW devices..")
    xiaomi.update()
    pprint(xiaomi.entries)


if __name__ == "__main__":
    main()
