"""The tests for discovering Yamaha Receivers."""
import unittest
import xml.etree.ElementTree as ElementTree

from netdisco.discoverables.yamaha import Discoverable
from netdisco.util import etree_to_dict

LOCATION = 'http://192.168.XXX.XXX:80/desc.xml'


class MockUPNPEntry(object):
    """UPNPEntry backed by a description file."""

    location = LOCATION

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
            Discoverable(None).info_from_entry(
                MockUPNPEntry("desc_RX-V481.xml")),
            {
                'control_url':
                'http://192.168.XXX.XXX:80/YamahaRemoteControl/ctrl',
                'description_url':
                'http://192.168.XXX.XXX:80/YamahaRemoteControl/desc.xml',
                'host': '192.168.xxx.xxx',
                'model_name': 'RX-V481',
                'model_number': 'V481',
                'manufacturer': 'Yamaha Corporation',
                'name': 'RX-V481 XXXXXX',
                'port': 80,
                'serial': 'XXXXXXXX',
                'ssdp_description': 'http://192.168.XXX.XXX:80/desc.xml',
                'udn': 'uuid:XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
            })

    def test_info_from_entry_single_service(self):
        self.assertEqual(
            Discoverable(None).info_from_entry(
                MockUPNPEntry("desc_single_service.xml")),
            {
                'control_url':
                'http://192.168.1.2:80/YamahaRemoteControl/single_ctrl',
                'description_url':
                'http://192.168.1.2:80/YamahaRemoteControl/single_desc.xml',
                'host': '192.168.xxx.xxx',
                'model_name': 'single service model name',
                'model_number': None,
                'manufacturer': None,
                'name': 'single service friendly name',
                'port': 80,
                'serial': None,
                'ssdp_description': 'http://192.168.XXX.XXX:80/desc.xml',
                'udn': None
            })

    def test_info_from_entry_multiple_services_remote_control_last(self):
        self.assertEqual(
            Discoverable(None).info_from_entry(MockUPNPEntry(
                "desc_multiple_services_remote_control_last.xml")),
            {
                'control_url':
                'http://192.168.1.2:80/YamahaRemoteControl/multi_ctrl',
                'description_url':
                'http://192.168.1.2:80/YamahaRemoteControl/multi_desc.xml',
                'host': '192.168.xxx.xxx',
                'model_name': 'multi service model name',
                'model_number': None,
                'manufacturer': None,
                'name': 'multi service friendly name',
                'port': 80,
                'serial': None,
                'ssdp_description': 'http://192.168.XXX.XXX:80/desc.xml',
                'udn': None
            })

    def test_info_from_entry_multiple_services_no_remote_control(self):
        self.assertEqual(
            Discoverable(None).info_from_entry(MockUPNPEntry(
                "desc_multiple_services_no_remote_control.xml")),
            {
                'control_url':
                'http://192.168.1.2:80/YamahaNewControl/ctrl',
                'description_url':
                'http://192.168.1.2:80/YamahaNewControl/desc.xml',
                'host': '192.168.xxx.xxx',
                'model_name': 'multi service model name',
                'model_number': None,
                'manufacturer': None,
                'name': 'multi service friendly name',
                'port': 80,
                'serial': None,
                'ssdp_description': 'http://192.168.XXX.XXX:80/desc.xml',
                'udn': None
            })
