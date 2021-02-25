import morpy
import pytest


@pytest.fixture
def setup_any_board():
    tmp = morpy.play_board.copy()
    morpy.play_board = [["X", "O", ""],["X", "O", ""],["O", "X",""]]
    yield tmp
    morpy.play_board = tmp


def test_computer_plays():
    """ Doit retourner un chiffre entre 1 et 9"""
    assert 1 <= morpy.play() <= 9


def test_computer_plays_any_board(setup_any_board):
    """Doit retourner un chiffre représentant une case vide"""
    assert morpy.play() in [3,6,9]