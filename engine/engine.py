from .camera import Camera
from .config import load_config
from .execution_context import ExecutionContext
from .render_window import RenderWindow
from .scene import Scene
from .transform import Transform

from typing import Dict
import pygame as pg

class Engine():
    def __init__(self, config_path: str) -> None:  
        pg.init()
        config = load_config(config_path) 

        self._window = RenderWindow(
                base_resolution=pg.Vector2(
                    config["window"]["base_resolution"]["x"],
                    config["window"]["base_resolution"]["y"]
                    ),
                target_resolution=pg.Vector2(
                    config["window"]["target_resolution"]["x"],
                    config["window"]["target_resolution"]["y"]
                    ),
                tile_size=pg.Vector2(
                    config["window"]["tile_size"]["x"],
                    config["window"]["tile_size"]["y"]
                    ),
                full_screen=config["window"]["fullscreen"]
                )

        self._context = ExecutionContext(
                self._window,
                Camera(
                    viewport=Transform(
                        pos=pg.Vector2(0.0, 0.0),
                        size=self._window.tiles()
                        )
                    ),
                clock=pg.time.Clock(),
                FPS=config["FPS"]  
                )

        self._scenes: Dict[str, Scene] = {}


    def add_scene(self, scene_name: str) -> Scene:
        scene = Scene(self._context)
        self._scenes[scene_name] = scene
        return scene


    def run(self) -> None:
        while not self._context.is_running():
            scene =  self._scenes.get(self._context.current_scene())
            if scene is None:
                break

            
            scene.run_and_switch()
        pg.quit()


    def context(self) -> ExecutionContext:
        return self._context
