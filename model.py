class AppState:
    def __init__(self):
        self.xtrace = []
        self.ytrace = []

        self.foot_len = 0
        self.foot_increment = 5
        self.tracemaxlen = 100
        self.x_current = 0
        self.y_current = 0
        self.theta = 0

    def reset_trace(self):
        self.xtrace = []
        self.ytrace = []

    @property
    def foot_len(self):
        return self._foot_len
    
    @foot_len.setter
    def foot_len(self, value):
        self._foot_len = min(100,max(0, value))

    @property
    def x_current(self):
        return self._x_current
    
    @x_current.setter
    def x_current(self, value):
        self._x_current = value
        self.xtrace.append(value)
        if len(self.xtrace) > self.tracemaxlen:
            self.xtrace = self.xtrace[-self.tracemaxlen:]

    @property
    def y_current(self):
        return self._y_current
    
    @y_current.setter
    def y_current(self, value):
        self._y_current = value
        self.ytrace.append(value)
        if len(self.ytrace) > self.tracemaxlen:
            self.ytrace = self.ytrace[-self.tracemaxlen:]