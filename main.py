class Task():

    def __init__(self, name: str, periodicity: str, function):
        self.name = name
        self.periodicity = periodicity
        self.function = function

    def get_task(self):
        return f"La tâche {self.name} avec une périodicité de {self.periodicity}"

class Scheduler():

    def __init__(self):
        self.running_tasks = []