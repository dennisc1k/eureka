tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def remover_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa para remover: ")) - 1
        if 0 <= indice < len(tarefas):
            removida = tarefas.pop(indice)
            print(f"Tarefa '{removida}' removida!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Digite um número válido.")

def listar_tarefas():
    print("\n--- Lista de Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def menu():
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Listar tarefas")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            remover_tarefa()
        elif opcao == "3":
            listar_tarefas()
        elif opcao == "4":
            print("Saindo do gerenciador de tarefas.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
