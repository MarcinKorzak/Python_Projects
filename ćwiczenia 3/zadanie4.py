import math

a = int(input("Podaj wartość a: "))
b = int(input("Podaj wartość b: "))

lista_nieparzystych = []

for liczba in range(a, b + 1):
    if liczba % 2 != 0:
        lista_nieparzystych.append(liczba)

lista_krotek = []

print(lista_nieparzystych)

for liczba in lista_nieparzystych:
    potega = liczba ** 2
    pierwiastek = math.sqrt(liczba)
    lista_krotek.append((liczba, potega, pierwiastek))

print("zmodyfikowana:")
print(lista_krotek)
