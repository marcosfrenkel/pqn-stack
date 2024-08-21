# University of Illinois Urbana-Champaign
# Public Quantum Network
#
# NCSA/Illinois Computes


class DriverNotFound(Exception):
    def __init__(self, driver, message="Device driver configuration not found"):
        self.driver = driver
        self.message = message
        super().__init__(self.message)
