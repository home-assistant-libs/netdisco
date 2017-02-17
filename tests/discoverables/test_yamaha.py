"""The tests for discovering Yamaha Receivers."""
import unittest
import xml.etree.ElementTree as ElementTree

from netdisco.discoverables.yamaha import Discoverable
from netdisco.util import etree_to_dict


class MockUPNPEntry(object):
    """UPNPEntry backed by a description file."""

    def __init__(self, name):
        """Read and parse a MockUPNPEntry from a file."""
        with open('tests/discoverables/yamaha_files/%s' % name,
                  encoding='utf-8') as content:
            self.description = etree_to_dict(
                ElementTree.fromstring(content.read())).get('root', {})

class TestYamaha(unittest.TestCase):
    """Test the Yamaha Discoverable."""

    def test_info_from_entry_rx_v481(self):
        self.assertEqual(
            ("RX-V481 XXXXXX", "RX-V481",
             "http://192.168.XXX.XXX:80/YamahaRemoteControl/ctrl",
             "http://192.168.XXX.XXX:80/YamahaRemoteControl/desc.xml"),
            Discoverable(None).info_from_entry(
                MockUPNPEntry("desc_RX-V481.xml")))

    def test_info_from_entry_single_service(self):
        self.assertEqual(
            ("single service friendly name", "single service model name",
             "http://192.168.1.2:80/YamahaRemoteControl/single_ctrl",
             "http://192.168.1.2:80/YamahaRemoteControl/single_desc.xml"),
            Discoverable(None).info_from_entry(
                MockUPNPEntry("desc_single_service.xml")))

    def test_info_from_entry_multiple_services_remote_control_last(self):
        self.assertEqual(
            ("multi service friendly name", "multi service model name",
             "http://192.168.1.2:80/YamahaRemoteControl/multi_ctrl",
             "http://192.168.1.2:80/YamahaRemoteControl/multi_desc.xml"),
            Discoverable(None).info_from_entry(MockUPNPEntry(
                "desc_multiple_services_remote_control_last.xml")))

    def test_info_from_entry_multiple_services_no_remote_control(self):
        self.assertEqual(
            ("multi service friendly name", "multi service model name",
             "http://192.168.1.2:80/YamahaNewControl/ctrl",
             "http://192.168.1.2:80/YamahaNewControl/desc.xml"),
            Discoverable(None).info_from_entry(MockUPNPEntry(
                "desc_multiple_services_no_remote_control.xml")))
