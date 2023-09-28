from lib.task_list import TaskList
from lib.task import Task

"""
When I add multiple tasks
And I don't mark any complete
#all_incomplete lists them out in the order they were added
"""
def test_adds_and_lists_incomplete_tasks():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_3 = Task("Walk the frog")
    task_list.add(task_1)
    task_list.add(task_2)
    task_list.add(task_3)
    assert task_list.all_incomplete() == [task_1, task_2, task_3]

"""
When I add multiple tasks
And I mark one as complete
#all_incomplete only lists the incomplete tasks
"""
def test_marking_tasks_as_complete_then_removes_from_incomplete_list():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_3= Task("Walk the frog")
    task_list.add(task_1)
    task_list.add(task_2)
    task_list.add(task_3)
    task_2.mark_complete()
    assert task_list.all_incomplete() == [task_1, task_3]

"""
When I add multiple tasks
And I mark one as complete
#all_incomplete only lists the complete tasks
"""
def test_marking_tasks_as_complete_then_present_in_complete_list():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Walk the cat")
    task_3 = Task("Walk the frog")
    task_list.add(task_1)
    task_list.add(task_2)
    task_list.add(task_3)
    task_2.mark_complete()
    assert task_list.all_complete() == [task_2]