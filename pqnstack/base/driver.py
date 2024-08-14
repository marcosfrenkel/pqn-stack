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
        self.setup()

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def exec(self):
        pass

    @abstractmethod
    def command(self):
        pass

    @abstractmethod
    def info(self):
        pass


class DeviceClass(Enum):
    SENSOR = 1
    MOTOR = 2
    TEMPCTRL = 3
    TIMESTMP = 4