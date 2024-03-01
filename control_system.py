from engine.system import System
from engine.execution_context import ExecutionContext
from engine.entity import Entity
from engine.control import Control, ActionStatus
from engine.transform import Transform

from board_cursor import BoardCursor, CursorState

class ControlSystem(System):
    def __init__(
            self, 
            context: ExecutionContext,
            ) -> None:
       self._context = context


    def apply(self, entity: Entity) -> None:
        control = entity.get_component(Control)
        if control:
            if len(control.actions) != 0:
                print(control.actions)
            if control.actions.get("SCENE_PAUSE") and\
                    control.actions.get(
                            "SCENE_PAUSE"
                            ) == ActionStatus.ENTRANCE:
                self._context.set_scene_to_switch("PAUSE")
                self._context.switch_to_next()
            if control.actions.get("CURSOR_MOVE_FORWARD"):
                transform = entity.get_component(Transform)
                action_status = control.actions.get("CURSOR_MOVE_FORWARD")
                if action_status == ActionStatus.ENTRANCE and transform:
                    transform.direction.y = -1
                elif action_status == ActionStatus.EXIT and transform:
                    transform.direction.y = 0
            if control.actions.get("CURSOR_MOVE_BACKWARD"):
                transform = entity.get_component(Transform)
                action_status = control.actions.get(
                        "CURSOR_MOVE_BACKWARD"
                        )
                if action_status == ActionStatus.ENTRANCE and transform:
                    transform.direction.y = 1
                elif action_status == ActionStatus.EXIT and transform:
                    transform.direction.y = 0
            if control.actions.get("CURSOR_MOVE_LEFT"):
                transform = entity.get_component(Transform)
                action_status = control.actions.get(
                        "CURSOR_MOVE_LEFT"
                        )
                if action_status == ActionStatus.ENTRANCE and transform:
                    transform.direction.x = -1
                elif action_status == ActionStatus.EXIT and transform:
                    transform.direction.x = 0
            if control.actions.get("CURSOR_MOVE_RIGHT"):
                transform = entity.get_component(Transform)
                action_status = control.actions.get(
                        "CURSOR_MOVE_RIGHT"
                        )
                if action_status == ActionStatus.ENTRANCE and transform:
                    transform.direction.x = 1
                elif action_status == ActionStatus.EXIT and transform:
                    transform.direction.x = 0
            if control.actions.get("CURSOR_FOCUS"):
                board_cursor = entity.get_component(BoardCursor)
                action_status = control.actions.get(
                        "CURSOR_FOCUS"
                        )
                if action_status == ActionStatus.EXIT and board_cursor:
                    match board_cursor.state:
                        case CursorState.Free:
                            print("try focus")
                            board_cursor.state = CursorState.TryFocus
                        case CursorState.Focused:
                            print("try release")
                            board_cursor.state = CursorState.TryRelease
