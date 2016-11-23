"""
Support for discovery Samsung Smart Air Conditioner.

"""
import threading
import socket
import binascii

DISCOVERY_ADDRESS = '<broadcast>'
DISCOVERY_PORT = 1900
DISCOVERY_TIMEOUT = 5

DISCOVERY_MSG = """NOTIFY * HTTP/1.1
HOST: 239.255.255.250:1900
CACHE-CONTROL: max-age=20
SERVER: AIR CONDITIONER
SPEC_VER: MSpec-1.00
SERVICE_NAME: ControlServer-MLib
MESSAGE_TYPE: CONTROLLER_START

""".encode('utf-8')


class SamsungAC(object):
    """Base class to discover Samsung Smart AC devices."""

    def __init__(self):
        self.entries = []
        self.last_scan = None
        self._lock = threading.RLock()

    def scan(self):
        """Scan the network."""
        with self._lock:
            self.update()

    def all(self):
        """Return all found entries.

        Will scan for entries if not scanned recently.
        """
        self.scan()
        return list(self.entries)

    def update(self):
        """Scan for new Samsung Smart AC devices.

        Example of the dict list returned by this function:
        [{'data': {
            'CACHE_CONTROL': 'max-age=60',
            'FIRMCODE': '01538A140403',
            'GROUP_ADDRESS': 'BC8CCDEE1A32FFFF',
            'HOST': '255.255.255.255:1900',
            'LOCATION': 'http://192.168.1.101',
            'MAC_ADDR': 'BC8CCDEE1A32',
            'MESSAGE_TYPE': 'DEVICEDESCRIPTION',
            'MODELCODE': 'SAMSUNG_DEVICE',
            'NICKNAME': '44454D4F',
            'NODE_ADDRESS': 'BC8CCDEE1A320000',
            'NTS': 'ssdp:alive',
            'ROOT_ADDRESS': 'BC8CCDEE1A320000',
            'SERVER': 'SSDP,SAMSUNG-AC-RAC_2013',
            'SERVICE_NAME': 'ControlServer-MLib',
            'SPEC_VER': 'MSpec-2.00'},
        'from': ('192.168.1.101', 46247)}]
        """

        self.entries = []
        servers = []
        # setup socket for broadcast
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.settimeout(DISCOVERY_TIMEOUT)
        sock.bind(('', DISCOVERY_PORT))

        try:
            # Broadcast message
            sock.sendto(DISCOVERY_MSG, (DISCOVERY_ADDRESS, DISCOVERY_PORT))

            # Look for responses from all recipients
            while True:
                try:
                    data, server = sock.recvfrom(1024)
                    data = data.decode('utf-8')
                    if 'LOCATION:' in data:
                        data = {k: v.strip() for (k, v) in (
                            line.split(':', 1) for line in
                            data.splitlines() if ':' in line)}
                        if 'NICKNAME' in data:
                            unhex = binascii.unhexlify(data['NICKNAME'])
                            data['NICKNAME'] = unhex.decode('utf-8')
                        if server not in servers:
                            servers.append(server)
                            self.entries.append({'data': data, 'from': server})
                except socket.timeout:
                    break
        finally:
            sock.close()


def main():
    """Test Samsung Smart AC discovery."""
    from pprint import pprint

    samsungac = SamsungAC()

    pprint("Scanning Samsung Smart AC...")
    samsungac.update()
    pprint(samsungac.entries)


if __name__ == "__main__":
    main()
