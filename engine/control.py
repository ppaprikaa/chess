from .component import Component

from typing import Dict
from enum import Enum

class ActionStatus(Enum):
    INACTIVE = 0
    ENTRANCE = 1
    EXIT = 2

class Control(Component):
    def __init__(self):
        self.actions: Dict[str, ActionStatus] = {}
