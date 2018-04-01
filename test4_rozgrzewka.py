#napisz funkcję, która zaszyfruje tekst szyfrem cezara



from rozgrzewka4 import cesar


def test_cesar_empty():
    text = ''
    assert cesar(text) == ''


def test_cesar_true():
    text = 'dupa'
    assert cesar(text) == 'evqb'


def test_cesar_single():
    text = 'j'
    assert cesar(text) == 'k'


def test_cesar_single_z():
    text = 'z'
    assert cesar(text) == 'a'
