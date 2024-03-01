from abc import ABC
from typing import TypeVar

class Component(ABC):
    pass


ComponentType = TypeVar('ComponentType', bound=Component)
