import morpy


def test_computer_plays():
    """ Doit retourner un chiffre entre 1 et 9"""
    assert 1 <= morpy.play() <= 9
