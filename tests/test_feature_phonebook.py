from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.phone_number_extractor import PhoneNumberExtractor

"""
When I add multiple diary entries
and I call PhoneNumberExtractor#extrack
I get a list of phone numbers from all diary contents
"""
def test_extracts_phone_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("My Tile 1", "My friend is 07800000000 and 07800000001")
    entry_2 = DiaryEntry("My Tile 2", "My Contents 2")
    entry_3 = DiaryEntry("My Tile 3", "My friend is 07800000002")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == {"07800000000", "07800000001", "07800000002"}

"""
When I add a diary entries
and I call PhoneNumberExtractor#extrack
It ignores invalid phone numbers
"""
def test_ignores_invalid_phone_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("My Tile 1", "My friend is 078000000000 and 0780000000 and 0780")
    diary.add(entry_1)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == set()