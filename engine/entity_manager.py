from .entity import Entity

from typing import Any, Dict, List

class EntityManager():
    def __init__(self):
        self._entities: List[Entity] = []
        self._entities_by_tag: Dict[str, List[Entity]] = {}

        self._to_add: List[Entity] = []

        self._gen_entity_id = 1


    def add_entity(self, tag: str) -> Entity:
        e = Entity(self._gen_entity_id, tag)
        self._gen_entity_id += 1
        self._to_add.append(e)
        return e


    def get_entities(self, tag: str | None = None) -> List[Entity]:
        if tag is None:
            return self._entities
        return self._entities_by_tag[tag]


    def sort(self, key_func: Any, reverse: bool = False) -> None:
        if key_func:
            self._entities = sorted(
                    self._entities, 
                    key=key_func, 
                    reverse=reverse
                    )


    def update(self):
        for entity in self._to_add:
            self._entities.append(entity)
            if not self._entities_by_tag.get(entity.get_tag()):
                self._entities_by_tag[entity.get_tag()] = [entity]
            self._entities_by_tag[entity.get_tag()].append(entity)
        self._to_add.clear()

        for entity in list(self._entities):
            if not entity.is_alive():
                self._entities_by_tag[entity.get_tag()].remove(entity)
                self._entities.remove(entity)
