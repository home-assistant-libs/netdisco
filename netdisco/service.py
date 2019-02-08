"""Provide service that scans the network in intervals."""
import logging
import threading
import time
from collections import defaultdict
from typing import Any, Callable, Dict, List  # noqa: F401

from .discovery import NetworkDiscovery

DEFAULT_INTERVAL = 300  # seconds

_LOGGER = logging.getLogger(__name__)


class DiscoveryService(threading.Thread):
    """Service that will scan the network for devices each `interval` seconds.

    Add listeners to the service to be notified of new services found.
    """

    def __init__(self, interval=DEFAULT_INTERVAL):
        """Initialize the discovery."""
        super(DiscoveryService, self).__init__()

        # Scanning interval
        self.interval = interval

        # Listeners for new services
        self.listeners = []  # type: List[Callable[[str, Any], None]]

        # To track when we have to stop
        self._stop = threading.Event()

        # Tell Python not to wait till this thread exits
        self.daemon = True

        # The discovery object
        self.discovery = None

        # Dict to keep track of found services. We do not want to
        # broadcast the same found service twice.
        self._found = defaultdict(list)  # type: Dict[str, List]

    def add_listener(self, listener):
        """Add a listener for new services."""
        self.listeners.append(listener)

    def stop(self):
        """Stop the service."""
        self._stop.set()

    def run(self):
        """Start the discovery service."""
        self.discovery = NetworkDiscovery()

        while True:
            self._scan()

            seconds_since_scan = 0

            while seconds_since_scan < self.interval:
                if self._stop.is_set():
                    return

                time.sleep(1)
                seconds_since_scan += 1

    def _scan(self):
        """Scan for new devices."""
        _LOGGER.info("Scanning")
        self.discovery.scan()

        for disc in self.discovery.discover():
            for service in self.discovery.get_info(disc):
                self._service_found(disc, service)

        self.discovery.stop()

    def _service_found(self, disc, service):
        """Tell listeners a service was found."""
        if service not in self._found[disc]:
            self._found[disc].append(service)

            for listener in self.listeners:
                try:
                    listener(disc, service)
                except Exception:  # pylint: disable=broad-except
                    _LOGGER.exception(
                        "Error calling listener")
