"""HF-LPB100 chip based device discovery."""
import socket
from datetime import timedelta

from netdisco.const import ATTR_HOST, ATTR_SERIAL, ATTR_MODEL_NAME

DISCOVERY_MSG = b'HF-A11ASSISTHREAD'

DISCOVERY_ADDRESS = '<broadcast>'
DISCOVERY_PORT = 48899
DISCOVERY_TIMEOUT = timedelta(seconds=2)


class HF_LPB100:
    """Base class to discover HF-LPB100 chip based devices."""

    def __init__(self):
        """Initialize the HF-LPB100 chip based discovery."""
        self.entries = []

    def scan(self):
        """Scan the network."""
        self.update()

    def all(self):
        """Scan and return all found entries."""
        self.scan()
        return self.entries

    def update(self):
        """Scan network for HF-LPB100 chip based devices."""
        entries = []

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as cs:
            cs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            cs.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            cs.settimeout(DISCOVERY_TIMEOUT.seconds)

            received_messages = []

            try:
                # send a local broadcast via udp with a "magic packet"
                cs.sendto(DISCOVERY_MSG, (DISCOVERY_ADDRESS, DISCOVERY_PORT))
                cs.settimeout(DISCOVERY_TIMEOUT.seconds)

                while True:
                    data, address = cs.recvfrom(4096)
                    received_messages.append(data.decode("UTF-8"))

            except socket.timeout:
                if len(received_messages) <= 0:
                    return []

        for message in received_messages:
            try:
                controller = self._parse_discovery_response(message)
                if controller is not None:
                    entries.append(controller)
            except:
                print("Error parsing discovery message: %s" % message)
                return None

        self.entries = entries

    @staticmethod
    def _parse_discovery_response(message: str) -> {}:
        # parse received message
        data = str.split(message, ",")

        # check validity
        if len(data) == 3:
            # extract data
            ip = data[0]
            hw_id = data[1]
            model = data[2]

            return {
                ATTR_HOST: ip,
                ATTR_SERIAL: hw_id,
                ATTR_MODEL_NAME: model
            }


def main():
    """Test HF-LPB100 chip based discovery."""
    from pprint import pprint
    hf_lpb100 = HF_LPB100()
    pprint("Scanning for HF-LPB100 chip based devices..")
    hf_lpb100.update()
    pprint(hf_lpb100.entries)


if __name__ == "__main__":
    main()
