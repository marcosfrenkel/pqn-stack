# University of Illinois Urbana-Champaign
# Public Quantum Network
#
# NCSA/Illinois Computes
from abc import abstractmethod
from pqnstack.base.network import NetworkElement
from pqnstack.base.driver import DeviceClass
from pqnstack.network.packet import Packet
from typing import Dict


class Node(NetworkElement):

    def __init__(self, specs: Dict):
        super().__init__()

        self.drivers = {

        }

        self.hw_init()

    def idle(self):
        pass

    def exec(self):
        pass

    def stop(self):
        pass

    def measure(self):
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

