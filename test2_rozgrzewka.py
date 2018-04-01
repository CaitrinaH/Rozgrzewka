#napisz funkcję, która dostaje długości boków trójkąta i zwraca czy faktycznie można z nich zbudować trójkąt



from rozgrzewka2 import is_valid_triangle

def test_all_edges_equal():
    assert is_valid_triangle(a=6, b=6, c=6) == True


def test_two_edges_equal():
    assert is_valid_triangle(a=6, b=6, c=10) == True


def test_all_edges_different():
    assert is_valid_triangle(a=5, b=7, c=10) == True


def test_all_edges_different_second_edge_longer():
    assert is_valid_triangle(a=7, b=10, c=5) == True


def test_all_edges_different_first_edge_longer():
    assert is_valid_triangle(a=10, b=7, c=5) == True


def test_third_edge_longer():
    assert is_valid_triangle(a=5, b=5, c=11) == False


def test_second_edge_longer():
    assert is_valid_triangle(a=5, b=11, c=5) == False


def test_first_edge_longer():
    assert is_valid_triangle(a=11, b=5, c=5) == False


def test_inequal_triangle():
    assert is_valid_triangle(a=11, b=5, c=6) == True   
     
