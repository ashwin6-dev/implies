from core import instance, relationship

@instance.Instance("AUTHOR")
class Dave:
    def __init__(self):
        self.name = "dave"
        self.books = 10

@instance.Instance("BOOK")
class BookOne:
    def __init__(self):
        self.name = "bookone"
        self.age = 50

@relationship.Relationship("AUTHOR", "BOOK")
class Writes:
    def __init__(self, time):
        self.time = 100

r = Writes(BookOne, Dave)(time=100)
print (r.get_props())