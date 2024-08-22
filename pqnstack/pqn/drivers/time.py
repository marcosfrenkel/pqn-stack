# University of Illinois Urbana-Champaign
# Public Quantum Network
#
# NCSA/Illinois Computes
from pqnstack.base.driver import DeviceDriver, DeviceStatus
from pqnstack.base.errors import (
    DriverFunctionNotImplemented,
    DriverFunctionUnknown
)
from typing import Dict
import zmq
import time
import math


class IDQTimeTagger(DeviceDriver):

    def __init__(self, specs: Dict):
        # Data structures unique to this class
        self.tc = None
        self.tc_ip = None
        self.tc_port = None

        # Init parent class
        super.__init__(specs)

    def setup(self, specs: Dict):
        # Connect to the time tagger
        context = zmq.Context()
        self.tc = context.socket(zmq.REQ)
        self.tc.connect(f"tcp://{self.tc_ip}:{self.tc_port}")

        # Map executable functions to their internal implementation
        self.executable['set_delay'] = self.__set_delay
        self.executable['single_counts'] = self.__single_counts
        self.executable['coincidence_counts'] = self.__coincidence_counts

        # Check all implementations were provided
        if set(self.provides).symmetric_difference(self.executable.keys()) != set():
            raise DriverFunctionNotImplemented('IDQTimeTagger')

        # Set device as on
        self.status = DeviceStatus.ON

    def exec(self, seq: str, **kwargs):
        if str not in self.executable.keys():
            raise DriverFunctionUnknown('IDQTimeTagger')

        self.executable[seq](**kwargs)

    def __hw_command(self, cmd: str):
        self.tc.send_string(cmd)
        return self.tc.recv().decode("utf-8")

    # Hardware level implementation of executable functions
    # =====================================================
    def __set_delay(self, **kwargs):
        command = f"INPU{kwargs['channel']}:DELAY {kwargs['delay']}"
        self.__hw_command(command)

    def __single_counts(self, **kwargs):
        command = f"INPU{kwargs['channel']}:COUN?"
        return int(self.__hw_command(command))

    def __coincidence_counts(self, **kwargs):
        command = (f"TSCO6:LINK {kwargs['channel1']}; TSCO6:LINK {kwargs['channel2']}; TSCO6:COUN:INTE "
                   f"{kwargs['interval']}")
        self.__hw_command(command)
        command = "TSCO6:COUN?"
        return int(self.__hw_command(command))
