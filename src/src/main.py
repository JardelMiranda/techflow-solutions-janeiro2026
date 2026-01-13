from task_manager import TaskManager

manager = TaskManager()

manager.create_task("Estudar Git", "Revisar commits e push")
manager.create_task("Criar Kanban", "Organizar tarefas no GitHub")

tasks = manager.list_tasks()
for task in tasks:
    print(task)
