import random
import time
import pyfiglet
from colorama import Fore, Back, Style

extra_spaces = " " * 8


class BattleshipGame:
    def __init__(self, grid_size, num_of_ships):
        """
        Initializes game parameters and boards, placing ships randomly.
        The maximum grid size is 9x9.
        """

        # Validates that the grid size is within the range of 1 to 9
        if grid_size < 1 or grid_size > 9:
            raise ValueError("Grid size must be between 1 and 9")

        # Size of the grid
        self.grid_size = grid_size

        # Number of ships
        self.num_of_ships = num_of_ships

        # Checks if number of ships are not > than total of spaces on the grid
        if self.num_of_ships > self.grid_size * self.grid_size:
            raise ValueError("Number of ships can't exceed the grid size")

        # Creates player and computer game boards
        self.player_board = [
            ["·"] * self.grid_size for _ in range(self.grid_size)
        ]
        self.computer_board = [
            ["·"] * self.grid_size for _ in range(self.grid_size)
        ]

        # Number of ships remaining
        self.player_ships_remaining = num_of_ships
        self.computer_ships_remaining = num_of_ships

        # Place ships randomly on the boards
        self.place_ships(self.player_board)
        self.place_ships(self.computer_board)

    def print_board(self, hide_computer_ships=True):
        """
        Prints the game boards, while hiding the computer's ships.
        """

        print(f"{extra_spaces}The Player's Board:")

        # Prints the player's game board with row and column labels
        print(f"{extra_spaces}    " + " \
".join(chr(65 + i) for i in range(self.grid_size)))
        print(f"{extra_spaces}  +" + " -" * self.grid_size + " +")

        for i, row in enumerate(self.player_board):
            print(f"{extra_spaces}{i + 1} | " + " ".join(row) + " |")

        print(f"{extra_spaces}  +" + " -" * self.grid_size + " +")

        print(f"{extra_spaces}The Computer's Board:")

        # Hides the computers ships
        if hide_computer_ships:
            computer_board_to_display = [
                ["·" if cell == "0" else cell for cell in row]
                for row in self.computer_board
            ]
        else:
            computer_board_to_display = self.computer_board

        # Prints the computer's game board with row and column labels
        print(f"{extra_spaces}    " + " \
".join(chr(65 + i) for i in range(self.grid_size)))
        print(f"{extra_spaces}  +" + " -" * self.grid_size + " +")

        for i, row in enumerate(computer_board_to_display):
            print(f"{extra_spaces}{i + 1} | " + " ".join(row) + " |")

        print(f"{extra_spaces}  +" + " -" * self.grid_size + " +")

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
        Handles player's guesses, hits and misses.
        """
        # Failsafe if the user picked the same space
        if self.computer_board[row][col] == "M":
            print(f"{extra_spaces}You already guessed that spot, try again")
            return False

        # Checks if the player hits a ship, and if the player won
        if self.computer_board[row][col] == "0":
            print(Fore.RED + f"\n{extra_spaces}That is a " "hit!\
" + Style.RESET_ALL)
            self.computer_ships_remaining -= 1

            if self.computer_ships_remaining == 0:
                print(f"{extra_spaces}Congratulations!!!")
            else:
                print(f"{extra_spaces}There're \
{self.computer_ships_remaining} \
ships left")
            self.computer_board[row][col] = "X"
            time.sleep(2)

        # Checks if the player missed
        else:
            print(Fore.BLUE + f"\n{extra_spaces}Missed! Better luck next time.\
" + Style.RESET_ALL)
            self.computer_board[row][col] = "M"
            time.sleep(2)
        return True

    def computer_guess(self):
        """
        Process the computer's guess.
        """
        while True:

            # Randomizes computer guesses
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            if self.player_board[row][col] not in ["X", "M"]:
                break

        # Checks if computer won/hit/miss a ship. Updates grid afterwards
        if self.player_board[row][col] == "0":
            print(Fore.RED + f"{extra_spaces}Computer hit your ship at\
 ({chr(65 + col)}, {row + 1})" + Style.RESET_ALL)
            self.player_ships_remaining -= 1
            if self.player_ships_remaining == 0:
                print(f"{extra_spaces}Oh no! The computer sank \
all your ships!")
            else:
                print(f"{extra_spaces}You've got \
{self.player_ships_remaining} \
ships left\n")
            self.player_board[row][col] = "X"
            time.sleep(2)
        else:
            print(Fore.BLUE + f"\n{extra_spaces}Computer has missed! \
They shot at\
({chr(65 + col)}, {row + 1})" + Style.RESET_ALL)
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
                    # Row
                    max_char = chr(64 + self.grid_size)
                    guess_row = input(f"{extra_spaces}\
Guess a row between (A-{max_char}): ").upper()

                    # Checks if the player wants to exit the game
                    if guess_row.lower() == "exit":
                        print(f"{extra_spaces}Exiting the game. Goodbye!")
                        return

                    # Checks if it's a letter
                    if not guess_row.isalpha():
                        print(f"{extra_spaces}Invalid input. \
Please enter a letter between (A-{max_char}).")
                        continue

                    # Column
                    guess_col = input(f"{extra_spaces}\
Guess a column between (1-{self.grid_size}): ")

                    # Checks if the player wants to exit the game
                    if guess_col.lower() == "exit":
                        print(f"{extra_spaces}Exiting the game. Goodbye!")
                        return

                    # Converts from str -> int
                    else:
                        guess_col = int(guess_col)

                    # Checks if the number is valid
                    if (
                        ord(guess_row.upper()) < 65
                        or ord(guess_row.upper()) > (65 + self.grid_size - 1)
                        or int(guess_col) < 1
                        or int(guess_col) > self.grid_size
                    ):
                        print(f"{extra_spaces}That's outside the grid")
                        continue

                    if self.player_guess(ord(guess_row) - 65, guess_col - 1):
                        break

                # Error message for invalid column input
                except ValueError:
                    print(f"{extra_spaces}Enter a valid number between 1 -\
{self.grid_size}!")

            #  Checks if player won and ends the game if true.
            if not any("0" in row for row in self.computer_board):
                break

            print(f"\n{extra_spaces}The Computer's Turn")
            game.loading_animation(5)
            self.computer_guess()

            # Checks if computer won and ends the game if true
            if not any("0" in row for row in self.player_board):
                break

    # Small simulation of the computer "thinking"
    def loading_animation(self, seconds):
        """
        Small loading animation with dots
        """
        print(f"{extra_spaces}", end="", flush=True)
        for _ in range(seconds):
            print(". ", end="", flush=True)
            time.sleep(0.7)
        print()


if __name__ == "__main__":
    # Starting page before game start with introduction and rules

    from colorama import Fore, Back, Style, init

    init()  # Initialize colorama

    font = pyfiglet.Figlet(font='slant')
    text = (Fore.BLUE + "\
            ============================================================\n\
" + Fore.WHITE + font.renderText('    BATTLESHIPS\n') + Fore.RED + "\
            ============================================================")

    print(text)

    print(Fore.GREEN + Style.BRIGHT + """
        Welcome to a thrilling game of Battleship with a twist! In this\
version,
        the playing field features only 1x1 ships, creating an intense and
        strategic challenge.
        """ + Style.RESET_ALL)

    print(Fore.MAGENTA + Style.BRIGHT + """
        What the symbols mean:
        ·  = Symbolizes that this coordinate hasn't been shot at
        """ + Fore.RED + "X" + Fore.MAGENTA + """  = \
Symbolizes that a ship has been struck
        """ + Fore.WHITE + "0" + Fore.MAGENTA + """  = \
Symbolizes where your ships are located
        """ + Fore.BLUE + "M" + Fore.MAGENTA + """  = \
Symbolizes that you missed and hit nothing
    """ + Style.RESET_ALL)

    print(Fore.YELLOW + Style.BRIGHT + """
        How to play:
        1. Start the game by pressing the "run program" button
        2. Type your preferred size grid. E.g typing a 6 will make the grid 6x6
        3. Type your ship count, they'll be placed randomly on the grid
        4. The top grid is yours and the bottom grid is your opponent's
        5. Typing a coordinate e.g (A, 3) shots the matching tile
        6. The computer and the user alternate turns until a winner is crowned.
        7. The aim of the game is to sink every ship of your opponent.
        8. Whenever you want to restart a new game or quit, type "exit".
        9. And, most importantly, have fun!
        """ + Style.RESET_ALL)

    while True:
        while True:
            try:
                # Obtains and validates the grid size input from the user
                size = int(input(f"{extra_spaces}Enter the grid size (1-9): "))
                if size < 1 or size > 9:
                    print(f"{extra_spaces}Grid size should be \
between 1 and 9.")
                    continue
                break
            except ValueError:
                print(f"{extra_spaces}Please enter a valid number")

        while True:
            try:
                # Validates ship count input
                num_of_ships = int(input(f"{extra_spaces}\
Enter the number of ships: "))
                if num_of_ships <= 0 or num_of_ships > size * size:
                    print(f"{extra_spaces}Ship amount entered is invalid")
                    continue
                game = BattleshipGame(size, num_of_ships)
                break

            except ValueError as e:
                # Error message for unvalid input
                if "Number of ships can't exceed the grid size" in str(e):
                    print(f"{extra_spaces}You've entered more ships \
than the grid can handle")
                else:
                    print(f"{extra_spaces}Please enter a valid number")

        # Continues or ends the game based on the player's input.
        game.play()
        while True:
            play_again = input(f"{extra_spaces}Do you want to play again? \
(yes/no): ")
            if play_again.lower() == "yes":
                print(f"{extra_spaces}Perfect! \
Let me start a new game for you.")
                game.loading_animation(3)
                break
            elif play_again.lower() == "no":
                print(f"{extra_spaces}Thank you for playing.")
                exit()
            else:
                print(f"{extra_spaces}Please choose 'yes' or 'no'")
