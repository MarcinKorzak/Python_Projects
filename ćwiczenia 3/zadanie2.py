import random

lista = [random.randint(1,10) for i in range(20)]
print(lista)

licznik = {}

for liczba in lista:
    if liczba in licznik:
        licznik[liczba] += 1
    else:
        licznik[liczba] = 1

for liczba, ilosc in licznik.items():
    print(f"Liczba {liczba} występuje {ilosc} razy")