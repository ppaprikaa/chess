import pygame as pg

class RenderWindow():
    def __init__(self, 
                 base_resolution: pg.Vector2 = pg.Vector2(640, 480), 
                 target_resolution: pg.Vector2 = pg.Vector2(640, 480),
                 tile_size = pg.Vector2(16, 16),
                 full_screen: bool = False,
                 ):
        flags = pg.RESIZABLE
        if full_screen:
            flags |= pg.FULLSCREEN | pg.DOUBLEBUF | pg.HWSURFACE
        else:
            flags |= pg.NOFRAME
        self._display_surface = pg.display.set_mode(
                size=(int(target_resolution.x), int(target_resolution.y)),
                flags=flags
                )

        self._target_resolution: pg.Vector2 = target_resolution
        self._base_resolution: pg.Vector2 = base_resolution
        self._full_screen: bool = full_screen
        self._scale = pg.Vector2(
                self._target_resolution.x / self._base_resolution.x,
                self._target_resolution.y / self._base_resolution.y
                )
        self._tile_size = pg.Vector2(
                tile_size.x * self._scale.x,
                tile_size.y * self._scale.y
                )


    def tiles(self) -> pg.Vector2:
        return pg.Vector2(
                self._target_resolution.x / self._tile_size.x,
                self._target_resolution.y / self._tile_size.y
                )


    def scale(self) -> pg.Vector2:
        return self._scale

    

    def tile_size(self) -> pg.Vector2:
        return self._tile_size


    def base_resolution(self) -> pg.Vector2:
        return self._base_resolution


    def target_resolution(self) -> pg.Vector2:
        return self._target_resolution


    def surface(self) -> pg.surface.Surface:
        return self._display_surface
