from queue import PriorityQueue

class Problem:
    def __init__(self, init):
        self.init = init
        self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        #self.node_count = 0

    def goal_test(self, node_state):
        return self.goal_state == node_state
    

    # from: https://realpython.com/python-enumerate/
    def find_blank(self, curr):
        for index, value in enumerate(curr):
            if value == 0:
                return index
            
    #def operators(self, input):
        

    def moveUp(self, index, curr):
        
    def moveDown(self, index, curr):

    def moveLeft(self, index, curr):

    def moveRight(self, index, curr):    
        
    
