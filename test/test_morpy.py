from io import StringIO

import pytest

import morpy

any_board = [["X", "O", ""], ["X", "O", ""], ["O", "X", ""]]
other_board = [["X", "O", ""], ["X", "O", "O"], ["O", "X", "X"]]
win_board_o_hor = [["O", "O", "O"], ["", "", ""], ["", "", ""]]
win_board_x_hor = [["X", "X", "X"], ["", "", ""], ["", "", ""]]
win_board_o_ver = [["O", "", ""], ["O", "", ""], ["O", "", ""]]
win_board_x_ver = [["X", "", ""], ["X", "", ""], ["X", "", ""]]
win_board_o_bslash = [["O", "", ""], ["", "O", ""], ["", "", "O"]]
win_board_x_bslash = [["X", "", ""], ["", "X", ""], ["", "", "X"]]
win_board_o_slash = [["", "", "O"], ["", "O", ""], ["O", "", ""]]
win_board_x_slash = [["", "", "X"], ["", "X", ""], ["X", "", ""]]
win_full_board_o = [["X", "X", "O"], ["X", "O", "X"], ["O", "X", "X"]]
win_full_board_x = [["O", "O", "X"], ["O", "X", "O"], ["X", "O", "O"]]
draw_board = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
board_x_can_win_ver = [["X", "", ""], ["X", "", ""], ["", "", ""]]
board_o_can_win_ver = [["O", "", ""], ["O", "", ""], ["", "", ""]]
board_x_can_win_hor = [["X", "", ""], ["X", "", ""], ["", "", ""]]
board_o_can_win_bslash = [["O", "", ""], ["", "O", ""], ["", "", ""]]
board_x_can_win_bslash = [["X", "", ""], ["", "X", ""], ["", "", ""]]
board_o_can_win_slash = [["", "", ""], ["", "O", ""], ["O", "", ""]]
win_board_x_can_win_slash = [["", "", ""], ["", "X", ""], ["X", "", ""]]


@pytest.fixture
def setup(request):
    tmp = morpy.play_board.copy()
    morpy.play_board = request.param
    yield
    morpy.play_board = tmp


@pytest.mark.parametrize("rep", range(50))
def test_computer_play_empty_board(rep):
    """ Doit retourner un chiffre entre 1 et 9"""
    print(f"tentative n°{rep}")  # inutile, mais pour le fun
    assert 1 <= morpy.play() <= 9


@pytest.mark.parametrize("rep", range(20))
@pytest.mark.parametrize("setup,result", [
    (any_board, [3, 6, 9]),
    (other_board, [3]),
    (win_board_o_hor, [4, 5, 6, 7, 8, 9]),
    (win_board_o_ver, [2, 3, 5, 6, 8, 9]),
    (win_board_o_bslash, [2, 3, 4, 6, 7, 8]),
    (win_board_o_slash, [1, 2, 4, 6, 8, 9]),
    (win_full_board_o, [-1]),
    (draw_board, [-1]),
], indirect=["setup"])
def test_computer_play(rep, setup, result):
    """Doit retourner un chiffre représentant une case vide"""
    assert morpy.play() in result


def test_human_play_empty_board(monkeypatch):
    """Imite le joueur humain choisissant la position 5"""
    s_in = StringIO("5")
    monkeypatch.setattr("sys.stdin", s_in)
    assert morpy.play(is_human=True) == 5


@pytest.mark.parametrize("setup, result", [
    (any_board, -1),
    (other_board, -1),
    (win_board_o_hor, 5),
    (win_board_o_ver, 5),
    (win_board_o_bslash, -1),
    (win_board_o_slash, -1),
    (win_full_board_o, -1),
    (draw_board, -1)
], indirect=["setup"])
def test_human_play(setup, result, monkeypatch):
    """Imite le joueur humain choisissant la position 5, avec indication s’il peut la jouer ou non"""
    s_in = StringIO("5")
    monkeypatch.setattr("sys.stdin", s_in)
    assert morpy.play(is_human=True) == result


@pytest.mark.parametrize("setup,result", [
    (any_board, "X O 3 \nX O 6 \nO X 9 \n"),
    (other_board, "X O 3 \nX O O \nO X X \n"),
    (win_board_o_hor, "O O O \n4 5 6 \n7 8 9 \n"),
    (win_board_x_hor, "X X X \n4 5 6 \n7 8 9 \n"),
    (win_board_o_ver, "O 2 3 \nO 5 6 \nO 8 9 \n"),
    (win_board_x_ver, "X 2 3 \nX 5 6 \nX 8 9 \n"),
    (win_board_o_bslash, "O 2 3 \n4 O 6 \n7 8 O \n"),
    (win_board_x_bslash, "X 2 3 \n4 X 6 \n7 8 X \n"),
    (win_full_board_o, "X X O \nX O X \nO X X \n"),
    (win_full_board_x, "O O X \nO X O \nX O O \n"),
    (draw_board, "X O X \nX O O \nO X X \n"),
], indirect=["setup"])
def test_show_board(setup, result, capsys):
    """"Affiche le tableau"""
    morpy.show_board()
    assert result == capsys.readouterr().out
