from task_manager import TaskManager

manager = TaskManager()

t1 = manager.create_task("Estudar Git", "Revisar commits")
manager.create_task("Criar Kanban", "Organizar tarefas")

manager.update_task(t1.task_id, status="concluída")

for task in manager.list_tasks():
    print(task)
