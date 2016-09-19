"""Daikin device discovery."""
import socket
import threading

# pylint: disable=unused-import, import-error, no-name-in-module
try:
    # Py2
    from urlparse import unquote  # noqa
except ImportError:
    # Py3
    from urllib.parse import unquote  # noqa

from datetime import timedelta

DISCOVERY_MSG = b"DAIKIN_UDP/common/basic_info"

UDP_SRC_PORT = 30000
UDP_DST_PORT = 30050

DISCOVERY_ADDRESS = '<broadcast>'
DISCOVERY_TIMEOUT = timedelta(seconds=5)


class Daikin(object):
    """Base class to discover Daikin devices."""

    def __init__(self):
        """Initialize the Daikin discovery."""
        self.entries = []
        self._lock = threading.RLock()

    def scan(self):
        """Scan the network."""
        with self._lock:
            self.update()

    def all(self):
        """Scan and return all found entries."""
        self.scan()
        return self.entries

    def update(self):
        """Scan network for Daikin devices."""
        entries = []

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.settimeout(DISCOVERY_TIMEOUT.seconds)
        sock.bind(("", UDP_SRC_PORT))

        try:

            sock.sendto(DISCOVERY_MSG, (DISCOVERY_ADDRESS, UDP_DST_PORT))

            while True:
                try:
                    data, (address, _) = sock.recvfrom(1024)

                    entry = dict([e.split('=')
                                  for e in data.decode("UTF-8").split(',')])

                    # expecting product, mac, activation code, version
                    if 'ret' not in entry or entry['ret'] != 'OK':
                        # non-OK return on response
                        continue

                    if 'mac' not in entry:
                        # no mac found for device"
                        continue

                    if 'type' not in entry or entry['type'] != 'aircon':
                        # no mac found for device"
                        continue

                    if 'name' in entry:
                        entry['name'] = unquote(entry['name'])

                    entries.append({
                        'id': entry['id'].encode("UTF-8"),
                        'name': entry['name'].encode("UTF-8"),
                        'ip': address,
                        'mac': entry['mac'].encode("UTF-8"),
                        'ver': entry['ver'].encode("UTF-8"),
                    })

                except socket.timeout:
                    break

        finally:
            sock.close()

        self.entries = entries


def main():
    """Test Daikin discovery."""
    from pprint import pprint
    daikin = Daikin()
    pprint("Scanning for Daikin devices..")
    daikin.update()
    pprint(daikin.entries)

if __name__ == "__main__":
    main()
