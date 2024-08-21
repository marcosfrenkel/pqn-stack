# University of Illinois Urbana-Champaign
# Public Quantum Network
#
# NCSA/Illinois Computes
from abc import abstractmethod
from pqnstack.base.network import NetworkElement
from pqnstack.network.packet import Packet
from typing import Dict


class Node(NetworkElement):

    def __init__(self, specs: Dict):
        super().__init__(specs)
        self.drivers = {}

    def idle(self):
        pass

    def exec(self):
        pass

    def stop(self):
        pass

    def measure(self):
        # Ensure the execution context is appropriate and orchestrate
        # the setup
        #
        # Output: list of actual data
        self.call()

        self.filter()

        # Produce a packet
        self.collect()

    @abstractmethod
    def config(self, specs: Dict):
        pass

    @abstractmethod
    def call(self):
        pass

    @abstractmethod
    def filter(self):
        pass

    @abstractmethod
    def collect(self) -> Packet:
        pass

    @abstractmethod
    def hw_init(self, specs: Dict):
        pass

