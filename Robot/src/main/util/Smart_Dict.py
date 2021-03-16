
from scipy.interpolate import UnivariateSpline

class Smart_Dict():

    values = {1:3, 2:4, 6:5, 7:9} # (int x, int y)

    top_bound = (10,10) #(max x, bound y)
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
        spl = UnivariateSpline(list(self.values.keys()), list(self.values.values()))
        spl.set_smoothing_factor(0.5)
        return spl(x)

