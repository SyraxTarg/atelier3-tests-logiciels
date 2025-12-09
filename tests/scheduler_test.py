from main import Scheduler, Task

def test_init_scheduler():
    s = Scheduler()
    assert s.running_tasks == []

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