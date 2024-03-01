from .camera import Camera
from .entity import Entity
from .sprite import Sprite
from .system import System
from .transform import Transform
import pygame as pg

vec = pg.Vector2
rect = pg.Rect

class Renderer(System):
    def __init__(self, 
                 camera: Camera,
                 display_surface: pg.surface.Surface,
                 tile_size: vec
                 ):
        self._cam = camera
        self._display_surface = display_surface
        self._tile_size = tile_size


    def apply(self, entity: Entity) -> None:
        sprite = entity.get_component(Sprite)
        transform = entity.get_component(Transform)
        if sprite and transform and \
        self._cam.get_viewport().scale(
                self._tile_size
                ).get_rect().colliderect(
                        transform.scale(self._tile_size).get_rect()
                        ):
            self.__render(sprite, transform)


    def __render(
            self, 
            sprite: Sprite,
            transform: Transform
            ) -> None:
        tfr = transform.scale(self._tile_size).get_rect()
        vpr = self._cam.get_viewport().scale(self._tile_size).get_rect()
        rrect = rect(
                tfr.x - vpr.x, 
                tfr.y - vpr.y, 
                tfr.width, 
                tfr.height
                )
        self._display_surface.blit(
                pg.transform.scale(
                    sprite.surface(),
                    vec(
                        sprite.size().x * self._tile_size.x,
                        sprite.size().y * self._tile_size.y
                        )
                    ), 
                rrect,
                ) 
