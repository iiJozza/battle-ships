import random
import time

class BattleshipGame:
    def __init__(self, grid_size, num_of_ships):
        """
        Initializes game parameters and boards, placing ships randomly.
        """
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
        """
        Prints the game boards for both player and computer, while hiding the computer's ships.
        """
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
        """
        Generates and places ships at random
        """

        for _ in range(self.num_of_ships):
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)

            while board[row][col] == "0":
                row = random.randint(0, self.grid_size - 1)
                col = random.randint(0, self.grid_size - 1)

            board[row][col] = "0"

    def player_guess(self, row, col):
        """
        Handles player's guesses, showing hit or miss messages and indicating if all the computer's ships are sunk.
        """

        #Failsafe if user picked the same space
        if self.computer_board[row][col] in ["M"]:
            print("You already guessed that spot, try again")
            return False

        #Checks if the player hits a ship, and if the player won
        if self.computer_board[row][col] == "0":
            print("That is a hit!")
            self.computer_ships_remaining -= 1
            if self.computer_ships_remaining == 0:
                print("Congratulations!!! You have just sunk all the of the computer's ships.")
            else:
                print(f"The computer has only {self.computer_ships_remaining} more ships to sink")
            self.computer_board[row][col] = "X"
            time.sleep(2)

        #Checks if player missed
        else:
            print("Missed! Better luck next time.")
            self.computer_board[row][col] = "M"
            time.sleep(2)
        return True

    def computer_guess(self):
        """
        Process the computer's guess.
        """
        while True:
            row = random.randint(1, self.grid_size - 1)
            col = random.randint(1, self.grid_size - 1)
            if self.player_board[row][col] not in ["X", "M"]:
                break
        if self.player_board[row][col] == "0":
            print(f"Computer has hit your ship at ({row}, {col})")
            self.player_ships_remaining -= 1
            if self.player_ships_remaining == 0:
                print("Oh no! The computer sank all your ships. Better luck next time!")
            else:
                print(f"The computer has only {self.player_ships_remaining} more ships to sink")
            self.player_board[row][col] = "X"
            time.sleep(2)
        else:
            print(f"Computer has missed your ship at ({row}, {col})")
            self.player_board[row][col] = "M"
            time.sleep(2)

    def play(self):
        """
        Main game loop where the player and computer take turns guessing.
        """
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
                break

            print("\nThe Computer's Turn")
            self.computer_guess()

            if not any("0" in row for row in self.player_board):
                break

#Starting page before game start with introduction and rules
if __name__ == "__main__":
    print("===============================================================================================================")
    print("                                      Welcome to Battleship!")
    print("===============================================================================================================")
    print("""
    Welcome to a thrilling game of Battleship with a twist! In this version,
    the playing field features only 1x1 ships, creating an intense and strategic challenge.
    Your task is to outsmart your opponent and sink their tiny, elusive ships while protecting your own.
    Precision and tactics are the name of the game in this compact naval battle. Are you ready to test
    your skills and emerge victorious in this micro-sized maritime showdown?

    What the symbols mean:
    ·  = Symbolizes that this coordinate haven't been shot at
    X  = Symbolizes that a ship has been struck
    M  = Symbolizes that you missed and hit nothing.
    0  = Symbolizes where your ships are located at

    How to play:
    1. Whenever you feel you want to play a new game, restart the current one or have just finished playing press the
    big button called "Run Program".
    2. Type in the terminal how large you want your square grid to be. If you type 6, it will produce a 6x6 grid
    3. Type in how many ships you want to play with. These ships will be scattered around the grid randomly
    4. You are now presented with 2 different game boards. The one on top is where your ships are located, and keeps
    track where the computer has aimed their shots,and the bottom one is the grid for the computer and keeps track where
    you have aimed your shots.
    5. Type in the terminal what row you want to aim at and afterwards what column. E.g Type in 1 in row, and later 3 in
    column to shot at the 1,3 coordinate.
    6. You will be presented with eiter an X - which means you have hit a ship, or M - which symbolizes that you missed.
    7. The aim of the game is to sink every ship of your opponent.
    8. And the most important: To have fun!
    """
    )

    #Collects user input for grid size and the number of ships to set up the game.
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

        #Continues or ends the game based on the player's input.
        game.play()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
