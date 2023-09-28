from lib.diary import Diary

"""
Initially, Diary has no entries
"""
def test_diary_is_initially_empty():
    diary = Diary()
    assert diary.all() == []