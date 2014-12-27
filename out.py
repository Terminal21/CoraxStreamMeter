from Adafruit_MCP4725.Adafruit_MCP4725 import MCP4725


class VOut:

    def __init__(self, max=1000, limit=4096):
        self.max = max
        self.limit = limit
        self.out = MCP4725()

    def set(self, val):
        if val > self.max:
            val = self.max
        v = float(val)/float(self.max) * self.limit
        self.out.setVoltage(int(v))
