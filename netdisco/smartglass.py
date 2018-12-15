"""Xbox One SmartGlass device discovery."""
import socket
import struct
import binascii
from datetime import timedelta
from typing import Any, Dict, List, Optional, Tuple  # noqa: F401


DISCOVERY_PORT = 5050
DISCOVERY_ADDRESS_BCAST = '<broadcast>'
DISCOVERY_ADDRESS_MCAST = '239.255.255.250'
DISCOVERY_REQUEST = 0xDD00
DISCOVERY_RESPONSE = 0xDD01
DISCOVERY_TIMEOUT = timedelta(seconds=2)

"""
SmartGlass Client type
XboxOne = 1
Xbox360 = 2
WindowsDesktop = 3
WindowsStore = 4
WindowsPhone = 5
iPhone = 6
iPad = 7
Android = 8
"""
DISCOVERY_CLIENT_TYPE = 4

_Response = Dict[str, Any]


class XboxSmartGlass:
    """Base class to discover Xbox SmartGlass devices."""

    def __init__(self):
        """Initialize the Xbox SmartGlass discovery."""
        self.entries = []  # type: List[Tuple[str, Optional[_Response]]]
        self._discovery_payload = self.discovery_packet()

    @staticmethod
    def discovery_packet():
        """Assemble discovery payload."""
        version = 0
        flags = 0
        min_version = 0
        max_version = 2

        payload = struct.pack(
            '>IHHH',
            flags, DISCOVERY_CLIENT_TYPE, min_version, max_version
        )
        header = struct.pack(
            '>HHH',
            DISCOVERY_REQUEST, len(payload), version
        )
        return header + payload

    @staticmethod
    def parse_discovery_response(data):
        """Parse console's discovery response."""
        pos = 0
        # Header
        # pkt_type, payload_len, version = struct.unpack_from(
        #    '>HHH',
        #    data, pos
        # )
        pos += 6
        # Payload
        flags, type_, name_len = struct.unpack_from(
            '>IHH',
            data, pos
        )
        pos += 8
        name = data[pos:pos + name_len]
        pos += name_len + 1  # including null terminator
        uuid_len = struct.unpack_from(
            '>H',
            data, pos
        )[0]
        pos += 2
        uuid = data[pos:pos + uuid_len]
        pos += uuid_len + 1  # including null terminator
        last_error, cert_len = struct.unpack_from(
            '>IH',
            data, pos
        )
        pos += 6
        cert = data[pos:pos + cert_len]

        return {
            'device_type': type_,
            'flags': flags,
            'name': name.decode('utf-8'),
            'uuid': uuid.decode('utf-8'),
            'last_error': last_error,
            'certificate': binascii.hexlify(cert).decode('utf-8')
        }

    def scan(self):
        """Scan the network."""
        self.update()

    def all(self):
        """Scan and return all found entries."""
        self.scan()
        return self.entries

    @staticmethod
    def verify_packet(data):
        """Parse packet if it has correct magic"""
        if len(data) < 2:
            return None

        pkt_type = struct.unpack_from('>H', data)[0]
        if pkt_type != DISCOVERY_RESPONSE:
            return None

        return XboxSmartGlass.parse_discovery_response(data)

    def update(self):
        """Scan network for Xbox SmartGlass devices."""
        entries = []

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(DISCOVERY_TIMEOUT.seconds)
        sock.sendto(self._discovery_payload,
                    (DISCOVERY_ADDRESS_BCAST, DISCOVERY_PORT))
        sock.sendto(self._discovery_payload,
                    (DISCOVERY_ADDRESS_MCAST, DISCOVERY_PORT))

        while True:
            try:
                data, (address, _) = sock.recvfrom(1024)

                response = self.verify_packet(data)
                if response:
                    entries.append((address, response))

            except socket.timeout:
                break

            self.entries = entries

        sock.close()


def main():
    """Test XboxOne discovery."""
    from pprint import pprint
    xbsmartglass = XboxSmartGlass()
    pprint("Scanning for Xbox One SmartGlass consoles devices..")
    xbsmartglass.update()
    pprint(xbsmartglass.entries)


if __name__ == "__main__":
    main()
