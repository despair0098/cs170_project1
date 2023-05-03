class Node:
    def __init__(self, board):
        self.board = board

    def get_state(self):
        return self.state

    def set_gn(self, gn):
        self.gn = gn
    
    def get_gn(self):
        return self.gn

    def set_hn(self, hn):
        self.hn = hn

    def get_hn(self):
        return self.hn
    
    def set_fn(self, fn):
        self.fn = fn

    def get_fn(self):
        return self.fn

    