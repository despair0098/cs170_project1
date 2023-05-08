class Node:
    def __init__(self, board):
        self.board = board

    def get_board(self):
        return self.board

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
    
    # this function needs to be typed because of this error: https://www.appsloveworld.com/coding/python3x/283/typeerror-not-supported-between-instances-of-node-and-node
    def __lt__(self, other):
        return self.fn < other.fn


    