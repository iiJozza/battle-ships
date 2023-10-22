import random
import time


class BattleshipGame:
    """
    Whole game class, contains all the game logic
    """
    def __init__(self, grid_size, num_of_ships):
        """
        Initialize the game parameters with grid size and number of ships
        """
        self.grid_size = grid_size
        self.num_of_ships = num_of_ships

        if self.num_of_ships > self.grid_size * self.grid_size:
            raise ValueError(
                "Number of ships can't exceed the grid size"
            )

        # Fill the board with 0's
        self.player_board = [
            ["0"] * self.grid_size for _ in range(self.grid_size)
        ]
        self.computer_board = [
            ["0"] * self.grid_size for _ in range(self.grid_size)
        ]

        # Initialize ship counts for the player and the computer
        self.player_ships_remaining = num_of_ships
        self.computer_ships_remaining = num_of_ships

        # Place the ships on the board
        self.place_ships(self.player_board)
        self.place_ships(self.computer_board)

    def print_board(self, hide_computer_ships=True):
        """
        Start the game and print the board
        """
        print("The Player's Board:")

        # Print column numbers
        print("    " + " ".join(str(i) for i in range(1, self.grid_size + 1)))

        # Print the top border of the box
        print("  +" + " -" * self.grid_size + " +")

        # Print the rows with row numbers and grid content
        for i, row in enumerate(self.player_board):
            print(f"{i + 1} | " + " ".join(row) + " |")

        # Print the bottom border of the box
        print("  +" + " -" * self.grid_size + " +")

        # Computer's board
        print("The Computer's Board:")

        if hide_computer_ships:
            computer_board_to_display = [
                ["0" if cell == "X" else cell for cell in row]
                for row in self.computer_board
            ]
        else:
            computer_board_to_display = self.computer_board

        print("    " + " ".join(str(i) for i in range(1, self.grid_size + 1)))

        # Print the top border of the box
        print("  +" + " -" * self.grid_size + " +")

        # Print the computer's board
        for i, row in enumerate(computer_board_to_display):
            print(f"{i + 1} | " + " ".join(row) + " |")

        # Print the bottom border of the computer board
        print("  +" + " -" * self.grid_size + " +")

    def place_ships(self, board):
        """
        Place the ships on the board
        """
        for _ in range(self.num_of_ships):
            # Generate a random row and column
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)

            # Check if the position is already occupied
            while board[row][col] == "X":
                row = random.randint(0, self.grid_size - 1)
                col = random.randint(0, self.grid_size - 1)

            # Place the ship
            board[row][col] = "X"

    def player_guess(self, row, col):
        """
        Check if the player has already guessed this spot
        """
        if self.computer_board[row - 1][col - 1] in ["H", "M"]:
            print("You already guessed that spot, try again")
            return False

        # Process the player's guess
        if self.computer_board[row - 1][col - 1] == "X":
            print("That is a hit!")
            # Reduce the computer's remaining ships count
            self.computer_ships_left -= 1
            print(f"You have: {self.computer_ships_left} more ships to sink")
            time.sleep(2)
        else:
            print("Missed!")
            self.computer_board[row - 1][col - 1] = "M"
            time.sleep(2)
        return True

    def computer_guess(self):
        """
        Process the computer's guess
        """
        while True:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            # Checks so the computer wont check the same spot twice
            if self.player_board[row][col] not in ["H", "M"]:
                break
        if self.player_board[row][col] == "X":
            print(
                f"Computer has hit your ship at ({row}, {col})"
                )
            self.player_board[row][col] = "H"
            # Reduce the player's remaining ships count
            self.player_ships_left -= 1
            print(f"You have: {self.player_ships_left} more ships to sink")
            time.sleep(2)
        else:
            print(
                f"Computer has missed your ship at ({row}, {col})"
                )
            self.player_board[row][col] = "M"
            time.sleep(2)

    def play(self):
        """
        Game loop, player and computer take turns guessing
        """
        while True:
            self.print_board()

            while True:
                try:
                    guess_row = int(input(f"Guess a row (1-{self.grid_size}): "))
                    guess_col = int(input(f"Guess a column (1-{self.grid_size}): "))

                    # To warn if the player guesses outside the grid
                    if (
                        guess_row < 1
                        or guess_row > self.grid_size
                        or guess_col < 1
                        or guess_col > self.grid_size
                    ):
                        print("That's outside the grid")
                        continue

                    if self.player_guess(guess_row - 1, guess_col - 1):  # Adjust for 0-based indexing
                        break
                except ValueError:
                    print("Please enter a number")

            # Check if the player has won
            if not any("X" in row for row in self.computer_board):
                print("You sank the computer's ships!")
                break

            # Computer's turn
            print("\nComputer's Turn")
            self.computer_guess()

            # Check if the computer has won
            if not any("X" in row for row in self.player_board):
                print("The computer has sunken all your ships!")
                break


if __name__ == "__main__":
    while True:
        while True:
            try:
                size = int(input("Enter the grid size: "))
                if size <= 0:
                    print("Grid size should be greater than 0.")
                    continue
                break
            except ValueError:
                print("Please enter a number")

        while True:
            try:
                num_of_ships = int(input("Enter the number of ships: "))
                if num_of_ships <= 0 or num_of_ships > size * size:
                    print("Number of ships should be greater than 0 and not exceed grid capacity.")
                    continue
                game = BattleshipGame(size, num_of_ships)
                break
            except ValueError as e:
                if "Number of ships can't exceed the grid size" in str(e):
                    print("You have entered more ships than the grid!")
                else:
                    print("Please enter a number")

        game.play()
        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break