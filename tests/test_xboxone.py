"""The tests for discovering Xbox gaming consoles via SmartGlass protocol."""
import unittest
from binascii import unhexlify

from netdisco.smartglass import XboxSmartGlass


class TestXboxOne(unittest.TestCase):
    """Test the Xbox One Discoverable."""
    def setUp(self):
        """
        Setup test class
        """
        with open('tests/xboxone_files/discovery_response', 'rb') as content:
            packet = content.read()

        if not packet:
            raise Exception('Failed to read test data')

        self.discovery_response = packet

    def test_assemble_request(self):
        """
        Test discovery request assembly
        """
        packet = XboxSmartGlass.discovery_packet()

        self.assertEqual(
            packet,
            unhexlify(b'dd00000a000000000000000400000002')
        )

    def test_parse_response(self):
        """
        Test discovery response parsing
        """
        response = XboxSmartGlass.parse_discovery_response(
            self.discovery_response)

        self.assertEqual(response['device_type'], 1)
        self.assertEqual(response['flags'], 2)
        self.assertEqual(response['name'], 'XboxOne')
        self.assertEqual(response['uuid'],
                         'DE305D54-75B4-431B-ADB2-EB6B9E546014')
        self.assertEqual(response['last_error'], 0)
        self.assertEqual(response['certificate'][:8], '30820203')
        self.assertEqual(len(unhexlify(response['certificate'])), 519)

    def test_verify_response(self):
        """
        Test discovery response verification
        """
        valid_parse = XboxSmartGlass.verify_packet(self.discovery_response)
        invalid_length = XboxSmartGlass.verify_packet(unhexlify(b'41'))
        invalid_magic = XboxSmartGlass.verify_packet(
            unhexlify(b'aabbccddeeff00'))

        self.assertIsNotNone(valid_parse)
        self.assertIsNone(invalid_length)
        self.assertIsNone(invalid_magic)
