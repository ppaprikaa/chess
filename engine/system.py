from abc import ABC, abstractmethod
from .entity import Entity

class System(ABC):
    @abstractmethod
    def apply(self, entity: Entity) -> None:
        pass
