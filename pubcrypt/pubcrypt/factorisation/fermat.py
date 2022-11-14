from math import floor, sqrt

def fermat_factorization(n):
    k = floor(sqrt(n))
    y = pow(k, 2) - n
    d = 1
    
    while True:
        if floor(sqrt(y)) == sqrt(y):
            break

        else:
            y = y+2*k+d
            d += 2

        if floor(sqrt(y)) >= n/2:
            raise ValueError("No factor found")

    x = sqrt(n+y)
    y = sqrt(y)

    return x-y, x+y