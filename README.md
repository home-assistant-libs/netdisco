# NetDisco

NetDisco is a Python library to discover local devices and services. It uses mDNS and uPnP to scan the network and supports Python 2 and 3.

It is the library that powers the device discovery within [Home Assistant](https://home-assistant.io/).

## Installation

```bash
git clone https://github.com/balloob/netdisco
pip install -r requirements.txt
```

*Use pip3 instead of pip if you're using Python 3.*

## Example

```python
import time
import netdisco

netdis = netdisco.NetworkDiscovery()

# Give some time for zeroconf to communicate
time.sleep(3)

for dev in netdis.discover():
    print(dev, netdis.get_info(dev))

netdis.stop()
```

Will result in a list of discovered devices and their most important information:

```
DLNA ['http://192.168.1.1:8200/rootDesc.xml', 'http://192.168.1.150:32469/DeviceDescription.xml']
google_cast [('Living Room.local.', 8009)]
philips_hue ['http://192.168.1.2:80/description.xml']
belkin_wemo ['http://192.168.1.10:49153/setup.xml']
```
