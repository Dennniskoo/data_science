class class1():
    def __init__(self):
        import numpy
        self.np = numpy
    def r_nan(self):
        return self.np.nan

c = class1()
print(c.r_nan())
print(c.np.nan)