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
        try:
            size = int(input("Enter the grid size (1-9): "))
            grid = create_grid(size)
            print_grid(grid)
            break
        except ValueError:
            print("Please enter a valid number for the grid size.")