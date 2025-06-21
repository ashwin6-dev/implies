class EntityType:
    def __init__(self, type_name: str):
        self.type_name = type_name

    def create_entity(self, entity_name, props=None):
        if props is None:
            props = {}

        return EntityComponent(entity_name, props, self)

    def __eq__(self, other):
        return self.type_name == other.type_name

class EntityComponent:
    def __init__(self, entity_name: str, props, entity_type: EntityType):
        self.entity_name = entity_name
        self.props = props
        self.entity_type = entity_type