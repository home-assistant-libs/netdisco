"""
Orvibo switch discovery.
"""
import threading

from orvibo.s20 import discover


class Orvibo(object):
    """Base class to discover Orvibo switches."""

    def __init__(self):
        self.entries = {}
        self.last_scan = None
        self._lock = threading.RLock()

    def scan(self):
        """Scan the network."""
        with self._lock:
            self.update()

    def all(self):
        """Scan and return all found entries."""
        self.scan()
        return list(self.entries)

    def update(self):
        """Scan network for Orvibo switches."""
        self.entries = discover()


def main():
    """Test Orvibo switch discovery."""
    from pprint import pprint

    # pylint: disable=invalid-name
    orvibo_discover = Orvibo()

    pprint("Scanning for Orvibo switches ...")
    orvibo_discover.update()
    pprint(orvibo_discover.entries)

if __name__ == "__main__":
    main()
