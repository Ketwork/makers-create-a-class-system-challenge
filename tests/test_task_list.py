from lib.task_list import TaskList

"""
Initially, TaskList has no incomplete tasks
"""
def test_task_list_incomplete_is_initially_empty():
    taskList = TaskList()
    assert taskList.all_incomplete() == []

"""
Initially, TaskList has no complete tasks
"""
def test_task_list_complete_is_initially_empty():
    taskList = TaskList()
    assert taskList.all_complete() == []