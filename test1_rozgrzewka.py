#Napisz funkcje zwracajaca sume: liczb parzystych

from rozgrzewka1 import sum_even


def test_only_even_numbers():
    assert sum_even([-20,2,4,26]) == -20+2+4+26


def test_odd_and_even_numbers():
    assert sum_even([4,5,7,8,9]) == 4+8


def test_only_odd_numbers():
    assert sum_even([5,9,11,35,23]) == 0


def test_empty_list():
    assert sum_even([]) == 0
