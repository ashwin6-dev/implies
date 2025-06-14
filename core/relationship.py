from typing import Type

from core.instance import InstanceComponent
from core.ontology_component import OntologyComponentDecorator, OntologyComponent

class RelationshipComponent(OntologyComponent):
    START_CONCEPT = ""
    END_CONCEPT = ""

    def __init__(self, source_node: Type[InstanceComponent], end_node: Type[InstanceComponent]):
        self._source_node = source_node
        self._end_node = end_node
        self.check()

    def __call__(self, *args, **kwargs):
        self.__class__._wrapped__init__(self, *args, **kwargs)
        return self

    def check(self):
        source_instance = self._source_node()
        end_instance = self._end_node()

        if source_instance.get_concept() != self.__class__.START_CONCEPT:
            raise AssertionError(f"Source concept should be {self.__class__.START_CONCEPT}. Got {source_instance.get_concept()}")

        if end_instance.get_concept() != self.__class__.END_CONCEPT:
            raise AssertionError(f"End concept should be {self.__class__.END_CONCEPT}. Got {end_instance.get_concept()}")

    def _wrapped__init__(self, *args, **kwargs):
        pass


class Relationship(OntologyComponentDecorator):
    def __init__(self, start_concept: str, end_concept: str):
        self.start_concept = start_concept
        self.end_concept = end_concept

    def __call__(self, cls) -> Type[RelationshipComponent]:
        new_class = type(cls.__name__, (RelationshipComponent, cls), {})

        new_class.START_CONCEPT = self.start_concept
        new_class.END_CONCEPT = self.end_concept
        new_class._wrapped__init__ = cls.__init__

        new_class.__module__ = cls.__module__
        new_class.__doc__ = cls.__doc__
        new_class.__qualname__ = cls.__qualname__

        return new_class