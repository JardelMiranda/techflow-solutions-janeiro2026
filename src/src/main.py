from task_manager import TaskManager

manager = TaskManager()

task1 = manager.create_task("Estudar Git", "Revisar commits e push")
task2 = manager.create_task("Criar Kanban", "Organizar tarefas no GitHub")

print(task1)
print(task2)
