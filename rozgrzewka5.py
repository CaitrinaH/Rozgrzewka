#Napisz funkcje zwracajace N-ta liczbe Fibonacciego.



def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        fibo_n_minus_1 = 1
        fibo_n_minus_2 = 0
        for i in range(n-1):
            fibo_n = fibo_n_minus_1 + fibo_n_minus_2
            fibo_n_minus_2 = fibo_n_minus_1
            fibo_n_minus_1 = fibo_n
        return fibo_n
    if n < 0:
        return 0 
