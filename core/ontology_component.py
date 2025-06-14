from typing import Type


class OntologyComponent:
    def get_props(self):
        self_dict = self.__dict__
        return {k: v for k, v in self_dict.items() if not k.startswith('_')}

class OntologyComponentDecorator:
    def __call__(self, cls) -> Type[OntologyComponent]:
        new_class = type(cls.__name__, (OntologyComponent, cls), {})

        new_class.__module__ = cls.__module__
        new_class.__doc__ = cls.__doc__
        new_class.__qualname__ = cls.__qualname__

        return new_class