# task_manager.py

class Task:
    def __init__(self, task_id, title, description, status="pendente"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def __repr__(self):
        return (f"Task(id={self.task_id}, title='{self.title}', "
                f"description='{self.description}', status='{self.status}')")


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, title, description):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def update_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task.task_id == task_id:
                for key, value in kwargs.items():
                    if hasattr(task, key):
                        setattr(task, key, value)
                return task
        raise ValueError(f"Tarefa com id {task_id} não encontrada")

    def list_tasks(self):
        return self.tasks
    