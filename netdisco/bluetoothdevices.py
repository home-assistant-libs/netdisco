"""Add support for discovering Bluetooth devices."""
import threading
import bluefang


class Bluetooth(object):
    """Add support for discovering Bluetooth devices."""

    def __init__(self):
        """Initialize discovery."""
        self.entries = []
        self._lock = threading.RLock()

    def scan(self):
        """Scan network for Bluetooth devices."""
        with self._lock:
            self.update()

    def all(self):
        """Scan and return all found entries."""
        self.scan()
        return self.entries

    def update(self):
        """Scan network for Bluetooth devices."""
        bluetooth = bluefang.Bluefang()
        self.entries = bluetooth.scan(timeout_in_ms=10000)
