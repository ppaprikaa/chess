from engine.system import System
from engine.entity import Entity
from engine.control import Control, ActionStatus
from engine.transform import Transform
from engine.execution_context import ExecutionContext

import pygame as pg

class MenuControlSystem(System):
    def __init__(
            self, 
            context: ExecutionContext, 
            upper_bound: int,
            lower_bound: int
            ) -> None:
        self.context = context
        self._upper_bound = upper_bound
        self._lower_bound = lower_bound

    def apply(self, entity: Entity) -> None:
        control = entity.get_component(Control)
        if not control:
            return

        if control.actions.get(
                "CURSOR_FOCUS"
                ) and control.actions.get(
                        "CURSOR_FOCUS"
                        ) == ActionStatus.ENTRANCE:
                    self.context.switch_to_next()

        if control.actions.get(
                "CURSOR_MOVE_FORWARD"
                ) and control.actions.get(
                        "CURSOR_MOVE_FORWARD"
                        ) == ActionStatus.ENTRANCE:
                    transform = entity.get_component(Transform)
                    if transform:
                        transform.set_direction(pg.Vector2(0, -1))
                        transform.set_speed(100)
                        transform.move()
                        transform.set_speed(0)
                        if transform.pos.y < self._lower_bound:
                            transform.pos.y = self._lower_bound

        if control.actions.get(
                "CURSOR_MOVE_BACKWARD"
                ) and control.actions.get(
                        "CURSOR_MOVE_BACKWARD"
                        ) == ActionStatus.ENTRANCE:
                    transform = entity.get_component(Transform)
                    if transform:
                        transform.set_direction(pg.Vector2(0, 1))
                        transform.set_speed(100)
                        transform.move()
                        transform.set_speed(0)
                        if transform.pos.y > self._upper_bound:
                            transform.pos.y = self._upper_bound

