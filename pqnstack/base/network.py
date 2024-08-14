# University of Illinois Urbana-Champaign
# Public Quantum Network
#
# NCSA/Illinois Computes
#
#
import queue
from abc import ABC, abstractmethod


class NetworkElement(ABC):

    def __init__(self):
        # TODO: consider async message while processing
        self.request_queue = queue.Queue()

    @abstractmethod
    def idle(self):
        pass

    @abstractmethod
    def exec(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def dispatch(self):
        pass