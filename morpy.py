# Définition des variables
import random

play_board = [["" for _ in range(3)] for _ in range(3)]  # le tableau de jeu
SYMBOLS = ("X", "O")  # les symboles joués
computer_is_playing = True  # l’ordinateur joue en premier


def play() -> int:
    return random.randint(1, 9)
