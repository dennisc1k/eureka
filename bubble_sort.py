def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

numeros = input("Digite os números separados por espaço: ")
lista_numeros = [int(num) for num in numeros.split()]

bubble_sort(lista_numeros)

print("Números ordenados:", lista_numeros)
# Fim do arquivo bubble_sort.py