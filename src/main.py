from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n=== TechFlow Solutions ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição (opcional): ")
            manager.add_task(titulo, descricao)
            print("Tarefa adicionada!")
        elif escolha == "2":
            print("\n--- Lista de Tarefas ---")
            manager.list_tasks()
        elif escolha == "3":
            manager.list_tasks()
            indice = int(input("Número da tarefa a concluir: ")) - 1
            manager.complete_task(indice)
        elif escolha == "4":
            manager.list_tasks()
            indice = int(input("Número da tarefa a remover: ")) - 1
            manager.remove_task(indice)
        elif escolha == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
