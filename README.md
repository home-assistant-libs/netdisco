# NetDisco

NetDisco is a Python 3 library to discover local devices and services. It allows to scan on demand or offer a service that will scan the network in the background in a set interval.

Current methods of scanning:

 - mDNS (includes Chromecast, Homekit)
 - uPnP
 - Plex Media Server using Good Day Mate protocol
 - Logitech Media Server discovery protocol
 - Daikin discovery protocol
 - Web OS discovery protocol

It is the library that powers the device discovery within [Home Assistant](https://home-assistant.io/).

## Installation

Netdisco is available on PyPi. Install using `pip3 install netdisco`.

## Example

From command-line:

```bash
python3 -m netdisco
# To see all raw data:
python3 -m netdisco dump
```

In your script:

```python
from netdisco.discovery import NetworkDiscovery

netdis = NetworkDiscovery()

netdis.scan()

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
