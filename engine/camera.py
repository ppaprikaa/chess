from .transform import Transform
import pygame as pg

rect = pg.Rect
vec = pg.Vector2

class Camera():
    def __init__(self, viewport: Transform):
        self._viewport: Transform = viewport


    def set_pos(self, pos: vec) -> None:
        self._viewport.pos = pos

    
    def get_viewport(self) -> Transform:
        return self._viewport


    def rect(self) -> rect:
        return self._viewport.get_rect()


    def set_velocity(self, velocity: vec) -> None:
        self._viewport.set_velocity(velocity)


    def move(self) -> None:
        self._viewport.move()
