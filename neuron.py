class Neuron:
    def __init__(self, weigth, bias):
        self.weigth = weigth
        self.bias = bias

    def compute_with_bias(self, x):
        res = 0
        for i in x:
            res = res + (i * self.weigth)
        return 1 if res + self.bias > 0 else 0

    def calc_with_threshold(self, x):
        res = 0
        for i in x:
            res = res + (i * self.weigth)
        return 1 if res > 1 else 0