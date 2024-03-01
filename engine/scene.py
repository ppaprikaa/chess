from .entity import Entity
from .system import System
from .transform import Transform
from.entity_manager import EntityManager
from .execution_context import ExecutionContext

from typing import Any, List, Tuple
from sys import maxsize

class Scene():
    def __init__(
            self, 
            context: ExecutionContext, 
            entity_sort_func: Any | None = None):
        self._em = EntityManager()
        self._systems: List[System] = []
        self._context = context
        if not entity_sort_func:
            self._entity_sort_func = self.default_entity_sorting


    def run_and_switch(self) -> None:
        self.__run()
        self.__switch_to_next()

    
    def __switch_to_next(self) -> None:
        self._context.stop()
        self._context.switch_to_next()


    def __run(self) -> None:
        self._context.run()
        while self._context.is_running():
            self._context.prologue()
            for e in self._em.get_entities():
                self.apply_systems(e)

            self._em.update()
            self._em.sort(self._entity_sort_func)
            self._context.epilogue()


    def apply_systems(self, entity: Entity) -> None:
        for system in self._systems:
            system.apply(entity)


    def add_system(self, system: System) -> None:
        self._systems.append(system)


    def entity_manager(self) -> EntityManager:
        return self._em


    def context(self) -> ExecutionContext:
        return self._context

    
    def default_entity_sorting(self, entity: Entity) -> Tuple[
            int, float
            ]:
        transform = entity.get_component(Transform)
        if transform:
            return transform.z, transform.pos.y
        return (-maxsize, maxsize)
