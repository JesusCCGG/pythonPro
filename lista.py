numeros = [3, 5, 4, 8, 14, 9, 26]
num_max = numeros[0]   # asumimos que el primer elemento es el máximo
print("Longitud", len(numeros))
for num in numeros:
    if num > num_max:
        num_max = num
print("El número más grande es:", num_max)