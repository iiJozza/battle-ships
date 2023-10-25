import random
import time
import pyfiglet
from colorama import Fore, Back, Style


class BattleshipGame:
    def __init__(self, grid_size, num_of_ships):
        """
        Initializes game parameters and boards, placing ships randomly.
        The maximum grid size is 9x9.
        """
        if grid_size < 1 or grid_size > 9:
            raise ValueError("Grid size must be between 1 and 9")

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
        Prints the game boards, while hiding the computer's ships.
        """
        print("The Player's Board:")

        print("    " + " ".join(chr(65 + i) for i in range(self.grid_size)))
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

        print("    " + " ".join(chr(65 + i) for i in range(self.grid_size)))
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
        Handles player's guesses, hits and misses.
        """
        # Failsafe if the user picked the same space
        if self.computer_board[row][col] == "M":
            print("You already guessed that spot, try again")
            return False

        # Checks if the player hits a ship, and if the player won
        if self.computer_board[row][col] == "0":
            print(Fore.RED + f"\nThat is a " "hit!" + Style.RESET_ALL)
            self.computer_ships_remaining -= 1

            if self.computer_ships_remaining == 0:
                print("Congratulations!!!")
            else:
                print(f"There're {self.computer_ships_remaining} ships left")
            self.computer_board[row][col] = "X"
            time.sleep(2)

        # Checks if the player missed
        else:
            print(Fore.BLUE + "\nMissed! Better luck next time.\
" + Style.RESET_ALL)
            self.computer_board[row][col] = "M"
            time.sleep(2)
        return True

    def computer_guess(self):
        """
        Process the computer's guess.
        """
        while True:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
            if self.player_board[row][col] not in ["X", "M"]:
                break
        if self.player_board[row][col] == "0":
            print(Fore.RED + f"Computer hit your ship at\
 ({chr(65 + col)}, {row + 1})" + Style.RESET_ALL)
            self.player_ships_remaining -= 1
            if self.player_ships_remaining == 0:
                print("Oh no! The computer sank all your ships!")
            else:
                print(f"You've got {self.player_ships_remaining} ships left\n")
            self.player_board[row][col] = "X"
            time.sleep(2)
        else:
            print(Fore.BLUE + f"\nComputer has missed! They shot at\
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
                    guess_row = input(f"Guess a row (A-{max_char}): ").upper()
                    
                    # Checks if the player wants to exit the game 
                    if guess_row.lower() == "exit":
                        print("Exiting the game. Goodbye!")
                        return

                    # Checks if it's a letter
                    if not guess_row.isalpha():
                        print(f"Invalid input. Please enter a letter between \
(A-{max_char}).")
                        continue
                    
                    # Column
                    guess_col = input(f"Column (1-{self.grid_size}): ")
                    
                    # Checks if the player wants to exit the game
                    if guess_col.lower() == "exit":
                        print("Exiting the game. Goodbye!")
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
                        print("That's outside the grid")
                        continue

                    if self.player_guess(ord(guess_row) - 65, guess_col - 1):
                        break
                
                # Error message for invalid column input
                except ValueError:
                    print(f"Enter a valid number between 1 -{self.grid_size}!")

            #  Checks if player won and ends the game if true.
            if not any("0" in row for row in self.computer_board):
                break

            print("\nThe Computer's Turn")
            self.computer_guess()
            
            # Checks if computer won and ends the game if true
            if not any("0" in row for row in self.player_board):
                break

    # Small simulation of the computer "thinking"
    def loading_animation(self, seconds):
        """
        Small loading animation with dots
        """
        for _ in range(seconds):
            print(". ", end="", flush=True)
            time.sleep(0.7)  
        print()

# Starting page before game start with introduction and rules


if __name__ == "__main__":
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
        8. And, most importantly, have fun!
        """ + Style.RESET_ALL)
   
    while True:
        while True:
            try:
                size = int(input("Enter the grid size (1-9): "))
                if size < 1 or size > 9:
                    print("Grid size should be between 1 and 9.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number")

        while True:
            try:
                num_of_ships = int(input("Enter the number of ships: "))
                if num_of_ships <= 0 or num_of_ships > size * size:
                    print("Ship amount entered is invalid")
                    continue
                game = BattleshipGame(size, num_of_ships)
                break
            except ValueError as e:
                if "Number of ships can't exceed the grid size" in str(e):
                    print("You've entered more ships than the grid can handle")
                else:
                    print("Please enter a valid number")

        # Continues or ends the game based on the player's input.
        game.play()
        while True:
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() == "yes":
                print("Perfect! Let me start a new game for you.")
                game.loading_animation(3)
                break
            elif play_again.lower() == "no":
                print("Thank you for playing.")
                exit()
            else:
                print("Please choose 'yes' or 'no'")
