from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, title, description):
        task = Task(
            task_id=self.next_id,
            title=title,
            description=description
        )
        self.tasks.append(task)
        self.next_id += 1
        return task
        def list_tasks(self):
        return self.tasks


