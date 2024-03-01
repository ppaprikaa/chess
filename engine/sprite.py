import pygame as pg
from .component import Component

class Sprite(pg.sprite.Sprite, Component):
    def __init__(
            self, 
            surface: pg.surface.Surface,
            size: pg.Vector2
            ):
        super().__init__()
        self._size = size
        self._surface = pg.transform.scale(
                surface=surface, 
                size=size * 100,
                )
        self._rect = self._surface.get_rect()


    def scale(self, factor: float) -> None:
        self._surface = pg.transform.scale_by(
                surface=self._surface, 
                factor=factor / 100
                )


    def surface(self) -> pg.surface.Surface:
            return self._surface

    
    def size(self) -> pg.Vector2:
        return self._size


    def rect(self) -> pg.rect.Rect:
        return self._rect


    def set_pos(self, x: float, y: float):
        self._rect.center = int(x), int(y)
