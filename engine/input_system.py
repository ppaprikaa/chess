from .control import Control, ActionStatus
from .entity import Entity
from .system import System
from enum import Enum
from typing import Dict, Any
import pygame as pg

class InputSystem(System):
    def __init__(
            self, 
            actions: Any, 
            action_to_kbd: Dict[str, Enum], 
            action_to_mouse: Dict[str, int],
            ) -> None:
        self._action_to_mouse: Dict[str, int] = action_to_mouse
        self._action_to_kbd: Dict[str, Enum] = action_to_kbd
        self._actions: Any = actions


    def apply(self, entity: Entity) -> None:
        control = entity.get_component(Control)
        if control:
            current_actions = {}
            events = pg.event.get()
            
            for event in events:
                if event.type == pg.KEYDOWN:
                    for action in self._action_to_kbd:
                        if event.key == self._action_to_kbd[action]:
                            current_actions[action] = ActionStatus.ENTRANCE
                if event.type == pg.KEYUP:
                    for action in self._action_to_kbd:
                        if event.key == self._action_to_kbd[action]:
                            current_actions[action] = ActionStatus.EXIT
                if event.type == pg.MOUSEBUTTONDOWN:
                    for action in self._action_to_mouse:
                        if event.button + 1 == self._action_to_mouse[action]:
                            current_actions[action] = ActionStatus.ENTRANCE
                if event.type == pg.MOUSEBUTTONUP:
                    for action in self._action_to_mouse:
                        if event.button == self._action_to_mouse[action]:
                            current_actions[action] = ActionStatus.EXIT

            control.actions = current_actions.copy()
