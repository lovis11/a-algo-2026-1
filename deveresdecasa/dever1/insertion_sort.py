#OBS: Teste no terminal : python insertion_sort.py
import random
import time

# Implementação do algoritmo Insertion Sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        # Move os elementos maiores que a chave
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista


# tamanhos das listas a serem testadas
tamanhos = [1000, 5000, 10000, 20000, 50000]


for n in tamanhos:

    # gera lista aleatória
    lista = [random.randint(0, 100000) for _ in range(n)]

    lista_insertion = lista.copy()
    lista_sorted = lista.copy()

    # mede tempo do insertion sort
    inicio = time.time()
    insertion_sort(lista_insertion)
    fim = time.time()

    tempo_insertion = fim - inicio

    # mede tempo do sorted()
    inicio = time.time()
    sorted(lista_sorted)
    fim = time.time()

    tempo_sorted = fim - inicio

    print("\nTamanho da lista:", n)
    print("Tempo Insertion Sort:", tempo_insertion, "segundos")
    print("Tempo sorted() Python:", tempo_sorted, "segundos")
    print("---------------------------------------")
