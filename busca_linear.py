numeros = input("Digite os números separados por espaço: ")
lista_numeros = [int(num) for num in numeros.split()]

busca = int(input("Digite o número que deseja buscar: "))

encontrado = False
for num in lista_numeros:
    if num == busca:
        encontrado = True
        break

if encontrado:
    print(f"O número {busca} está presente na lista.")
else:
    print(f"O número {busca} não está presente na lista.")
    