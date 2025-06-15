from core import instance, relationship, ontology

spec = ontology.OntologySpec()

@ontology.Ontology(spec)
@instance.Instance("AUTHOR")
class Dave:
    def __init__(self):
        self.name = "dave"
        self.books = 10

@ontology.Ontology(spec)
@instance.Instance("BOOK")
class BookOne:
    def __init__(self):
        self.name = "bookone"
        self.successful = False

@ontology.Ontology(spec)
@instance.Instance("BOOK")
class BookTwo:
    def __init__(self):
        self.name = "booktwo"
        self.successful = True

@ontology.Ontology(spec)
@relationship.Relationship("AUTHOR", "BOOK")
class Writes:
    def __init__(self, time):
        self.time = time

Writes(Dave, BookOne)(time=100)
print (spec.instances, spec.relationships, spec.relationship_types)