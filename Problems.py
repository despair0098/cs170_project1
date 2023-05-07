from queue import PriorityQueue
import copy

class Problem:
    def __init__(self, init):
        self.init = init
        self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.node_count = 0

    def goal_test(self, node_state):
        return self.goal_state == node_state
    

    # from: https://realpython.com/python-enumerate/
    def find_blank(self, curr):
        for index, value in enumerate(curr):
            if value == 0:
                return index
            
    def operators(self, input):
        self.node_count += 1
        curr = input.get_board()
        

        
    # from: https://docs.python.org/3/library/copy.html
    def moveUp(self, index, curr):
        up = copy.deepcopy(curr)
        temp = up[index]
        up[index] = up[index-3]
        up[index-3] = temp
        return up
        
    def moveDown(self, index, curr):
        down = copy.deepcopy(curr)
        temp = down[index]
        down[index] = down[index+3]
        down[index+3] = temp
        return down

    def moveLeft(self, index, curr):
        left = copy.deepcopy(curr)
        temp = left[index]
        left[index] = left[index-1]
        left[index-1] = temp
        return left

    def moveRight(self, index, curr):
        right = copy.deepcopy(curr)
        temp = right[index]
        right[index] = right[index+1]
        right[index+1] = temp
        return right

    #def misplaced_tiles(nodes, new_nodes):
        
    def uniformCostSearch(puzzle):
        for x in puzzle:
            x.set_hn(0)
        solveUniform = PriorityQueue()
        solveUniform.put(puzzle)
        while(solveUniform != ""):
            if(find_blank(puzzle) == 0):
                moveLeft()