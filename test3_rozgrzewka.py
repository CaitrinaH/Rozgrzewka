#Napisz funkcję, która zanonimizuj  podany string poprzez zamianę wszystkich liter poza pierwszą i ostatnią na gwiazdki


from rozgrzewka3 import anonymize_text
    


def test_two_characters_in_string():
    assert anonymize_text('kh') == 'kh'


def test_one_character_in_string():
    assert anonymize_text('j') == 'j'


def test_string():
    assert anonymize_text('chuj') == 'c**j'


def test_space_between_characters():
    assert anonymize_text('jebac jave') == 'j********e'



