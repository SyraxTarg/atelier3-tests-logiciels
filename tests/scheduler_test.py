from main import Scheduler

def test_init_scheduler():
    s = Scheduler()
    assert s.ruuning_tasks == []