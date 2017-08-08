"""tplink device discovery."""
import json
import socket
import struct


DISCOVERY_PORT = 9999
DISCOVERY_TIMEOUT = 3
INITIALIZATION_VECTOR = 171


class Tplink(object):
    """Base class to discover tplink devices."""

    def __init__(self, device_type=None):
        """Initialize the tplink discovery."""
        self.device_type = device_type
        self.entries = []

    def scan(self):
        """Scan the network."""
        self.discover(DISCOVERY_PORT, DISCOVERY_TIMEOUT)

    def discover(self, port=9999, timeout=3):
        """Sends discovery message to 255.255.255.255:9999 in order."""

        discovery_query = {"system": {"get_sysinfo": None},
                           "emeter": {"get_realtime": None}}

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(timeout)

        req = json.dumps(discovery_query)

        encrypted_req = self.encrypt(req)
        sock.sendto(encrypted_req[4:], ("255.255.255.255", port))

        try:
            while True:
                data, addr = sock.recvfrom(4096)
                ip_address, port = addr
                info = json.loads(self.decrypt(data))
                if "system" in info and "get_sysinfo" in info["system"]:
                    sysinfo = info["system"]["get_sysinfo"]
                    if "type" in sysinfo:
                        dtype = sysinfo["type"]
                    elif "mic_type" in sysinfo:
                        dtype = sysinfo["mic_type"]
                    else:
                        dtype = "UNKNOWN"
                if self.device_type is None or self.device_type in \
                        dtype.lower():
                    entry = {"host": ip_address, "name": sysinfo["alias"]}
                    self.entries.append(entry)
        except socket.timeout:
            pass
        except Exception as ex:
            raise ex

    @staticmethod
    def encrypt(request):
        """
        Encrypt a request for a TP-Link Smart Home Device.

        :param request: plaintext request data
        :return: ciphertext request
        """
        key = INITIALIZATION_VECTOR
        buffer = bytearray(struct.pack(">I", len(request)))

        for char in request:
            cipher = key ^ ord(char)
            key = cipher
            buffer.append(cipher)

        return buffer

    @staticmethod
    def decrypt(ciphertext):
        """
        Decrypt a response of a TP-Link Smart Home Device.

        :param ciphertext: encrypted response data
        :return: plaintext response
        """
        key = INITIALIZATION_VECTOR
        buffer = []

        ciphertext = ciphertext.decode('latin-1')

        for char in ciphertext:
            plain = key ^ ord(char)
            key = ord(char)
            buffer.append(chr(plain))

        plaintext = ''.join(buffer)

        return plaintext


def main():
    """Test tplink discovery."""
    from pprint import pprint
    tplink_light = Tplink("smartbulb")
    pprint("Scanning for tplink lights..")
    tplink_light.scan()
    pprint(tplink_light.entries)
    tplink_switch = Tplink("smartplug")
    pprint("Scanning for tplink plugs..")
    tplink_switch.scan()
    pprint(tplink_switch.entries)
    tplink_all = Tplink()
    pprint("Scanning for all tplink devices..")
    tplink_all.scan()
    pprint(tplink_all.entries)


if __name__ == "__main__":
    main()
