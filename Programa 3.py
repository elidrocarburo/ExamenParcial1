import random
import time

def generar_lista(n):
    return [random.randint(1, 500) for _ in range(n)]

def busqueda_lineal(lista, objetivo):
    for i, num in enumerate(lista):
        if num == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

n = 500
lista_aleatoria = generar_lista(n)
lista_ordenada = sorted(lista_aleatoria) 

numero = int(input("Ingrese el número a buscar: "))

inicio_lineal = time.time()
indice_1 = busqueda_lineal(lista_aleatoria, numero)
fin_lineal = time.time()

inicio_binaria = time.time()
indice_2 = busqueda_binaria(lista_ordenada, numero)
fin_binaria = time.time()

print("Lista aleatoria:", lista_aleatoria)
print("Lista ordenada:", lista_ordenada)

print(f"Tiempo de búsqueda lineal: {fin_lineal - inicio_lineal:.6} segundos")
print(f"Tiempo de búsqueda binaria: {fin_binaria - inicio_binaria:.6f} segundos")

if indice_1 != -1:
    print(f"El número {numero} se encontró en el índice {indice_1} usando búsqueda lineal.")
else:
    print(f"El número {numero} no se encontró en la lista usando búsqueda lineal.")

if indice_2 != -1:
    print(f"El número {numero} se encontró en el índice {indice_2} usando búsqueda binaria.")
else:
    print(f"El número {numero} no se encontró en la lista usando búsqueda binaria.")