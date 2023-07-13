import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smaller = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(smaller) + [pivot] + quicksort(greater)

# Generar un arreglo de 200 números aleatorios del 1 al 10
#arreglo = [random.randint(1, 10) for _ in range(2000)]
#Sin repeticion
arreglo = random.sample(range(1, 201), 200)

# Imprimir el arreglo original
print("Arreglo original:", arreglo)

# Ordenar el arreglo utilizando Quicksort y medir el tiempo de ejecución
start_time = time.time()
arreglo_ordenado = quicksort(arreglo)
end_time = time.time()

# Imprimir el arreglo ordenado y el tiempo de ejecución
print("Arreglo ordenado:", arreglo_ordenado)
print("Tiempo de ejecución:", end_time - start_time, "segundos")
