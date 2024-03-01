from .render_window import RenderWindow
from .camera import Camera
import pygame as pg

class ExecutionContext():
    def __init__(
            self, 
            window: RenderWindow, 
            camera: Camera,
            clock: pg.time.Clock, 
            FPS: int,
            scene: str = "START",
            scene_to_switch: str = "PAUSE"
            ) -> None:
        self._window = window
        self._camera = camera
        self._clock = clock
        self._FPS = FPS
        self._delta_time = float(1) / self._FPS
        self._current_scene = scene
        self._scene_to_switch = scene_to_switch
        self._is_running = False


    def run(self) -> None:
        self._is_running = True


    def stop(self) -> None:
        self._is_running = False


    def switch_to_next(self) -> None:
        self._current_scene = self._scene_to_switch
        self.stop()


    def prologue(self) -> None:
        self._window.surface().fill((0, 0, 0))


    def epilogue(self) -> None:
        self._clock.tick(self._FPS)
        pg.display.flip()
        pg.event.pump()


    def clock(self) -> pg.time.Clock:
        return self._clock


    def window(self) -> RenderWindow:
        return self._window


    def camera(self) -> Camera:
        return self._camera

    def is_running(self) -> bool:
        return self._is_running


    def set_scene_to_switch(self, scene_to_switch: str) -> None:
        self._scene_to_switch = scene_to_switch

    
    def scene_to_switch(self) -> str:
        return self._scene_to_switch


    def current_scene(self) -> str:
        return self._current_scene

    
    def get_FPS(self) -> int:
        return self._FPS


    def get_delta_time(self) -> float:
        return self._delta_time
