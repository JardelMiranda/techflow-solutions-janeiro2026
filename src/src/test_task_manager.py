from src.task_manager import TaskManager

def test_create_task():
    manager = TaskManager()
    task = manager.create_task("Teste", "Descrição")
    assert task.title == "Teste"
    assert task.status == "pendente"

def test_list_tasks():
    manager = TaskManager()
    manager.create_task("T1", "Desc 1")
    manager.create_task("T2", "Desc 2")
    tasks = manager.list_tasks()
    assert len(tasks) == 2

def test_update_task():
    manager = TaskManager()
    task = manager.create_task("Antigo", "Desc")
    manager.update_task(task.task_id, title="Novo", status="concluída")
    assert task.title == "Novo"
    assert task.status == "concluída"

def test_delete_task():
    manager = TaskManager()
    task = manager.create_task("Excluir", "Desc")
    result = manager.delete_task(task.task_id)
    assert result is True
    assert len(manager.list_tasks()) == 0
