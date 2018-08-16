import unittest
from binascii import unhexlify

from netdisco.xboxone import XboxOneSmartGlass


class TestXboxOne(unittest.TestCase):
    """Test the Xbox One Discoverable."""
    def test_assemble_request(self):
        packet = XboxOneSmartGlass.discovery_packet()

        self.assertEqual(
            packet,
            unhexlify(b'dd00000a000000000000000400000002')
        )

    def test_parse_request(self):
        with open('tests/xboxone_files/discovery_response', 'rb') as content:
            packet = content.read()

        response = XboxOneSmartGlass.parse_discovery_response(packet)
        self.assertEqual(response['device_type'], 1)
        self.assertEqual(response['flags'], 2)
        self.assertEqual(response['name'], 'XboxOne')
        self.assertEqual(response['uuid'], 'DE305D54-75B4-431B-ADB2-EB6B9E546014')
        self.assertEqual(response['last_error'], 0)
        self.assertEqual(response['certificate'][:8], '30820203')
        self.assertEqual(len(unhexlify(response['certificate'])), 519)
