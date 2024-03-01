from engine.component import Component
from enum import Enum
import pygame as pg

class CursorState(Enum):
    Free = 1
    TryFocus = 2
    Focused = 3
    TryRelease = 4

class BoardCursor(Component):
    def __init__(self) -> None:
        self.state: CursorState = CursorState.Free
        self.pos: pg.Vector2 = pg.Vector2(3, 3)
