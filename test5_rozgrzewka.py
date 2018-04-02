#Napisz funkcje zwracajaca  N-ta liczba Fibonacciego.


from rozgrzewka5 import fibo


def test_fibo_zero():
    assert fibo(0) == 0


def test_fibo_one():
    assert fibo(1) == 1


def test_fibo_5():
    assert fibo(5) == 5


def test_fibo_18():
    assert fibo(18) == 2584

def test_fibo_minus():
    assert fibo(-5) == 0


def test_fibo_400():
    assert fibo(400) > 102334155
