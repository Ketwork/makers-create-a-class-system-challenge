from lib.diary_entry import DiaryEntry

"""
DiaryEntry is constucted with a title and contents
"""
def test_diary_entry_contructs():
    entry = DiaryEntry("My Title", "My Contents")
    assert entry.title == "My Title"
    assert entry.contents == "My Contents"