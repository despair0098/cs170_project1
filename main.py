# Libraries
import node
import Problems
import time

print("Welcome to nceba003, zwang465, hmai015, bmott001 8 puzzle solver.")
print("Type '1' to use a default puzzle, or '2' to enter your own puzzle.")
choice = int(input())

if (choice == 1):
    print("You have chosen to use a default puzzle.")
    puzzle = [1, 2, 3, 4, 8, 0, 7, 6, 5]

elif (choice == 2):
    print("Enter your puzzle, use a zero to represent the blank.")
    puzzle = [int(item) for item in input("Enter the first row, use space or tabs between numbers\n").split()]
    puzzle += [int(item) for item in input("Enter the second row, use space or tabs between numbers\n").split()]
    puzzle += [int(item) for item in input("Enter the second row, use space or tabs between numbers\n").split()]
    checkRepeat = len(set(puzzle))
    if (checkRepeat != 9 or len(puzzle) != 9):
        print("Invalid puzzle.")
        exit(0)
    for x in puzzle:
        if (x > 8 or x < 0):
            print("Invalid puzzle.")
            exit(0)
            break
    print(puzzle)   # temp debug
else:
    print("Invalid option.")
    exit(0)

print("Enter your choise of algorithm\n1. Uniform Cost Search.\n2. A* with the Misplaced Tile heuristic.\n3. A* with the Euclidean distance heuristic.")
choice = int(input())
if (choice > 3 or choice < 1):
    print("Invalid option.")
    exit(0)
else:
    temp = Problems.Problem(puzzle)
    start = time.time()
    node = Problems.general_alg(temp, choice)
    end = time.time()
    #print(puzzle)   # temp debug
    print("Time to finish: {}".format(end - start))
