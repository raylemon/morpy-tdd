# Définition des variables
import random

play_board = [["" for _ in range(3)] for _ in range(3)]  # le tableau de jeu
SYMBOLS = ("X", "O")  # les symboles joués
computer_is_playing = True  # l’ordinateur joue en premier


def play(is_human: bool = False) -> int:
    empties = []
    for i in range(9):
        line = i // 3
        column = i % 3
        if play_board[line][column] == "":
            empties.append(i + 1)

    if len(empties) == 0:
        return -1

    if is_human:
        rep = input(f"Sélectionnez une case vide ({empties}): ")
        if not rep.isdigit() or int(rep) not in empties:
            return -1
        else:
            return int(rep)
    else:
        return random.choice(empties)


def show_board():
    i = 1
    for line in play_board:
        for cell in line:
            if cell == "":
                print(i, end=" ")
            else:
                print(cell, end=" ")
            i += 1
        print()


def is_won_vert(symbol, column):
    pass