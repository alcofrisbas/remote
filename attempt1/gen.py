class step:
    def __init__(self,half=False):
        self.steps = (0b1000,
             0b1100,
             0b0100,
             0b0110,
             0b0010,
             0b0011,
             0b0001,
             0b1001)
        if half:
            self.step = self.steps[::2]
        self.n = 0
        self.l = len(self.steps)
        self._direction = 1
    def direction(self, reverse):
        if reverse:
            self._direction = -1
        else:
            self._direction = 1
    def forward(self):
        self._direction = 1
    def backward(self):
        self._direction = -1
    
    def __iter__(self):
        return self

    def __next__(self):
        out = self.steps[self.n]
        self.n = (self.n + _self.direction) % self.l
        return out

