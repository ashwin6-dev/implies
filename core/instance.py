from typing import Type

from core.ontology_component import OntologyComponentDecorator, OntologyComponent


class InstanceComponent(OntologyComponent):
    CONCEPT_VALUE = ""

    def get_concept(self):
        return self.__class__.CONCEPT_VALUE

class Instance(OntologyComponentDecorator):
    def __init__(self, concept: str):
        self.concept = concept

    def __call__(self, cls) -> Type[InstanceComponent]:
        new_class = type(cls.__name__, (InstanceComponent, cls), {})
        new_class.CONCEPT_VALUE = self.concept

        new_class.__module__ = cls.__module__
        new_class.__doc__ = cls.__doc__
        new_class.__qualname__ = cls.__qualname__

        return new_class