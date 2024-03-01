from engine.engine import Engine
from engine.asset_loading import load_assets_from_config
from engine.input_actions_loading import load_input_actions_from_file
from engine.transform import Transform

from engine.render_system import Renderer
from engine.input_system import InputSystem
from menu_control_system import MenuControlSystem
from menu_scene_switch_system import MenuSceneSwitchSystem
from create_menu_entities import create_cursor, create_menu_button,\
        create_background

import pygame as pg

def menu_scene(engine: Engine) -> None:
    actions, action_to_kbd, action_to_mouse, _ = \
            load_input_actions_from_file("config/input_actions.json")

    start_scene = engine.add_scene("START")

    context = engine.context()
    em = start_scene.entity_manager()
    assets = load_assets_from_config("config/assets.json")

    create_background(
            em,
            assets,
            "IMAGE_MENU_BACKGROUND",
            )
    cursor = create_cursor(em, pg.Vector2(2, 3))
    create_menu_button(
            em,
            "PICK_SIDE",
            pg.Vector2(2, 4),
            pg.Vector2(1, 4)
            )
    create_menu_button(
            em,
            "EXIT",
            pg.Vector2(2, 5),
            pg.Vector2(1, 3)
            )
    render_sys = Renderer(
            context.camera(), 
            context.window().surface(),
            context.window().tile_size()
            )

    cursor_transform = cursor.get_component(Transform)
    if not cursor_transform:
        context.set_scene_to_switch("EXIT")
        context.switch_to_next()
        return

    input_system = InputSystem(actions, action_to_kbd, action_to_mouse)
    control_system = MenuControlSystem(start_scene.context(), 5, 3)
    menu_scene_switch_system = MenuSceneSwitchSystem(
            cursor_transform,
            context
            )

    start_scene.add_system(input_system)
    start_scene.add_system(render_sys)
    start_scene.add_system(control_system)
    start_scene.add_system(menu_scene_switch_system)
