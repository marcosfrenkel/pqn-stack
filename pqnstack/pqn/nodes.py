# University of Illinois Urbana-Champaign
# Public Quantum Network
#
# NCSA/Illinois Computes
from typing import List, Dict
from pqnstack.network.node import Node
from pqnstack.network.packet import Packet


class PQNNode(Node):

    def __init__(self, specs: Dict):
        # Initialize as much as we can from a generic node
        super().__init__(specs)

        # Setup all device drivers
        self.hw_init(specs)

    def call(self) -> List:
        # Call drivers in sequence
        #
        # Activate the wave plate and collect list of measurement, takes time
        # Send command to time tagger
        # Wait period and collect raw data
        # Return wave plate to the starting position (clean up!)
        # Produce a list of measurements with respective bases
        pass

    def filter(self):
        # Calculate error - does the job of estimating matches
        # Computes statistics
        # Pass a new list/object
        pass

    def collect(self) -> Packet:
        # Now, generate a packet we can send to the network
        pass


