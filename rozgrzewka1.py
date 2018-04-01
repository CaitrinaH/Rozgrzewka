#Funkcja zwracajaca sume liczb parzystych



def sum_even(a):
    even = []
    for x in a:
        if x %2 == 0:
            even.append(x)
    return sum(even)
