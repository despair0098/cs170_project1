from queue import PriorityQueue
from node import *
import copy
from node import Node 
from math import sqrt, floor

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
            
    def find_any_number(self, curr, number):
        for index, value in enumerate(curr):
            if value == number:
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
        if zero_index % 3 < 2:
            right_node = Node(self.moveRight(zero_index, curr))
            right_node.set_gn(input.get_gn()+1)
            if self.check_attempts(right_node.get_board()):
                node_list.append(right_node)

        # Moving left
        if zero_index % 3 > 0:
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
    
# From: https://www.geeksforgeeks.org/python-iterate-multiple-lists-simultaneously/
def misplaced_calc(board):
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    misplaced = 0
    for tile, goal_tile in zip(board, goal): #Iterate through both current board and goal board simultaneously and compare
        if (tile != goal_tile and tile != 0):
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

def euclidean_calc(board):
    dist = 0
    goal2d = [[1,2,3],[4,5,6],[7,8,0]]                                  # Turn both goal and board into 2d so that we can use rows and colums
    board2d = [board[:3],board[3:6],board[6:9]]
    for i in range(0, 3):                                               
        for j in range(0, 3):
            if (board2d[i][j] != goal2d[i][j] and board2d[i][j] != 0):  # If current tile on board and goal are different, search for where tile should be
                for a in range(0,3):
                    for b in range(0,3):
                        if (board2d[i][j] == goal2d[a][b]):             # If current tile found on board, calculate Euclidean distance
                            dist += sqrt((i - a)**2 + (j - b)**2)
    return dist

def euclidean(nodes, new_nodes):
    frontier = nodes
    for node in new_nodes:
        euc = euclidean_calc(node.get_board())
        node.set_hn(euc)
        currentGn = node.get_gn()
        node.set_fn(currentGn + euc)
        frontier.put(node)
    return frontier

def uniform(nodes, new_nodes):
    frontier = nodes
    for node in new_nodes:
        node.set_hn(0)
        node.set_fn(node.get_gn())
        frontier.put(node)
    return frontier

def printNode(curr):
    print(curr[0:3])
    print(curr[3:6])
    print(curr[6:9])

def general_alg(problem, algorithm):
    nodes = PriorityQueue()
    first = Node(problem.get_Init())
    first.set_fn(0.00)
    first.set_gn(0.00)
    first.set_hn(0.00)
    nodes.put(first)
    print("Expanding state")
    print(problem.get_Init()[0:3])
    print(problem.get_Init()[3:6])
    print(problem.get_Init()[6:9])

    maxQueue = nodes.qsize()
    while(1):
        if nodes.empty():
            return "failure"
        node = nodes.get()
        print("The best state to expand with g(n) = {0} and h(n) = {1} is...".format(str(node.get_gn()),str(node.get_hn())))
        printNode(node.get_board())
        if problem.goal_test(node.get_board()):
            print("Goal!!!")
            print("Nodes expanded:{0}".format(str(problem.get_node_count())))
            print("Maximum num of nodes:{0}".format(str(maxQueue)))
            return node
        if (algorithm == 1):
            nodes = uniform(nodes, problem.operators(node))
        elif (algorithm == 2):
            nodes = misplaced_tiles(nodes, problem.operators(node))
        elif (algorithm == 3):
            nodes = euclidean(nodes, problem.operators(node))
        curSize = nodes.qsize()
        if curSize > maxQueue:
            maxQueue = curSize
            
# def uniformCostSearch(puzzle):
#     currPuzzleState = Node(puzzle.get_Init())
#     currPuzzleState.set_fn(0)
#     currPuzzleState.set_gn(0)
#     currPuzzleState.set_hn(0)


#     listOfPossibleOutcomesGn = []
#     listOfPossibleOutcomesPuzzle = []

#     solveUniform = PriorityQueue()
#     exploredUniform = PriorityQueue()
#     solveUniform.put(currPuzzleState)
#     exploredUniform.put(currPuzzleState)
#     while(solveUniform != ""):
#         print("hello")
#         newPuzzle = []
#         availableOperations = puzzle.operators(currPuzzleState)
#         #operators returns a list of NODES
#         #check goal state
#         if solveUniform.queue[0] == puzzle.goal:
#             return
#         else:
#             exploredUniform.put(solveUniform.get())
#         #pushing every possible operation
#         # for x in availableOperations:
#         #     possibility = x
#         #     listOfPossibleOutcomesPuzzle.append(possibility)
#         #     #and this is where I compute its heuristic thingy
#         #     gntemp = 0
#         #     for y in x.get_board():
#         #         if(x.find_any_number(y.get_board()) != puzzle.goal.find_any_number(y.get_board())):
#         #             gntemp += abs((currPuzzleState.find_any_number(y.get_board()) % 3) - (currPuzzleState.goal.find_any_number(y.get_board()) % 3))
#         #             gntemp += abs((currPuzzleState.find_any_number(y.get_board()) / 3) - (currPuzzleState.goal.find_any_number(y.get_board()) / 3))
#         #     listOfPossibleOutcomesGn += gntemp
#         # for z in listOfPossibleOutcomesGn:
#         #     whichOneToPushFirst = listOfPossibleOutcomesGn.index(max(listOfPossibleOutcomesGn))
#         #     newPuzzle = listOfPossibleOutcomesPuzzle[whichOneToPushFirst]
#         #     solveUniform.put(newPuzzle)
#         solveUniform.put(max(availableOperations.get_gn()))
