#src/utils.py

#Utility functions for rendering and input.

import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def display_board(grid):
    clear_console()
    print("\n".join(["\t".join(map(str, row)) for row in grid]))
