"""The tests for discovering Twinkly devices via XLED protocol."""
import unittest

from netdisco.xled import XLED


class TestTwinkly(unittest.TestCase):
    """Test the Twinkly Discoverable."""

    def setUp(self):
        """
        Setup test class
        """
        self.discovery_response = b'\x01\x04\xa8\xc0OKTwinkly_33AAFF\x00'

    def test_verify_response(self):
        """
        Test discovery response verification
        """
        valid_parse = XLED.verify_packet(self.discovery_response)
        invalid_length = XLED.verify_packet(b'\x01\x04\xa8\xc0T\x00')
        invalid_magic = XLED.verify_packet(
            b'\x01\x04\xa8\xc0KOTwinkly_33AAFF\x00'
        )

        self.assertIsNotNone(valid_parse)
        self.assertIsNone(invalid_length)
        self.assertIsNone(invalid_magic)

    def test_parse_response(self):
        """
        Test discovery response parsing
        """
        response = XLED.parse_discovery_response(self.discovery_response)

        self.assertEqual(response['name'], 'Twinkly_33AAFF')
