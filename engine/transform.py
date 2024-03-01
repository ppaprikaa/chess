from .component import Component

from pygame import Vector2, Rect

vec = Vector2
rect = Rect

class Transform(Component):
    def __init__(self, 
                 pos: vec, 
                 size: vec, 
                 direction: vec = vec(0, 0), 
                 speed: float = 0, 
                 z: int = 1,
                 ):
        self.pos = pos
        self.size = size
        if direction.length() != 0:
            direction = direction.normalize()
        self.direction = direction
        self.speed = speed
        self.velocity = vec(
                self.direction.x * self.speed,
                self.direction.y * self.speed,
                )

        # value by which certain entites will be sorted
        # for example
        # Tiles == 0
        # entities == 1
        # HUD == 2
        self.z = z


    def scale(self, scaler: vec) -> 'Transform':
        return Transform(
                pos=vec(
                    self.pos.x * scaler.x,
                    self.pos.y * scaler.y,
                    ),
                size=vec(
                    self.size.x * scaler.x,
                    self.size.y * scaler.y,
                    ),
                )


    def get_center(self) -> vec:
        return vec(
                self.pos.x + (self.size.x / 2),
                self.pos.y + (self.size.y / 2)
                )


    def get_rect(self) -> rect:
        return rect(
                self.pos.x,
                self.pos.y,
                self.size.x,
                self.size.y,
                )



    def set_direction(self, direction: vec) -> None:
        if direction.length() != 0:
            self.direction = direction.normalize()
            self.velocity = vec(
                    self.direction.x * self.speed,
                    self.direction.y * self.speed,
                    )
        else:
            self.direction = vec(0, 0)
            self.speed = 0


    def set_speed(self, speed: float) -> None:
        self.speed = speed / 100
        self.velocity = vec(
                self.direction.x * self.speed,
                self.direction.y * self.speed,
                )


    def set_velocity(self, velocity: vec) -> None:
        self.velocity = velocity
        if velocity.length() != 0:
            self.direction = velocity.normalize()
        else:
            self.direction = velocity

        self.speed = 0
        if self.direction.x != 0:
            self.speed = self.velocity.x / self.direction.x
        if self.direction.y != 0:
            self.speed = self.velocity.y / self.direction.y


    def set_center(self, center: vec) -> None:
        self.pos.x = center.x - (self.size.x / 2)
        self.pos.y = center.y - (self.size.y / 2)


    def move(self) -> None:
        self.pos = vec(
                self.pos.x + (self.velocity.x),
                self.pos.y + (self.velocity.y),
                )


    def is_moving(self) -> bool:
        return self.speed != 0 and self.direction.length() != 0 and \
                self.velocity.length() != 0
