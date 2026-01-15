from src.task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description):
        task = Task(
            task_id=self.next_id,
            title=title,
            description=description
        )
        self.tasks.append(task)
        self.next_id += 1

    def complete_task(self, index):
        try:
            self.tasks[index].status = "concluída"
        except IndexError:
            print("Número inválido!")

    def remove_task(self, index):
        try:
            self.tasks.pop(index)
        except IndexError:
            print("Número inválido!")