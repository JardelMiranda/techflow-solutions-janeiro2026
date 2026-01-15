class Task:
    def __init__(self, task_id, title, description, status="pendente"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def __repr__(self):
        return (f"Task(id={self.task_id}, title='{self.title}', "
                f"description='{self.description}', status='{self.status}')")