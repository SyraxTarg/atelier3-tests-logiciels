from main import Scheduler

def test_init_scheduler():
    s = Scheduler()
    assert s.running_tasks == []