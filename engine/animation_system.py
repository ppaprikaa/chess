import pygame as pg

from .sprite import Sprite
from .system import System
from .entity import Entity
from .animation import Animation

vec = pg.Vector2
rect = pg.Rect

class Animator(System):
    def __init__(self):
        pass


    def apply(self, entity: Entity) -> None:
        sprite = entity.get_component(Sprite)
        animation = entity.get_component(Animation)
        if sprite and animation and animation.is_active():
            animation.step()
            entity.overwrite_component(animation.get_current())
