# Libraries
import node
import Problems
import time

def main():
    print("Welcome to nceba003, zwang465, hmai015, bmott001 8 puzzle solver.")
    print("Type '1' to use a default puzzle, or '2' to enter your own puzzle.")
    choice = int(input())

    if (choice == 1):
        print("You have chosen to use a default puzzle.")
        puzzle = [1, 2, 3, 4, 8, 0, 7, 6, 5]
        temp = Problems.Problem(puzzle)
        start = time.time()
        node = Problems.general_alg(temp)
        end = time.time()
        #print(puzzle)   # temp debug
        print("Time to finish: {}".format(end - start))

    elif (choice == 2):
        print("Enter your puzzle, use a zero to represent the blank.")
        puzzle = [int(item) for item in input("Enter the first row, use space or tabs between numbers\n").split()]
        puzzle += [int(item) for item in input("Enter the second row, use space or tabs between numbers\n").split()]
        puzzle += [int(item) for item in input("Enter the second row, use space or tabs between numbers\n").split()]
        for x in puzzle:
            check = x
            for y in puzzle:
                if (check==y):
                    print("Invalid puzzle.")
                    exit(0)
                    break
            print(puzzle)   # temp debug
        else:
            print("Invalid option.")
            exit(0)

    puzzle2 = []
    puzzle2 = Problems.Problem(puzzle)

    print("Enter your choice of algorithm\n1. Uniform Cost Search.\n2. A* with the Misplaced Tile heuristic.\n3. A* with the Euclidean distance heuristic.")
    choice = int(input())
    if (choice > 3 or choice < 1):
        print("Invalid option.")
        exit(0)
    elif (choice == 1):
        start = time.time()
        solution = Problems.uniformCostSearch(puzzle2)
        end = time.time()
        print("Time taken = " + end-start)

main()
