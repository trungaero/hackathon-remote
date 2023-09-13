class AppState:
    def __init__(self):
        self.foot_len = 0
        self.foot_increment = 5

    @property
    def foot_len(self):
        return self._foot_len
    
    @foot_len.setter
    def foot_len(self, value):
        self._foot_len = min(100,max(0, value))