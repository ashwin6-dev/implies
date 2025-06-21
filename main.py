from implies.core.entity import EntityType
from implies.core.knowledge_graph import Graph
from implies.core.relationship import RelationshipSchema

G = Graph()

author = EntityType('Author')
book = EntityType('Book')
song = EntityType('Song')
writes = RelationshipSchema('WRITES', author, book)

writes.create_relationship (
    author.create_entity('Dave'),
    book.create_entity('BookOne')
)