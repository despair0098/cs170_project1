# Libraries

print("Welcome to nceba003, zwang465, hmai015, bmott001 8 puzzle solver.")
print("Type '1' to use a default puzzle, or '2' to enter your own puzzle.")
choice = int(input())
if (choice == 1):
    print("You have chosen to use a default puzzle.")
    puzzle = [1, 0, 3, 4, 2, 6, 7, 5, 8]
elif (choice == 2):
    print("Enter your puzzle, use a zero to represent the blank.")
    puzzle = []    # TODO: Populate puzzle with user input
else:
    print("Invalid option.")