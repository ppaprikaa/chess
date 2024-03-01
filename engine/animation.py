from .component import Component
from .sprite import Sprite

from typing import List, Mapping, Tuple

import math

class Animation(Component):
    def __init__(
            self,
            animation_to_sprites: Mapping[
                str, 
                Tuple[List[Sprite], float]
                ],
            ):
        self._animation_to_sprite_ranges = animation_to_sprites
        self._current_animations: List[Sprite] = []
        self._current_frame: float = 0
        self._speed = 0.2
        self._active = False


    def set_animation(self, name: str, frame: float = 0.0) -> None:
        animation = self._animation_to_sprite_ranges.get(name)
        if not animation:
            return
        
        self._current_animations, self._speed = \
                self._animation_to_sprite_ranges[name]
        self._current_frame = frame
        self._active = True


    def set_active(self, active: bool = True) -> None:
        self._active = active


    def step(self) -> None:
        self._current_frame = math.fmod(
                self._current_frame + self._speed, 
                len(self._current_animations)
                )
        self._current = self.get_current()


    def get_current(self) -> Sprite:
        return self._current_animations[int(self._current_frame)]

    
    def is_active(self) -> bool:
        return self._active
