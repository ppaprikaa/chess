from .component import Component, ComponentType

from typing import Optional, Type, Dict, cast

class Entity():
    def __init__(self, id: int, tag: str):
        self._id: int = id
        self._tag: str = tag
        self._alive: bool = True

        self._components: Dict[Type[Component], Component] = {}


    def add_component(self, component: Component) -> None:
        if not self.get_component(type(component)):
            self._components[type(component)] = component


    def overwrite_component(self, component: Component) -> None:
        if self.get_component(type(component)):
            self._components[type(component)] = component


    def get_component(self, 
                      type: Type[ComponentType]
                      ) -> ComponentType | None:
        return cast(
                Optional[ComponentType], 
                self._components.get(type, None)
                )


    def get_id(self) -> int:
        return self._id


    def get_tag(self) -> str:
        return self._tag


    def is_alive(self) -> bool:
        return self._alive


    def kill(self) -> None:
        self._alive = False
