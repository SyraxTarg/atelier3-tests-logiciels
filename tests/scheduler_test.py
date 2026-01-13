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
    task = Task("toto", "0 0 13 * 5", lambda x: print(f"Salut {x}"))
    result = s.set_task(task)
    planned = s.get_planned_tasks()

    # Assert
    assert result == "La tâche toto avec une périodicité de 0 0 13 * 5"
    assert planned == "Les tâches plannifiées sont toto"

def test_delete_task():
    # Arrange
    s = Scheduler()
    task = Task("toto", "0 0 13 * 5", lambda x: print(f"Salut {x}"))
    task2 = Task("lala", "0 0 13 * 5", lambda x: print(f"Salut {x}"))
    task3 = Task("rihanna", "0 0 13 * 5", lambda x: print(f"Salut {x}"))
    s.set_task(task)
    s.set_task(task2)
    s.set_task(task3)

    # Act
    result = s.delete_task("rihanna")
    planned = s.get_planned_tasks()

    # Assert
    assert result == "La tâche rihanna a été supprimée"
    assert planned == "Les tâches plannifiées sont toto, lala"


def test_delete_task_unknown_task():
    # Arrange
    s = Scheduler()
    task = Task("toto", "0 0 13 * 5", lambda x: print(f"Salut {x}"))
    task2 = Task("lala", "0 0 13 * 5", lambda x: print(f"Salut {x}"))
    task3 = Task("rihanna", "0 0 13 * 5", lambda x: print(f"Salut {x}"))
    s.set_task(task)
    s.set_task(task2)
    s.set_task(task3)

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
    
    
    
    