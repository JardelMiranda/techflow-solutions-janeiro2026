class Task:
    def __init__(self, task_id, title, description, status="pendente"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.task_id} - {self.title} ({self.status})"
