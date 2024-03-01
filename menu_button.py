from engine.component import Component

class MenuButton(Component):
    def __init__(self, scene_to_switch: str) -> None:
        self.scene_to_switch = scene_to_switch
