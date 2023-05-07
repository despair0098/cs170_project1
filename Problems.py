from queue import PriorityQueue
from node import *
import copy

class Problem:
    def __init__(self, init):
        self.init = init
        self.goal = (Node)[1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.node_count = 0

    def goal_test(self, node_state):
        return self.goal_state == node_state
    

    # from: https://realpython.com/python-enumerate/
    def find_blank(self, curr):
        for index, value in enumerate(curr):
            if value == 0:
                return index
            
    def find_any_number(self, curr, number):
        for index, value in enumerate(curr):
            if value == number:
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

    listOfPossibleOutcomesGn = []
    listOfPossibleOutcomesPuzzle = []

    # for x in puzzle:
    #     x.set_hn(0)
    solveUniform = PriorityQueue()
    exploredUniform = PriorityQueue()
    solveUniform.put(puzzle)
    exploredUniform.put(puzzle)
    while(solveUniform != ""):
        print("hello")
        newPuzzle = []
        availableOperations = [self.moveUp, self.moveDown, self.moveLeft, self.moveRight]
        #finding out where it can move
        if(self.find_blank(puzzle) % 3 == 0):
            #in this case, it can't go left
            del availableOperations[2]
        if(self.find_blank(puzzle) % 3 == 2):
            #in this case, it can't go right
            del availableOperations[3]
        if(self.find_blank(puzzle) < 3):
            #in this case, it can't go up
            del availableOperations[0]
        if(self.find_blank(puzzle) > 5):
            #in this case, it can't go down
            del availableOperations[1]
        #check goal state
        if solveUniform[0] == self.goal:
            return
        else:
            exploredUniform.put(solveUniform.get())
        #pushing every possible operation
        for x in availableOperations:
            possibility = puzzle.availableOperations[x]
            listOfPossibleOutcomesPuzzle += possibility
            #and this is where I compute its heuristic thingy
            gntemp = 0
            for y in possibility:
                if(possibility.find_any_number(y.get_board()) != puzzle.goal.find_any_number(y.get_board())):
                    gntemp += abs((puzzle.find_any_number(y.get_board()) % 3) - (puzzle.goal.find_any_number(y.get_board()) % 3))
                    gntemp += abs((puzzle.find_any_number(y.get_board()) / 3) - (puzzle.goal.find_any_number(y.get_board()) / 3))
            listOfPossibleOutcomesGn += gntemp
        for z in listOfPossibleOutcomesGn:
            whichOneToPushFirst = listOfPossibleOutcomesGn.index(max(listOfPossibleOutcomesGn))
            newPuzzle = listOfPossibleOutcomesPuzzle[whichOneToPushFirst]
            solveUniform.put(newPuzzle)
