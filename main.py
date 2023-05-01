# Libraries

print("Welcome to nceba003, zwang465, hmai015, bmott001 8 puzzle solver.")
print("Type '1' to use a default puzzle, or '2' to enter your own puzzle.")
choice = int(input())

if (choice == 1):
    print("You have chosen to use a default puzzle.")
    puzzle = [1, 0, 3, 4, 2, 6, 7, 5, 8]
    print(puzzle)   # temp debug

elif (choice == 2):
    print("Enter your puzzle, use a zero to represent the blank.")
    puzzle = [int(item) for item in input("Enter the first row, use space or tabs between numbers\n").split()]
    puzzle += [int(item) for item in input("Enter the second row, use space or tabs between numbers\n").split()]
    puzzle += [int(item) for item in input("Enter the second row, use space or tabs between numbers\n").split()]
    print(puzzle)   # temp debug

else:
    print("Invalid option.")
    exit(0)

print("Enter your choise of algorithm\n1. Uniform Cost Search.\n2. A* with the Misplaced Tile heuristic.\n3. A* with the Euclidean distance heuristic.")
choice = int(input())
if (choice > 3):
    print("Invalid option.")
    exit(0)