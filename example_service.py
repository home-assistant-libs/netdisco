"""
Example use of DiscoveryService.

Will scan every 10 seconds and print out new found entries.
Will quit after 2 minutes.

"""
from __future__ import print_function

import logging
from datetime import datetime
import time

from netdisco.service import DiscoveryService

logging.basicConfig(level=logging.INFO)

# Scan every 10 seconds
nd = DiscoveryService(10)


def new_service_listener(discoverable, service):
    """ Print out a new service found message. """
    print("{} - Found new service: {} {}".format(
        datetime.now(), discoverable, service))

nd.add_listener(new_service_listener)

nd.start()

time.sleep(120)

nd.stop()
