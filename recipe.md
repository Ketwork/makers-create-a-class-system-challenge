# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```


_Also design the interface of each class in more detail._

```python

class Dairy:
    def add(self, diary_entry):
        # diary_entry: instance of DiaryEntry
        # returns nothin
        # Side-effects: adds to list of dairy entries
        pass 

    def all(self):
        # returns a list of DiaryEntries
        pass 


class DiaryEntry():
    # Public properties:
    #   title: string
    #   contents: string

    def __init__(self, title, contents):
        pass 

class TaskList():
    def add(self, task):
        pass
    
    def all_incomplete(self):
        pass

    def all_complete(self):
        pass

class Task():
    # Public properties:
    #   title: string representing a job to do

    def __init__(self, title):
        #title: string
        pass 

    def mark_complete():
        pass

class PhoneNumberExtractor():
    def __init__(self, diary):
        #title: string
        pass

    def extract(self):
        pass

class ReadableEntryExtractor():
    def __init__(self, diary):
        #diary: an instance of Diary
        pass

    def extract(self, wpm, minutes):
        # wpm: integer
        # minutes: integer
        pass

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# Diary
"""
When I add multiple diary entries
#all lists them out in the order they were added
"""
diary = Diary()
entry_1 = DiaryEntry("My Tile 1", "My Contents 1")
entry_2 = DiaryEntry("My Tile 2", "My Contents 2")
entry_3 = DiaryEntry("My Tile 3", "My Contents 3")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
diary.all() # => [entry_1, entry_2, entry_3]

"""
When I add multiple tasks
And I don't mark any complete
#all_incomplete lists them out in the order they were added
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the frog")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_list.all_incomplete() # => [task_1, task_2, task_3]

"""
When I add multiple tasks
And I mark one as complete
#all_incomplete only lists the incomplete tasks
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the frog")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_2.mark_complete()
task_list.all_incomplete() # => [task_1, task_3]

"""
When I add multiple tasks
And I mark one as complete
#all_incomplete only lists the complete tasks
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Walk the cat")
task_3 = Task("Walk the frog")
task_list.add(task_1)
task_list.add(task_2)
task_list.add(task_3)
task_2.mark_complete()
task_list.all_complete() # => [task_2]


"""
When I add multiple diary entries
and I call PhoneNumberExtractor#extrack
I get a list of phone numbers from all diary contents
"""
diary = Diary()
entry_1 = DiaryEntry("My Tile 1", "My friend is 07800000000 and 07800000001")
entry_2 = DiaryEntry("My Tile 2", "My Contents 2")
entry_3 = DiaryEntry("My Tile 3", "My friend is 07800000002")
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => ["07800000000", "07800000001", "07800000002"]

"""
When I add a diary entries
and I call PhoneNumberExtractor#extrack
It ignores non-valid phone numbers
"""
diary = Diary()
entry_1 = DiaryEntry("My Tile 1", "My friend is 078000000000 and 0780000000 and 0780")
diary.add(entry_1)
extractor = PhoneNumberExtractor(diary)
extractor.extract() # => []

"""
When I add one diary entry that fits in the time
and I call ReadableEntryExtractor#extrack
with a wpm of 2 and a minutes of 2
it gets that diary entry
"""
diary = Diary()
entry_1 = DiaryEntry("My Tile 1", "one two three four")
diary.add(entry_1)
extractor = ReadableEntryExtractor(diary)
extractor.extract(2, 2) # => entry_1


```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

# Diary
"""
Initially, Diary has no entries
"""
diary = Diary()
diary.all() # => []

# DiaryEntry
"""
DiaryEntry is constucted with a title and contents
"""
entry = DiaryEntry("My Title", "My Contents")
entry.title # => "My Title"
entry.contents # => "My contents"

# TaskList
"""
Initially, TaskList has no incomplete tasks
"""
taskList = TaskList()
taskList.all_incomplete() # => []

"""
Initially, TaskList has no complete tasks
"""
taskList = TaskList()
taskList.all_complete() # => []

# Task
"""
Task constructs with a title
"""
task= Task("Walk the dog")
task.title # => "Walk the dog")


```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fmulti_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
