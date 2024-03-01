from engine.engine import Engine
from gameplay_scene import gameplay_scene
from menu_scene import menu_scene
from pick_side_menu_scene import pick_side_menu_scene
from result_scene import result_scene

from color import Color

engine = Engine("config/config.json")

menu_scene(engine)
pick_side_menu_scene(engine)
gameplay_scene(engine, Color.White)
gameplay_scene(engine, Color.Black)
result_scene(engine, "DRAW", "IMAGE_DRAW")
result_scene(engine, "WIN", "IMAGE_WIN")
result_scene(engine, "LOSE", "IMAGE_LOSE")

engine.run()
