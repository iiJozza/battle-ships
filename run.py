import random
import time

class BattleshipGame:
    def __init__(self, grid_size, num_of_ships):
        self.grid_size = grid_size
        self.num_of_ships = num_of_ships

        if self.num_of_ships > self.grid_size * self.grid_size:
            raise ValueError("Number of ships can't exceed the grid size")

        self.player_board = [
            ["·"] * self.grid_size for _ in range(self.grid_size)
        ]
        self.computer_board = [
            ["·"] * self.grid_size for _ in range(self.grid_size)
        ]

        self.player_ships_remaining = num_of_ships
        self.computer_ships_remaining = num_of_ships

        self.place_ships(self.player_board)
        self.place_ships(self.computer_board)

    def print_board(self, hide_computer_ships=True):
        print("The Player's Board:")
        print("    " + " ".join(str(i) for i in range(1, self.grid_size + 1))
        )
        print("  +" + " -" * self.grid_size + " +")

        for i, row in enumerate(self.player_board):
            print(f"{i + 1} | " + " ".join(row) + " |")

        print("  +" + " -" * self.grid_size + " +")

        print("The Computer's Board:")

        if hide_computer_ships:
            computer_board_to_display = [
                ["·" if cell == "0" else cell for cell in row]
                for row in self.computer_board
            ]
        else:
            computer_board_to_display = self.computer_board

        print("    " + " ".join(str(i) for i in range(1, self.grid_size + 1))
        )
        print("  +" + " -" * self.grid_size + " +")

        for i, row in enumerate(computer_board_to_display):
            print(f"{i + 1} | " + " ".join(row) + " |")

        print("  +" + " -" * self.grid_size + " +")

    def place_ships(self, board):
        for _ in range(self.num_of_ships):
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)

            while board[row][col] == "0":
                row = random.randint(0, self.grid_size - 1)
                col = random.randint(0, self.grid_size - 1)

            board[row][col] = "0"

    def player_guess(self, row, col):
        if self.computer_board[row][col] in ["M"]:
            print("You already guessed that spot, try again")
            return False

        if self.computer_board[row][col] == "0":
            print("That is a hit!")
            self.computer_ships_remaining -= 1
            print(f"You have: {self.computer_ships_remaining} more ships to sink")
            self.computer_board[row][col] = "X"  # Update with "X" for hit
            time.sleep(2)
        else:
            print("Missed!")
            self.computer_board[row][col] = "M"
            time.sleep(2)
        return True

    def computer_guess(self):
        while True:
            row = random.randint(1, self.grid_size - 1)
            col = random.randint(1, self.grid_size - 1)
            if self.player_board[row][col] not in ["X", "M"]:
                break
        if self.player_board[row][col] == "0":
            print(f"Computer has hit your ship at ({row}, {col})")
            self.player_ships_remaining -= 1
            if self.player_ships_remaining == 0:
                print("Oh no! The computer sank all your ships. Better luck next time")
            else:
                print(f"The computer has only {self.player_ships_remaining} more ships to sink")
            self.player_board[row][col] = "X"  # Update with "0" for hit
            time.sleep(2)
        else:
            print(f"Computer has missed your ship at ({row}, {col})")
            self.player_board[row][col] = "M"
            time.sleep(2)
        
    def play(self):
        while True:
            self.print_board()

            while True:
                try:
                    guess_row = int(input(f"Guess a row (1-{self.grid_size}): "))
                    guess_col = int(input(f"Guess a column (1-{self.grid_size}): "))

                    if (
                        guess_row < 1
                        or guess_row > self.grid_size
                        or guess_col < 1
                        or guess_col > self.grid_size
                    ):
                        print("That's outside the grid")
                        continue

                    if self.player_guess(guess_row - 1, guess_col - 1):
                        break
                except ValueError:
                    print("Please enter a number")

            if not any("0" in row for row in self.computer_board):
                print("You sank the computer's ships!")
                break

            print("\nComputer's Turn")
            self.computer_guess()

            if not any("0" in row for row in self.player_board):
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
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
