class Task():

    def __init__(self, name: str, periodicity: str, function):
        self.name = name
        self.periodicity = periodicity
        self.function = function

    def get_task(self):
        return f"La tâche {self.name} avec une périodicité de {self.periodicity}"

class Scheduler():

    def __init__(self):
        self.planned_tasks: list[Task] = []

    def get_planned_tasks(self)->str:
        planned = []
        for task in self.planned_tasks:
            planned.append(task.name)
        return f"Les tâches plannifiées sont {', '.join(planned)}"

    def set_task(self, name: str, periodicity: str, function)->str:
        task = Task(name, periodicity, function)
        self.planned_tasks.append(task)
        return task.get_task()

    def delete_task(self, name:str)->str:
        for task in self.planned_tasks:
            if task.name == name:
                self.planned_tasks.remove(task)
                return f"La tâche {name} a été supprimée"