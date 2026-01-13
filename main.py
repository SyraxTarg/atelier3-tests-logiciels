import datetime

class Task:
    def __init__(self, name: str, periodicity: str, function):
        self.name = name
        self.periodicity = periodicity
        self.minute, self.hour, self.day, self.month, self.weekday = periodicity.split()
        self.function = function
        self.last_run = None

    def get_task(self):
        return f"La tâche {self.name} avec une périodicité de {self.minute} {self.hour} {self.day} {self.month} {self.weekday}"

class Scheduler():

    def __init__(self):
        self.planned_tasks: list[Task] = []

    def get_planned_tasks(self)->str:
        planned = []
        for task in self.planned_tasks:
            planned.append(task.name)
        return f"Les tâches plannifiées sont {', '.join(planned)}"

    def set_task(self, task: Task)->str:
        self.planned_tasks.append(task)
        return task.get_task()

    def delete_task(self, name:str)->str:
        for task in self.planned_tasks:
            if task.name == name:
                self.planned_tasks.remove(task)
                return f"La tâche {name} a été supprimée"

        return f"La tâche {name} n'existe pas"


    def cron_match(self, value, cron_field):
        if cron_field == "*":
            return True
        return int(value) == int(cron_field)


    def update(self):
        now = datetime.datetime.now()

        for task in self.planned_tasks:
            if not self.cron_match(now.minute, task.minute):
                continue
            if not self.cron_match(now.hour, task.hour):
                continue
            if not self.cron_match(now.day, task.day):
                continue
            if not self.cron_match(now.month, task.month):
                continue
            if not self.cron_match(now.weekday(), task.weekday):
                continue

            if task.last_run == (now.year, now.month, now.day, now.hour, now.minute):
                continue

            task.function()
            task.last_run = (now.year, now.month, now.day, now.hour, now.minute)
