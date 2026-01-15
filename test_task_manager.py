import pytest 
from src.task_manager import TaskManager


@pytest.fixture
def manager():
    return TaskManager()


def test_add_task(manager):
    manager.add_task("Estudar Python", "Testar o sistema")
    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Estudar Python"


def test_complete_task(manager):
    manager.add_task("Tarefa teste", "Descrição teste")
    manager.complete_task(0)
    assert manager.tasks[0].status == "concluída"


def test_remove_task(manager):
    manager.add_task("Remover", "Descrição")
    manager.remove_task(0)
    assert len(manager.tasks) == 0
