import os
"""
Function to clear the console screen
"""
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    """
    Start the game with choice quit
    """
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