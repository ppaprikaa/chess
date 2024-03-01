from engine.engine import Engine
from engine.execution_context import ExecutionContext
from engine.entity import Entity
from engine.control import ActionStatus, Control
from engine.asset_loading import load_assets_from_config
from engine.input_actions_loading import load_input_actions_from_file
from engine.system import System
from engine.render_system import Renderer
from engine.input_system import InputSystem
from create_menu_entities import create_background

class ControlSystem(System):
    def __init__(self, context: ExecutionContext) -> None:
        self.context = context

    def apply(self, entity: Entity) -> None:
        control = entity.get_component(Control)
        if control:
            if control.actions.get("SCENE_PAUSE") and\
                    control.actions.get("SCENE_PAUSE") ==\
                    ActionStatus.ENTRANCE:
                        self.context.set_scene_to_switch("EXIT")
                        self.context.switch_to_next()
            
        

def result_scene(engine: Engine, scene: str, background: str) -> None:
    actions, action_to_kbd, action_to_mouse, _ = \
            load_input_actions_from_file("config/input_actions.json")

    start_scene = engine.add_scene(scene)

    context = engine.context()
    em = start_scene.entity_manager()
    assets = load_assets_from_config("config/assets.json")

    controller = em.add_entity("controller")
    controller.add_component(Control())

    create_background(
            em,
            assets,
            background
            )

    render_sys = Renderer(
            context.camera(), 
            context.window().surface(),
            context.window().tile_size()
            )

    input_system = InputSystem(actions, action_to_kbd, action_to_mouse)
    control_system = ControlSystem(start_scene.context())

    start_scene.add_system(input_system)
    start_scene.add_system(render_sys)
    start_scene.add_system(control_system)
