
from scipy.interpolate import UnivariateSpline

class Smart_Dict():

    values = {} # (int x, int y)

    top_bound = (0,0) #(max x, bound y)
    bot_bound = (0,0) #(min x, bound y)

    def __init__(self):
        pass

    def get(self, x):
        try:
            out = self.values[x]
            return out
        except KeyError:
            out = self.interpolate(x)
            return out

    def interpolate(self, x):
        if(x < self.bot_bound[0]):
            return self.bot_bound[1]
        elif x > self.top_bound[0]:
            return self.top_bound[1]
        spl = UnivariateSpline(self.values.keys(), self.values.values())
        spl.set_smoothing_factor(0.5)
        return spl(x)
