# University of Illinois Urbana-Champaign
# Public Quantum Network
#
# NCSA/Illinois Computes

from abc import ABC, abstractmethod
from typing import Dict
from enum import Enum


class DeviceDriver(ABC):

    def __init__(self, specs: Dict):
        self.name = specs['name']
        self.desc = specs['desc']
        self.dtype = DeviceClass[specs['dtype']]
        self.setup(specs)

    @abstractmethod
    def setup(self, specs: Dict):
        pass

    @abstractmethod
    def exec(self, seq: str):
        pass

    @abstractmethod
    def command(self, cmd: str):
        pass

    @abstractmethod
    def info(self, attr: str):
        pass


class DeviceClass(Enum):
    SENSOR = 1
    MOTOR = 2
    TEMPCTRL = 3
    TIMETAGR = 4
