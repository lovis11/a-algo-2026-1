def F(n):
    """
    Calcula a recorrência:
    F(n) = 2F(n-1) + n^2
    com F(1) = 2
    """
    if n == 1:
        return 2
    return 2 * F(n - 1) + n**2


def main():
    n = int(input("Digite um valor inteiro positivo para n: "))

    if n < 1:
        print("Erro: n deve ser maior ou igual a 1.")
        return

    resultado = F(n)
    print(f"F({n}) = {resultado}")


if __name__ == "__main__":
    main()
