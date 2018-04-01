#Fukcja zwracajaca, czy z podanych bokow powstanie trojkat


def is_valid_triangle(a, b, c):
    if a + b >= c and b + c >= a and a + c >= b:
        return True
    return False
