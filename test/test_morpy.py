from io import StringIO

import pytest

import morpy

any_board = [["X", "", ""], ["X", "", "O"], ["O", "X", ""]]
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
board_x_can_win_hor = [["X", "X", ""], ["", "", ""], ["", "", ""]]
board_o_can_win_hor = [["O", "O", ""], ["", "", ""], ["", "", ""]]
board_o_can_win_bslash = [["O", "", ""], ["", "O", ""], ["", "", ""]]
board_x_can_win_bslash = [["X", "", ""], ["", "X", ""], ["", "", ""]]
board_o_can_win_slash = [["", "", ""], ["", "O", ""], ["O", "", ""]]
board_x_can_win_slash = [["", "", ""], ["", "X", ""], ["X", "", ""]]


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
    assert 1 <= morpy.play("X") <= 9


@pytest.mark.parametrize("rep", range(20))
@pytest.mark.parametrize("setup,result", [
    (any_board, [2, 3, 5, 9]),
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
    assert morpy.play("X") in result


def test_human_play_empty_board(monkeypatch):
    """Imite le joueur humain choisissant la position 5"""
    s_in = StringIO("5")
    monkeypatch.setattr("sys.stdin", s_in)
    assert morpy.play("X", is_human=True) == 5


@pytest.mark.parametrize("setup, result", [
    (any_board, 5),
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
    assert morpy.play("X", is_human=True) == result


@pytest.mark.parametrize("setup,result", [
    (any_board, "\x1b[31mX 2 3 \n\x1b[31mX 5 \x1b[32mO \n\x1b[32mO \x1b[31mX 9 \n"),
    (other_board, "\x1b[31mX \x1b[32mO 3 \n\x1b[31mX \x1b[32mO \x1b[32mO \n\x1b[32mO \x1b[31mX \x1b[31mX \n"),
    (win_board_o_hor, "\x1b[32mO \x1b[32mO \x1b[32mO \n4 5 6 \n7 8 9 \n"),
    (win_board_x_hor, "\x1b[31mX \x1b[31mX \x1b[31mX \n4 5 6 \n7 8 9 \n"),
    (win_board_o_ver, "\x1b[32mO 2 3 \n\x1b[32mO 5 6 \n\x1b[32mO 8 9 \n"),
    (win_board_x_ver, "\x1b[31mX 2 3 \n\x1b[31mX 5 6 \n\x1b[31mX 8 9 \n"),
    (win_board_o_bslash, "\x1b[32mO 2 3 \n4 \x1b[32mO 6 \n7 8 \x1b[32mO \n"),
    (win_board_x_bslash, "\x1b[31mX 2 3 \n4 \x1b[31mX 6 \n7 8 \x1b[31mX \n"),
    (win_full_board_o, "\x1b[31mX \x1b[31mX \x1b[32mO \n\x1b[31mX \x1b[32mO \x1b[31mX \n\x1b[32mO \x1b[31mX \x1b[31mX \n"),
    (win_full_board_x, "\x1b[32mO \x1b[32mO \x1b[31mX \n\x1b[32mO \x1b[31mX \x1b[32mO \n\x1b[31mX \x1b[32mO \x1b[32mO \n"),
    (draw_board, "\x1b[31mX \x1b[32mO \x1b[31mX \n\x1b[31mX \x1b[32mO \x1b[32mO \n\x1b[32mO \x1b[31mX \x1b[31mX \n"),
], indirect=["setup"])
def test_show_board(setup, result, capsys):
    """"Affiche le tableau"""
    morpy.show_board()
    assert capsys.readouterr().out == result


@pytest.mark.parametrize("setup, symbol", [
    (win_board_o_ver, "O"),
    (win_board_x_ver, "X"),
], indirect=["setup"])
def test_for_win_vert(setup, symbol):
    """Vérifie si on gagne en vertical, selon le symbole joué"""
    assert morpy.is_won_vert(symbol=symbol) is True


@pytest.mark.parametrize("setup, symbol", [
    (win_board_o_hor, "O"),
    (win_board_x_hor, "X"),
], indirect=["setup"])
def test_for_win_hor(setup, symbol):
    """Vérifie si on gagne en horizontal, selon le symbole joué"""
    assert morpy.is_won_hor(symbol=symbol) is True


@pytest.mark.parametrize("setup, symbol", [
    (win_board_o_slash, "O"),
    (win_board_x_slash, "X"),
    (win_full_board_o, "O"),
    (win_full_board_x, "X"),
], indirect=["setup"])
def test_for_win_slash(setup, symbol):
    """Vérifie si on gagne en diagonale, selon le symbole joué"""
    assert morpy.is_won_slash(symbol=symbol) is True


@pytest.mark.parametrize("setup, symbol", [
    (win_board_o_bslash, "O"),
    (win_board_x_bslash, "X"),
], indirect=["setup"])
def test_for_win_bslash(setup, symbol):
    """Vérifie si on gagne en diagonale, selon le symbole joué"""
    assert morpy.is_won_bslash(symbol=symbol) is True


@pytest.mark.parametrize("setup,symbol", [
    (win_board_o_hor, "O"),
    (win_board_x_hor, "X"),
    (win_board_o_ver, "O"),
    (win_board_x_ver, "X"),
    (win_board_o_bslash, "O"),
    (win_board_x_bslash, "X"),
    (win_board_o_slash, "O"),
    (win_board_x_slash, "X"),
    (win_full_board_o, "O"),
    (win_full_board_x, "X"),
], indirect=["setup"])
def test_for_win(setup, symbol):
    """Vérifie si le symbole joué gagne la partie en ayant joué la 1è case"""
    assert morpy.is_won(symbol=symbol) is True


@pytest.mark.parametrize("setup,result", [
    (board_x_can_win_ver, [7]),
    (board_o_can_win_ver, [7]),
    (board_x_can_win_hor, [3]),
    (board_o_can_win_hor, [3]),
    (board_x_can_win_bslash, [9]),
    (board_o_can_win_bslash, [9]),
    (board_x_can_win_slash, [3]),
    (board_o_can_win_slash, [3]),
    (draw_board, []),
    (other_board, [3]),
    (any_board, [2, 3, 5, 9])
], indirect=["setup"])
@pytest.mark.parametrize("symbol", ("O", "X"))
def test_prediction_window(setup, symbol, result):
    """Vérifie que l’IA sorte un chiffre selon les règles suivantes:
        - Si l’ordinateur peut gagner, alors il joue pour gagner;
        - Si l’ordinateur peut perdre, alors il joue pour empêcher le joueur de gagner;
        - Si personne ne peut gagner, alors il joue dans une case libre au hasard.
    """
    assert morpy.predict(symbol) == result


@pytest.mark.parametrize("setup,result", [
    (any_board, [2, 3, 5, 9]),
    (other_board, [3]),
    (win_board_o_hor, [4, 5, 6, 7, 8, 9]),
    (win_board_o_ver, [2, 3, 5, 6, 8, 9]),
    (win_board_o_bslash, [2, 3, 4, 6, 7, 8]),
    (win_board_o_slash, [1, 2, 4, 6, 8, 9]),
    (board_o_can_win_ver, [2, 3, 5, 6, 7, 8, 9]),
    (board_o_can_win_hor, [3, 4, 5, 6, 7, 8, 9]),
    (board_o_can_win_slash, [1, 2, 3, 4, 6, 8, 9]),
    (board_x_can_win_bslash, [2, 3, 4, 6, 7, 8, 9])
], indirect=["setup"])
def test_find_empties(setup, result):
    """ Vérifie que le programme trouve les cases vides.
        Ce test a été ajouté car j’ai refactoré le code en créant la fonction find_empties
        Chaque fonction créée doit être testée.
    """
    assert morpy.find_empties() == result


def test_update_empty_board():
    """Vérifie si le tableau est mis à jour"""
    morpy.update_board(symbol="X", cell=5)
    assert morpy.play_board == [["", "", ""], ["", "X", ""], ["", "", ""]]


@pytest.mark.parametrize("setup,cell,result", [
    (any_board, 5, [["X", "", ""], ["X", "X", "O"], ["O", "X", ""]]),
    (other_board, 3, [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]),
    (win_board_o_hor, 5, [["O", "O", "O"], ["", "X", ""], ["", "", ""]]),
    (win_board_o_ver, 5, [["O", "", ""], ["O", "X", ""], ["O", "", ""]]),
    (win_board_o_bslash, 3, [["O", "", "X"], ["", "O", ""], ["", "", "O"]]),
    (win_board_o_slash, 2, [["", "X", "O"], ["", "O", ""], ["O", "", ""]]),
], indirect=["setup"])
def test_update_board(setup, cell, result):
    morpy.update_board(symbol="X", cell=cell)
    assert morpy.play_board == result


@pytest.mark.parametrize("setup", [
    any_board,
    other_board,
    win_board_o_hor,
    win_board_o_ver,
    win_board_o_bslash,
    win_board_o_slash,
], indirect=["setup"])
def test_clear_board(setup):
    morpy.clear_board()
    assert morpy.play_board == [["" for _ in range(3)] for _ in range(3)]


