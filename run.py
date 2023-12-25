class Player:
    def __init(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Try again.")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose your symbol (letters only): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol. Try again.")
# Menu class for displaying menus
class Menu:
    def display_main_menu(self):
        print("Welcome to my Tic-Tac-Toe game!")
        print("1. Start a new game")
        print("2. Quit")
        choice = input("Enter your choice (1 or 2): ")
        return choice

    """
    Choice for the Game
    """

    def display_endgame_menu(self):
        choice = input("Game Over!\n1. Play again\n2. Quit\nEnter your choice (1 or 2): ")
        return choice


class Board:
    """
    Board class for managing the game board
    """
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]
    

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))
            if i < 6:
                print("-"*5)

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def is_valid_move(self,choice)
       return self.board[choice - 1].isdigit()

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]

class Game:
    def __init__(self):
        self.Players = [Player(), player()]
        self.board = Board()
        self.menu = Menu
        self.current_player_indix = 0  



    


    
    

