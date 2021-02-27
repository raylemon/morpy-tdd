# Définition des variables
import random

play_board = [["" for _ in range(3)] for _ in range(3)]  # le tableau de jeu
computer_is_playing = True  # l’ordinateur joue en premier


def play(symbol, is_human: bool = False) -> int:
    empties = find_empties()
    if len(empties) == 0:
        return -1

    if is_human:
        rep = input(f"Sélectionnez une case vide ({empties}): ")
        if not rep.isdigit() or int(rep) not in empties:
            return -1
        else:
            return int(rep)
    else:
        return random.choice(predict(symbol))


def find_empties() -> list:
    empties = []
    for i in range(9):
        line = i // 3
        column = i % 3
        if play_board[line][column] == "":
            empties.append(i + 1)
    return empties


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


def is_won_vert(symbol: str) -> bool:
    transpose = [list(i) for i in zip(*play_board)]
    for line in range(3):
        if transpose[line].count(symbol) == 3:
            return True
    return False


def is_won_hor(symbol: str) -> bool:
    for line in range(3):
        if play_board[line].count(symbol) == 3:
            return True
    return False


def is_won_slash(symbol: str) -> bool:
    for i in range(3):
        if play_board[i][2 - i] != symbol:
            return False
    return True


def is_won_bslash(symbol: str) -> bool:
    for i in range(3):
        if play_board[i][i] != symbol:
            return False
    return True


def is_won(symbol: str) -> bool:
    return is_won_vert(symbol) or is_won_hor(symbol) or is_won_bslash(symbol) or is_won_slash(symbol)


def predict(symbol: str) -> list:
    opposite = "O" if symbol == "X" else "X"
    empties = find_empties()
    wins = []
    counter_wins = []

    for c in empties:
        c -= 1
        line = c // 3
        column = c % 3
        play_board[line][column] = symbol
        if is_won(symbol):
            wins.append(c + 1)
        play_board[line][column] = opposite
        if is_won(opposite):
            counter_wins.append(c + 1)
        play_board[line][column] = ""

    if len(wins) > 0:
        return wins
    elif len(counter_wins) > 0:
        return counter_wins
    else:
        return empties
