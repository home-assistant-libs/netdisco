from __future__ import print_function
import time

import netdisco

nd = netdisco.NetworkDiscovery()

# Give some time for zeroconf to communicate
time.sleep(3)

for dev in nd.discover():
    print(dev, nd.get_info(dev))

nd.stop()
