import math

n = int(input("Podaj dodatnią liczbę naturalną n: "))

macierz = [["" for i in range(n)] for i in range(n)]

def czy_wzglednie_pierwsze(a, b):
    return math.gcd(a, b) == 1

for i in range(n):
    for j in range(n):
        if czy_wzglednie_pierwsze(i + 1, j + 1):
            macierz[i][j] = "+"
        else:
            macierz[i][j] = "."

print("Utworzona macierz:")
for wiersz in macierz:
    print(" ".join(wiersz))