# University of Illinois Urbana-Champaign
# Public Quantum Network
#
# NCSA/Illinois Computes

from pqnstack.base.driver import DeviceDriver


class TimeTagger(DeviceDriver):

    def __init__(self):
        super.__init__()
        self.setup()

    def setup(self):
        pass

    def exec(self):
        pass

    def command(self):
        pass

    def info(self, attr: str):
        pass


