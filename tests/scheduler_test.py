from main import Scheduler, Task
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_cron_match(mocker):
    return mocker.patch("main.Scheduler.cron_match")

@pytest.fixture
def mock_get_task(mocker):
    return mocker.patch("main.Task.get_task")

@pytest.fixture
def mock_thread_start(mocker):
    return mocker.patch("threading.Thread.start")

@pytest.fixture
def mock_task_1():
    task = MagicMock()
    task.name = "toto"
    task.periodicity = "0 0 13 * 5"
    task.function = lambda: print("hello")
    return task

@pytest.fixture
def mock_task_2():
    task2 = MagicMock()
    task2.name = "lala"
    task2.periodicity = "8 * * * *"
    task2.function = lambda: print("hello")
    return task2

@pytest.fixture
def mock_task_3():
    task3 = MagicMock()
    task3.name = "rihanna"
    task3.periodicity = "8 * * * *"
    task3.function = lambda: print("hello")
    return task3

def test_init_scheduler():
    s = Scheduler()
    assert s.planned_tasks == []

def test_init_task():
    t = Task("toto", "0 0 13 * 5", lambda x: print(f"Salut {x}"))

    assert t.name == "toto"
    assert t.periodicity == "0 0 13 * 5"
    assert t.function is not None

def test_get_task():
    #Arrange
    t = Task("toto", "0 0 13 * 5", lambda x: print(f"Salut {x}"))

    # Act
    result = t.get_task()

    # Assert
    assert result == "La tâche toto avec une périodicité de 0 0 13 * 5"

def test_get_planned_tasks(mock_task_1, mock_task_2):
    # Arrange
    s = Scheduler()
    s.planned_tasks = [mock_task_1, mock_task_2]

    # Act
    result = s.get_planned_tasks()

    # Assert
    assert result == "Les tâches plannifiées sont toto, lala"


def test_set_task(mock_task_1):
    # Arrange
    s = Scheduler()
    mock_task_1.get_task.return_value = "La tâche toto avec une périodicité de 0 0 13 * 5"

    # Act
    result = s.set_task(mock_task_1)
    planned = s.get_planned_tasks()

    # Assert
    assert result == "La tâche toto avec une périodicité de 0 0 13 * 5"
    assert planned == "Les tâches plannifiées sont toto"

def test_delete_task(mock_task_1, mock_task_2, mock_task_3):
    # Arrange
    s = Scheduler()
    s.planned_tasks = [mock_task_1, mock_task_2, mock_task_3]

    # Act
    result = s.delete_task("rihanna")
    planned = s.get_planned_tasks()

    # Assert
    assert result == "La tâche rihanna a été supprimée"
    assert planned == "Les tâches plannifiées sont toto, lala"


def test_delete_task_unknown_task(mock_task_1, mock_task_2, mock_task_3):
    # Arrange
    s = Scheduler()
    s.planned_tasks = [mock_task_1, mock_task_2, mock_task_3]

    # Act
    result = s.delete_task("madonna")
    planned = s.get_planned_tasks()

    # Assert
    assert result == "La tâche madonna n'existe pas"
    assert planned == "Les tâches plannifiées sont toto, lala, rihanna"


def test_cron_match():
    # Arrange
    minute = 12
    task_minute = 12

    # Act
    s = Scheduler()
    result = s.cron_match(minute, task_minute)

    # Assert
    assert result == True


def test_cron_match_not_match():
    # Arrange
    minute = 12
    task_minute = 15

    # Act
    s = Scheduler()
    result = s.cron_match(minute, task_minute)

    # Assert
    assert result == False


def test_cron_match_all():
    # Arrange
    minute = 12
    task_minute = "*"

    # Act
    s = Scheduler()
    result = s.cron_match(minute, task_minute)

    # Assert
    assert result == True


def test_update(mock_cron_match, mock_task_1, mock_task_2, mock_task_3, mock_thread_start):
    # Arrange
    s = Scheduler()
    s.planned_tasks = [mock_task_1, mock_task_2, mock_task_3]
    mock_cron_match.side_effects = [True, True, True, True, True]
    mock_task_1.return_value = True
    mock_task_2.return_value = True
    mock_task_3.return_value = True

    # Act
    s.update()

    # Assert
    assert mock_cron_match.call_count == 15
    assert mock_thread_start.call_count == 3


def test_update_no_task(mock_cron_match, mock_thread_start):
    # Arrange
    s = Scheduler()
    s.planned_tasks = []

    # Act
    s.update()

    # Assert
    assert mock_cron_match.call_count == 0
    assert mock_thread_start.call_count == 0