def gcd(a, b):
    # zwraca a i b na podstawie algorytmu euklidesa
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    # zwraca wartość odwrotną do a%m gdzie  a*x % m = 1

    if gcd(a, m) != 1:
        return None # jeżeli a%m nie jest względnie pierwsza, nie rób nic

    # obliczenie na podstawie rozszerzonego algorytmu euklidesa
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # 
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
