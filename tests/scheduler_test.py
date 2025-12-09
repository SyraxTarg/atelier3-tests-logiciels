from main import Scheduler, Task

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

def test_get_planned_tasks():
    # Arrange
    s = Scheduler()
    t1 = Task("yoyo", "0 0 23 * 4", lambda x: print(f"Salut {x}"))
    t2 = Task("toto", "0 0 13 * 5", lambda x: print(f"Salut {x}"))
    s.planned_tasks = [t1, t2]

    # Act
    result = s.get_planned_tasks()

    # Assert
    assert result == "Les tâches plannifiées sont yoyo, toto"


def test_set_task():
    # Arrange
    s = Scheduler()

    # Act
    result = s.setTask("toto", "0 0 13 * 5", lambda x: print(f"Salut {x}"))
    planned = s.get_planned_tasks()

    # Assert
    assert result == "La tâche toto avec une périodicité de 0 0 13 * 5"
    assert planned == "Les tâches plannifiées sont toto"