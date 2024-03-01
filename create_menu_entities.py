from engine.entity_manager import EntityManager
from engine.transform import Transform
from engine.control import Control
from engine.sprite import Sprite
from engine.entity import Entity

from typing import Dict, Any

from menu_button import MenuButton

import pygame as pg

def create_background(
        em: EntityManager,
        assets: Dict[str, Any],
        background_tag: str
        ) -> Entity:
    background = em.add_entity("background")
    sprite = Sprite(assets[background_tag], pg.Vector2(8, 8))
    transform = Transform(pg.Vector2(0, 0), pg.Vector2(1, 1)) 

    background.add_component(sprite)
    background.add_component(transform)
    return background

def create_cursor(
        em: EntityManager,
        pos: pg.Vector2,
        ) -> Entity:
    surface = pg.surface.Surface((16, 16))
    surface.fill((255, 0, 0))

    transform = Transform(pos, pg.Vector2(1, 1), z=2)
    sprite = Sprite(surface, pg.Vector2(1, 1))
    control = Control()
    
    cursor = em.add_entity("cursor")
    cursor.add_component(transform)
    cursor.add_component(sprite)
    cursor.add_component(control)
    return cursor

def create_menu_button(
        em: EntityManager,
        scene_to_switch: str,
        pos: pg.Vector2,
        size: pg.Vector2
        ) -> Entity:
    transform = Transform(pos, size)
    button_component = MenuButton(scene_to_switch)

    button = em.add_entity("button")
    button.add_component(transform)
    button.add_component(button_component)
    return button
