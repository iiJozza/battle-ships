import random

def create_grid(size):
    if size < 1 or size > 9:
        raise ValueError("Grid size must be between 1 and 9")

    grid = [["·"] * size for _ in range(size)]

    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

if __name__ == "__main__":
    while True:
        while True:
            try:
                size = int(input("Enter the grid size: "))
                if size <= 0:   # check if the size is valid
                    print( "Grid size should be greater than 0.")
                    continue
                break
            except ValueError:
                print("Please enter a number")

        while True:
            try:
                num_of_ships = int(input("Enter the number of ships: "))
                if num_of_ships <= 0 or num_of_ships > size*size:   # check if the number of ships is valid
                    print("Number of ships should be greater than 0 and not exceed grid capacity.")
                    continue
                game = BattleshipGame(size, num_of_ships)
                break
            except ValueError as e:
                if "Number of ships can't exceed the grid size" in str(e):
                    print("You have entered more ships than the grid!")
                else:
                    print("Please enter a number")
