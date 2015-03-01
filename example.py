from __future__ import print_function
import sys

from netdisco.discovery import NetworkDiscovery

nd = NetworkDiscovery()

nd.scan()

# Pass in command line argument dump to get the raw data
if sys.argv[-1] == 'dump':
    nd.print_raw_data()

else:
    for dev in nd.discover():
        print(dev, nd.get_info(dev))

nd.stop()
