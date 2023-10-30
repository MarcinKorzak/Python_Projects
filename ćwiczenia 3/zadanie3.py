import random

macierz = [[random.randint(-5, 5) for i in range(5)] for i in range(5)]

for wiersz in macierz:
    print(wiersz)

minima = [float('inf')] * 5
maxima = [float('-inf')] * 5

for wiersz in macierz:
    for i in range(5):
        element = wiersz[i]
        if element < minima[i]:
            minima[i] = element
        if element > maxima[i]:
            maxima[i] = element

print("\nMinima")
for i in range(5):
    print(f"Kolumna {i + 1}: {minima[i]}")

print("\nMaxima")
for i in range(5):
    print(f"Kolumna {i + 1}: {maxima[i]}")
    