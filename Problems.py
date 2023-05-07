from queue import PriorityQueue
import copy
from node import Node 

class Problem:
    def __init__(self, init):
        self.init = init
        self.goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.node_count = 0
        self.attempts = set() # storing all of the ways that can be done by moving
        self.attempts.add(tuple(self.init))

    def goal_test(self, node_state):
        return self.goal == node_state
    
    def get_node_count(self):
        return self.node_count
    

    # from: https://realpython.com/python-enumerate/
    def find_blank(self, curr):
        for index, value in enumerate(curr):
            if value == 0:
                return index
            
    def check_attempts(self, board):
        if tuple(board) in self.attempts: # tuple is used here for converting from list and list can't be compared with set
            return False
        else:
            # from https://www.tutorialsteacher.com/python/set-add -> so i had to convert to tuple. 
            self.attempts.add(tuple(board))
            return True
            
    def operators(self, input):
        self.node_count += 1
        curr = input.get_board()
        node_list = list() # this is a list cuz we want ordered, changeable list of the nodes that is possible. 
        zero_index = self.find_blank(curr)

        # Moving up
        if zero_index > 2:
            up_node = Node(self.moveUp(zero_index, curr))
            up_node.set_gn(input.get_gn()+1)
            if self.check_attempts(up_node.get_board()):
                node_list.append(up_node)

        # Moving down
        if zero_index < 6:
            down_node = Node(self.moveDown(zero_index, curr))
            down_node.set_gn(input.get_gn()+1)
            if self.check_attempts(down_node.get_board()):
                node_list.append(down_node)

        # Moving right
        if zero_index % 3 > 0:
            right_node = Node(self.moveRight(zero_index, curr))
            right_node.set_gn(input.get_gn()+1)
            if self.check_attempts(right_node.get_board()):
                node_list.append(right_node)

        # Moving left
        if zero_index % 3 < 2:
            left_node = Node(self.moveLeft(zero_index, curr))
            left_node.set_gn(input.get_gn()+1)
            if self.check_attempts(left_node.get_board()):
                node_list.append(left_node)
        
        return node_list
        
    # from: https://docs.python.org/3/library/copy.html
    def moveUp(self, index, curr):# the index should be the one for zero
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
    
    def get_Init(self):
        return self.init
    
def misplaced_calc(board):
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    misplaced = 0
    for tile in board:
        for goal_tile in goal:
            if tile != goal_tile:
                misplaced += 1
    return misplaced

def misplaced_tiles(nodes, new_nodes):
    frontier = nodes
    for node in new_nodes:
        misplaced = misplaced_calc(node.get_board())
        node.set_hn(misplaced)
        currentGn = node.get_gn()
        node.set_fn(currentGn + misplaced)
        frontier.put(node)
    return frontier


def general_alg(problem):
    nodes = PriorityQueue()
    first = Node(problem.get_Init())
    first.set_fn(0)
    first.set_gn(0)
    first.set_hn(0)
    nodes.put(first)

    maxQueue = nodes.qsize()
    while(1):
        if nodes.empty():
            return "failure"
        node = nodes.get()
        if problem.goal_test(node.get_board()):
            print("Nodes expanded:{0}".format(str(problem.get_node_count())))
            print("Maximum num of nodes:{0}".format(str(maxQueue)))
            return node
        nodes = misplaced_tiles(nodes, problem.operators(node))
        curSize = nodes.qsize()
        if curSize > maxQueue:
            maxQueue = curSize