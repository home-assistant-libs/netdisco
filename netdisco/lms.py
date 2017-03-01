"""Squeezebox/Logitech Media server discovery."""
import socket

from .const import ATTR_HOST, ATTR_PORT

DISCOVERY_PORT = 3483
DEFAULT_DISCOVERY_TIMEOUT = 5


class LMS(object):
    """Base class to discover Logitech Media servers."""

    def __init__(self):
        """Initialize the Logitech discovery."""
        self.entries = []
        self.last_scan = None

    def scan(self):
        """Scan the network."""
        self.update()

    def all(self):
        """Scan and return all found entries."""
        self.scan()
        return list(self.entries)

    def update(self):
        """Scan network for Logitech Media Servers."""
        lms_ip = '<broadcast>'
        lms_port = DISCOVERY_PORT
        lms_msg = b"eJSON\0"
        lms_timeout = DEFAULT_DISCOVERY_TIMEOUT

        entries = []

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.settimeout(lms_timeout)
        sock.bind(('', 0))

        try:
            sock.sendto(lms_msg, (lms_ip, lms_port))

            while True:
                try:
                    data, server = sock.recvfrom(1024)
                    if data.startswith(b'E'):
                        # Full response is EJSON\xYYXXXX
                        # Where YY is length of port string (ie 4)
                        # And XXXX is the web interface port (ie 9000)
                        port = None
                        if data.startswith(b'JSON', 1):
                            length = data[5:6][0]
                            port = int(data[0-length:])
                        entries.append({
                            ATTR_HOST: server[0],
                            ATTR_PORT: port,
                        })
                except socket.timeout:
                    break
        finally:
            sock.close()
        self.entries = entries


def main():
    """Test LMS discovery."""
    from pprint import pprint

    # pylint: disable=invalid-name
    lms = LMS()

    pprint("Scanning for Logitech Media Servers...")
    lms.update()
    pprint(lms.entries)


if __name__ == "__main__":
    main()
