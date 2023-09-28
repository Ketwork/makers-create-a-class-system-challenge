from lib.task import Task
"""
Task constructs with a title
"""
def test_task_contructs():
    task = Task("Walk the dog")
    assert task.title == "Walk the dog"

"""
Newly constucted tasks are not complete
"""
def test_task_contructs_ioncomplete_tasks():
    task = Task("Walk the dog")
    assert task.complete == False

"""
When i mark a task as complete
It is reflected in the complete property
"""
def test_marks_tasks_as_complete():
    task = Task("Walk the dog")
    task.mark_complete()
    assert task.complete == True