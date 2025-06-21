from implies.core.entity import EntityComponent, EntityType


class RelationshipSchema:
    def __init__(self, relationship_name: str, head_type: EntityType, tail_type: EntityType):
        self.relationship_name = relationship_name
        self.head_type = head_type
        self.tail_type = tail_type

    def create_relationship(self, head: EntityComponent, tail: EntityComponent):
        assert head.entity_type == self.head_type
        assert tail.entity_type == self.tail_type

        return RelationshipComponent(self, head, tail)


class RelationshipComponent:
    def __init__(self, relationship_schema: RelationshipSchema, head: EntityComponent, tail: EntityComponent):
        self.relationship_schema = relationship_schema
        self.head = head
        self.tail = tail