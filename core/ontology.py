from typing import List, Dict, Type, TypeVar

from .instance import InstanceComponent
from .relationship import RelationshipComponent

class OntologySpec:
    def __init__(self):
        self.instances: Dict[str, List[InstanceComponent]] = {}
        self.relationship_types: Dict[str, List[str]] = {}
        self.relationships: List[RelationshipComponent] = []

    def register_instance(self, instance: Type[InstanceComponent]):
        instance = instance()
        concept = instance.get_concept()

        if concept not in self.instances:
            self.instances[concept] = []

        self.instances[concept].append(instance)

    def register_relationship(self, relationship: Type[RelationshipComponent]):
        relationship.ONTOLOGY_SPEC = self
        relationship_name = relationship.__name__

        self.relationship_types[relationship_name] = [relationship.START_CONCEPT, relationship.END_CONCEPT]

    def add_relationship(self, relationship: RelationshipComponent):
        self.relationships.append(relationship)

    def get_instances(self):
        return self.instances

    def get_concepts(self):
        return self.instances.keys()

    def get_relationships(self):
        return self.relationships

    def get_relationship_types(self):
        return self.relationship_types


T = TypeVar('T', bound=type)

class Ontology:
    def __init__(self, spec):
        self.spec: OntologySpec = spec

    def __call__(self, cls: Type[T]) -> Type[T]:
        if issubclass(cls, InstanceComponent):
            self.spec.register_instance(cls)
        elif issubclass(cls, RelationshipComponent):
            self.spec.register_relationship(cls)

        return cls