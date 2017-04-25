"""Tellstick device discovery."""
import socket
from datetime import timedelta
import logger

DISCOVERY_PORT = 30303
DISCOVERY_ADDRESS = '<broadcast>'
DISCOVERY_PAYLOAD = b"D"
DISCOVERY_TIMEOUT = timedelta(seconds=5)

_LOGGER =  logging.getLogger(__name__)

class Tellstick(object):
    """Base class to discover Tellstick devices."""

    def __init__(self):
        """Initialize the Tellstick discovery."""
        self.entries = []

    def scan(self):
        """Scan the network."""
        self.update()

    def all(self):
        """Scan and return all found entries."""
        self.scan()
        return self.entries

    def update(self):
        """Scan network for Tellstick devices."""
        entries = []

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.settimeout(DISCOVERY_TIMEOUT.seconds)
            sock.sendto(DISCOVERY_PAYLOAD, (DISCOVERY_ADDRESS, DISCOVERY_PORT))
        except Exception as e:
            _LOGGER.exception("tellstick: Exception in sending: %s",
                              str(e))
            self.entries = []
            return
        
        while True:
            try:
                data, (address, _) = sock.recvfrom(1024)
                entry = data.decode("ascii").split(":")
                # expecting product, mac, activation code, version
                if len(entry) != 4:
                    continue
                entry = (address,) + tuple(entry)
                entries.append(entry)

            except socket.timeout:
                break
            except Exception as e:
                _LOGGER.exception("tellstick: Exception in receiving: %s",
                                  str(e))
                break

            self.entries = entries

        sock.close()


def main():
    """Test Tellstick discovery."""
    from pprint import pprint
    tellstick = Tellstick()
    pprint("Scanning for Tellstick devices..")
    tellstick.update()
    pprint(tellstick.entries)


if __name__ == "__main__":
    main()
