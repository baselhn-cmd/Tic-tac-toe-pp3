import os
    def clear_screen('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): \n")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Try again.")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose your symbol (letters only): \n")
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

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for number, player in enumerate(self.player, start=1):
            print(f"Player {number}, enter your details:")
            player.choose_name()
            player.choose_symbol()
            clear_screen()

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
    
    def restart_game(self):
        self.board.reset.board()
        self.current_player_indix = 0
        self.play_game()

       

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
            [0, 4, 8], [2, 4, 6]  # diagonal
        ]
        for combination in win_combinations_
            if self.board.board[combination[0]] == self.board.board[combination[1]] == \
                self.board.board[combination[2]] != "":
                print(f"{self.players[self.current_player_index].name} wins!")
                return True
        return False

       
    def check_draw(self):
        for cell in range(len(self.board.board)):
            if self.board.board[cell].isdigit():
                return False
        print("Draw! No one wins")
        return True

    
    def play_turn(self):
        player = self.player[self.current_player_indix]
        seld.board.display_board()
        print(f"{player.name}, choose your move: ({player.symbol})")
        while True:
            try:
                cell_choice = int(input("Enter your choice (1-9": ))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move. Try agin.")
            except ValueError:
                print("Invalid move. Try again.")
        self.switch_player()
    
    def switch_player(self):
        self.current_player_indix = 1 - self.current_player_indix

    def quit_game(self):
        print("Thanks for playing")


    



    


    
    

