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