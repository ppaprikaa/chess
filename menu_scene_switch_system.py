from engine.system import System
from engine.transform import Transform
from engine.execution_context import ExecutionContext
from engine.entity import Entity
from menu_button import MenuButton

class MenuSceneSwitchSystem(System):
    def __init__(
            self,
            cursor_transform: Transform, 
            context: ExecutionContext
            ) -> None:
        self.cursor_transform = cursor_transform
        self.context = context


    def apply(self, entity: Entity) -> None:
        button = entity.get_component(MenuButton)
        transform = entity.get_component(Transform)

        if button and transform and\
                transform.get_rect().colliderect(
                        self.cursor_transform.get_rect()
                        ):
                    self.context.set_scene_to_switch(
                            button.scene_to_switch
                            )
