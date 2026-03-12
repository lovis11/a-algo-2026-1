#OBS : O algoritmo executa uma chamada recursiva para cada valor até chegar a 1.
# o tempo cresce linearmente com o tamanho da entrada.

import time
import sys

# aumenta limite de recursão para evitar erro em n grande
sys.setrecursionlimit(2000)


# função recursiva para calcular o fatorial
def fatorial(n):
    
    # caso base
    if n == 0 or n == 1:
        return 1

    # chamada recursiva
    return n * fatorial(n - 1)


# valores que serão testados
valores = [10, 100, 500, 1000]


for n in valores:

    inicio = time.time()

    resultado = fatorial(n)

    fim = time.time()

    tempo_execucao = fim - inicio

    print("\nValor de n:", n)
    print("Tempo de execução:", tempo_execucao, "segundos")
