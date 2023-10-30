import random

a = int(input("Podaj wartość a: "))
b = int(input("Podaj wartość b: "))
n = int(input("Podaj wielkość n: "))

macierz = [[random.randint(a, b) for i in range(n)] for i in range(n)]

print("Pierwotna macierz:")
for wiersz in macierz:
    print(wiersz)

suma_przekatnej1 = sum(macierz[i][i] for i in range(n))
suma_przekatnej2 = sum(macierz[i][n - 1 - i] for i in range(n))

suma_elementow_nieparzystych = sum(sum(wiersz[i] for i in range(n) if i % 2 == 1) for wiersz in macierz if macierz.index(wiersz) % 2 == 1)

macierz = [wiersz[::-1] for wiersz in macierz]

print("Zmodyfikowana macierz:")
for wiersz in macierz:
    print(wiersz)

print("Suma przekątnej 1:", suma_przekatnej1)
print("Suma przekątnej 2:", suma_przekatnej2)
print("Suma elementów o nieparzystych indeksach w listach o nieparzystych indeksach:", suma_elementow_nieparzystych)