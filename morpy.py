# Définition des variables
import random

play_board = [["" for _ in range(3)] for _ in range(3)]  # le tableau de jeu
SYMBOLS = ("X", "O")  # les symboles joués
computer_is_playing = True  # l’ordinateur joue en premier


def play() -> int:
    empties = []
    for i in range(9):
        line = i//3
        column =i%3
        if play_board[line][column] == "":
            empties.append(i+1)
    return random.choice(empties)


def show_board():
    pass