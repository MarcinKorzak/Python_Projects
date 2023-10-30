import random

lista = [random.randint(-10, 10) for i in range(10)]

print(f"lista: {lista}")

najmn = min(lista)
najw = max(lista)

srednia = sum(lista) / len(lista)

mniejsze = sum(1 for element in lista if element < srednia)
wieksze = sum(1 for element in lista if element > srednia)

print(f"najmniejszy element {najmn}")
print(f"najwiekszy element {najw}")
print(f"srednia {srednia}")
print(f"ile mniejszych {mniejsze}")
print(f"ile wiekszych {wieksze}")

print(f"odwrocona {lista[::-1]}")