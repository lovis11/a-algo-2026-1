def eh_palindromo(arr, inicio, fim):
    # Caso base
    if inicio >= fim:
        return True
    
    # Se os elementos forem diferentes
    if arr[inicio] != arr[fim]:
        return False
    
    # Chamada recursiva
    return eh_palindromo(arr, inicio + 1, fim - 1)


# Testes
array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "a"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"]

print("array1:", eh_palindromo(array1, 0, len(array1) - 1))
print("array2:", eh_palindromo(array2, 0, len(array2) - 1))
print("array3:", eh_palindromo(array3, 0, len(array3) - 1))
print("array4:", eh_palindromo(array4, 0, len(array4) - 1))
