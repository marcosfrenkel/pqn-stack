# University of Illinois Urbana-Champaign
# Public Quantum Network
#
# NCSA/Illinois Computes
#
#
from dataclasses import dataclass
from enum import Enum


@dataclass
class Packet:
    intent: str
    request: str
    source: int
    destination: int
    payload: object

    def signature(self):
        return self.intent, self.request

    def routing(self):
        return self.source, self.destination


class PacketIntent(Enum):
    DATA = 1
    CONTROL = 2
    ROUTING = 3


class PacketRequest(Enum):
    MEASUREMENT = 1
