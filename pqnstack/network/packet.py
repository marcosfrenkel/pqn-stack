# University of Illinois Urbana-Champaign
# Public Quantum Network
#
# NCSA/Illinois Computes
#
#
from dataclasses import dataclass


@dataclass
class Packet:
    intent: str
    request: str
    source: int
    destination: int
    payload: object

    def signature(self):
        return self.intent, self.request
