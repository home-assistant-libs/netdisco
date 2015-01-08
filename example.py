from __future__ import print_function

import netdisco

nd = netdisco.NetworkDiscovery()

nd.scan()

for dev in nd.discover():
    print(dev, nd.get_info(dev))

nd.stop()
