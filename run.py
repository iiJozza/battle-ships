import random


class BattleshipGame:
    def __init__(self, grid_size, num_of_ships):

        
        self.grid_size = grid_size
        self.num_of_ships = num_of_ships

        def print_board(self, hide_computer_ships=True):
                """
                Prints the game boards for both player and computer, while hiding the computer's ships.
                """
                # Print the player's board
                print("The Player's Board:")

                # Printing column letters and lines (top)
                print("    " + " ".join(chr(65 + i) for i in range(self.grid_size)))
                print("  +" + " -" * self.grid_size + " +")

                # Printing rows with numbers(sides)
                for i, row in enumerate(self.player_board):
                    print(f"{i + 1} | " + " ".join(row) + " |")

                # Printing column lines (bottom)
                print("  +" + " -" * self.grid_size + " +")


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
