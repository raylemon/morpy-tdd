from io import StringIO

import morpy
import pytest


@pytest.fixture
def setup_any_board():
    tmp = morpy.play_board.copy()
    morpy.play_board = [["X", "O", ""], ["X", "O", ""], ["O", "X", ""]]
    yield
    morpy.play_board = tmp


@pytest.fixture
def setup_other_board():
    tmp = morpy.play_board.copy()
    morpy.play_board = [["X", "O", ""], ["X", "O", "O"], ["O", "X", "X"]]
    yield
    morpy.play_board = tmp


def test_computer_plays():
    """ Doit retourner un chiffre entre 1 et 9"""
    assert 1 <= morpy.play() <= 9


def test_computer_plays_any_board(setup_any_board):
    """Doit retourner un chiffre représentant une case vide"""
    assert morpy.play() in [3, 6, 9]


def test_computer_plays_other_board(setup_other_board):
    """Doit retourner un chiffre représentant une case vide"""
    assert morpy.play() == 3


def test_human_plays(monkeypatch):
    """Imite le joueur humain choisissant la position 5"""
    s_in = StringIO("5")
    monkeypatch.setattr("sys.stdin", s_in)
    assert morpy.play(is_human=True) == 5


def test_human_plays_any_board(setup_any_board, monkeypatch):
    """Imite le joueur humain choisissant la position 5, sauf qu’il ne peut PAS la jouer"""
    s_in = StringIO("5")
    monkeypatch.setattr("sys.stdin", s_in)
    assert morpy.play(is_human=True) == -1


def test_show_board(capsys):
    """"Affiche le tableau de jeu vide"""
    morpy.show_board()
    assert "1 2 3 \n4 5 6 \n7 8 9 \n" == capsys.readouterr().out


def test_show_board_any_board(setup_any_board, capsys):
    """Affiche le tableau de jeu
        X O 3
        X O 6
        O X 9
    """
    morpy.show_board()
    assert "X O 3 \nX O 6 \nO X 9 \n" == capsys.readouterr().out


def test_show_board_other_board(setup_other_board, capsys):
    """Affiche le tableau de jeu
        X O 3
        X O O
        O X X
    """
    morpy.show_board()
    assert "X O 3 \nX O O \nO X X \n" == capsys.readouterr().out
