from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.readable_entry_extractor import ReadableEntryExtractor

"""
When I add one diary entry that fits in the time
and I call ReadableEntryExtractor#extrack
with a wpm of 2 and a minutes of 2
it gets that diary entry
"""
def test_gets_single_entry_that_fits_in_the_time():
    diary = Diary()
    entry_1 = DiaryEntry("My Tile 1", "one two three four")
    diary.add(entry_1)
    extractor = ReadableEntryExtractor(diary)
    assert extractor.extract(2, 2) == entry_1

"""
When I add muktiple diary entries, multiple readable
and I call ReadableEntryExtractor#extrack
with a wpm of 2 and a minutes of 2
It returns the longest reaable one
"""
def test_gets_longest_readable():
    diary = Diary()
    entry_1 = DiaryEntry("My Tile 1", "one two three four")
    entry_2 = DiaryEntry("My Tile 1", "one two three")
    entry_3 = DiaryEntry("My Tile 1", "one two three four five six seven")
    entry_4 = DiaryEntry("My Tile 1", "one two three four five")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    extractor = ReadableEntryExtractor(diary)
    assert extractor.extract(wpm=2, minutes=3) == entry_4

"""
When I add one no entries
and I call ReadableEntryExtractor#extrack
it returns None
"""
def test_with_no_entries_returns_None():
    diary = Diary()
    extractor = ReadableEntryExtractor(diary)
    assert extractor.extract(2, 2) == None