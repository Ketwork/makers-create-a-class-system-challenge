class TaskList():
    def __init__(self):
        self._tasks = []

    def add(self, task):
        self._tasks.append(task)
    
    def all_incomplete(self):
        return [
            task for task in self._tasks
            if not task.complete
        ]

    def all_complete(self):
        return [
            task for task in self._tasks
            if task.complete
        ]