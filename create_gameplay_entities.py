import pygame as pg
from engine.entity_manager import EntityManager
from engine.entity import Entity
from engine.transform import Transform
from engine.sprite import Sprite
from engine.animation import Animation
from engine.control import Control

from piece import Piece, PieceKind
from board_cursor import BoardCursor
from color import Color

from typing import Any, Dict

def create_cursor(
        em: EntityManager, 
        assets: Dict[str, Any],
        pos: pg.Vector2 = pg.Vector2(4, 4),
        size: pg.Vector2 = pg.Vector2(1, 1),
        ) -> Entity:
    cursor = em.add_entity("cursor")

    image: pg.Surface = assets["IMAGE_CURSOR"]
    image1: pg.Surface = assets["IMAGE_CURSOR1"]
    image2: pg.Surface = assets["IMAGE_CURSOR2"]
    image3: pg.Surface = assets["IMAGE_CURSOR3"]
    image4: pg.Surface = assets["IMAGE_CURSOR4"]
    image5: pg.Surface = assets["IMAGE_CURSOR5"]
    image6: pg.Surface = assets["IMAGE_CURSOR6"]
    image7: pg.Surface = assets["IMAGE_CURSOR7"]
    image8: pg.Surface = assets["IMAGE_CURSOR8"]
    image9: pg.Surface = assets["IMAGE_CURSOR9"]
    image10: pg.Surface = assets["IMAGE_CURSOR10"]

    fimage1: pg.Surface = assets["IMAGE_CURSOR_FOCUSED1"]
    fimage2: pg.Surface = assets["IMAGE_CURSOR_FOCUSED2"]
    fimage3: pg.Surface = assets["IMAGE_CURSOR_FOCUSED3"]
    fimage4: pg.Surface = assets["IMAGE_CURSOR_FOCUSED4"]
    fimage5: pg.Surface = assets["IMAGE_CURSOR_FOCUSED5"]
    fimage6: pg.Surface = assets["IMAGE_CURSOR_FOCUSED6"]
    fimage7: pg.Surface = assets["IMAGE_CURSOR_FOCUSED7"]

    sprite = Sprite(image, size)
    transform = Transform(
            pos=pos,
            size=size,
            z=2
            )

    animation = Animation({
        "IDLE": ([
            Sprite(image1, pg.Vector2(1, 1)),
            Sprite(image2, pg.Vector2(1, 1)),
            Sprite(image3, pg.Vector2(1, 1)),
            Sprite(image4, pg.Vector2(1, 1)),
            Sprite(image5, pg.Vector2(1, 1)),
            Sprite(image6, pg.Vector2(1, 1)),
            Sprite(image7, pg.Vector2(1, 1)),
            Sprite(image8, pg.Vector2(1, 1)),
            Sprite(image9, pg.Vector2(1, 1)),
            Sprite(image10, pg.Vector2(1, 1)),
            ], 0.1),
        "FOCUSED": ([
            Sprite(fimage1, pg.Vector2(1, 1)),
            Sprite(fimage2, pg.Vector2(1, 1)),
            Sprite(fimage3, pg.Vector2(1, 1)),
            Sprite(fimage4, pg.Vector2(1, 1)),
            Sprite(fimage5, pg.Vector2(1, 1)),
            Sprite(fimage6, pg.Vector2(1, 1)),
            Sprite(fimage7, pg.Vector2(1, 1)),
            ], 0.025)
        })
    cursor_component = BoardCursor()

    cursor.add_component(cursor_component)
    cursor.add_component(sprite)
    cursor.add_component(transform)
    cursor.add_component(Control())
    cursor.add_component(animation)
    return cursor


def create_square(
        em: EntityManager,
        assets: Any,
        pos: pg.Vector2, 
        size: pg.Vector2, 
        color: Color
        ) -> Entity:
    if color == Color.Black:
        color_str = "BLACK"
    else:
        color_str = "WHITE"
    image: pg.Surface = assets["IMAGE_" + color_str + "_TILE"]
    square = em.add_entity("square")
    sprite = Sprite(image, size)
    transform = Transform(
            pos=pos,
            size=size,
            z=-1
            )
    square.add_component(sprite)
    square.add_component(transform)
    return square

def create_pawn(
        em: EntityManager,
        assets: Any,
        pos: pg.Vector2, 
        size: pg.Vector2, 
        color: Color
        ) -> Entity:
    if color == Color.Black:
        color_str = "BLACK"
    else:
        color_str = "WHITE"


    image: pg.Surface = assets["IMAGE_" + color_str + "_PAWN"]
    fimage1: pg.Surface = assets["IMAGE_" + color_str + "_PAWN_FOCUSED1"]
    fimage2: pg.Surface = assets["IMAGE_" + color_str + "_PAWN_FOCUSED2"]

    animation = Animation({
        "IDLE": ([
            Sprite(image, pg.Vector2(1, 1)),
            ], 0.1),
        "FOCUSED": ([
            Sprite(fimage1, pg.Vector2(1, 1)),
            Sprite(fimage2, pg.Vector2(1, 1)),
            ], 0.1)
        })

    pawn = em.add_entity("pawn")
    sprite = Sprite(image, size)
    transform = Transform(
            pos=pos,
            size=size,
            z=1
            )
    piece = Piece(kind=PieceKind.Pawn, color=color, pos=pos)
    pawn.add_component(sprite)
    pawn.add_component(transform)
    pawn.add_component(piece)
    pawn.add_component(animation)
    return pawn


def create_rook(
        em: EntityManager,
        assets: Any,
        pos: pg.Vector2, 
        size: pg.Vector2, 
        color: Color
        ) -> Entity:
    if color == Color.Black:
        color_str = "BLACK"
    else:
        color_str = "WHITE"
    image: pg.Surface = assets["IMAGE_" + color_str + "_ROOK"]
    fimage1: pg.Surface = assets["IMAGE_" + color_str + "_PAWN_FOCUSED1"]
    fimage2: pg.Surface = assets["IMAGE_" + color_str + "_PAWN_FOCUSED2"]

    animation = Animation({
        "IDLE": ([
            Sprite(image, pg.Vector2(1, 1)),
            ], 0.1),
        "FOCUSED": ([
            Sprite(fimage1, pg.Vector2(1, 1)),
            Sprite(fimage2, pg.Vector2(1, 1)),
            ], 0.1)
        })

    rook = em.add_entity("rook")
    sprite = Sprite(image, size)
    transform = Transform(
            pos=pos,
            size=size,
            z=1
            )
    piece = Piece(kind=PieceKind.Pawn, color=color, pos=pos)
    rook.add_component(sprite)
    rook.add_component(transform)
    rook.add_component(piece)
    rook.add_component(animation)
    return rook


def create_knight(
        em: EntityManager,
        assets: Any,
        pos: pg.Vector2, 
        size: pg.Vector2, 
        color: Color
        ) -> Entity:
    if color == Color.Black:
        color_str = "BLACK"
    else:
        color_str = "WHITE"
    image: pg.Surface = assets["IMAGE_" + color_str + "_KNIGHT"]
    fimage1: pg.Surface = assets["IMAGE_" + color_str + "_KNIGHT_FOCUSED1"]
    fimage2: pg.Surface = assets["IMAGE_" + color_str + "_KNIGHT_FOCUSED2"]

    animation = Animation({
        "IDLE": ([
            Sprite(image, pg.Vector2(1, 1)),
            ], 0.1),
        "FOCUSED": ([
            Sprite(fimage1, pg.Vector2(1, 1)),
            Sprite(fimage2, pg.Vector2(1, 1)),
            ], 0.1)
        })
    knight = em.add_entity("knight")
    sprite = Sprite(image, size)
    transform = Transform(
            pos=pos,
            size=size,
            z=1
            )
    piece = Piece(kind=PieceKind.Pawn, color=color, pos=pos)
    knight.add_component(sprite)
    knight.add_component(transform)
    knight.add_component(piece)
    knight.add_component(animation)
    return knight


def create_bishop(
        em: EntityManager,
        assets: Any,
        pos: pg.Vector2, 
        size: pg.Vector2, 
        color: Color
        ) -> Entity:
    if color == Color.Black:
        color_str = "BLACK"
    else:
        color_str = "WHITE"
    image: pg.Surface = assets["IMAGE_" + color_str + "_BISHOP"]
    fimage1: pg.Surface = assets["IMAGE_" + color_str + "_BISHOP_FOCUSED1"]
    fimage2: pg.Surface = assets["IMAGE_" + color_str + "_BISHOP_FOCUSED2"]

    animation = Animation({
        "IDLE": ([
            Sprite(image, pg.Vector2(1, 1)),
            ], 0.1),
        "FOCUSED": ([
            Sprite(fimage1, pg.Vector2(1, 1)),
            Sprite(fimage2, pg.Vector2(1, 1)),
            ], 0.1)
        })

    bishop = em.add_entity("bishop")
    sprite = Sprite(image, size)
    transform = Transform(
            pos=pos,
            size=size,
            z=1
            )
    piece = Piece(kind=PieceKind.Pawn, color=color, pos=pos)
    bishop.add_component(sprite)
    bishop.add_component(transform)
    bishop.add_component(piece)
    bishop.add_component(animation)
    return bishop


def create_king(
        em: EntityManager,
        assets: Any,
        pos: pg.Vector2, 
        size: pg.Vector2, 
        color: Color
        ) -> Entity:
    if color == Color.Black:
        color_str = "BLACK"
    else:
        color_str = "WHITE"
    image: pg.Surface = assets["IMAGE_" + color_str + "_KING"]
    fimage1: pg.Surface = assets["IMAGE_" + color_str + "_KING_FOCUSED1"]
    fimage2: pg.Surface = assets["IMAGE_" + color_str + "_KING_FOCUSED2"]

    animation = Animation({
        "IDLE": ([
            Sprite(image, pg.Vector2(1, 1)),
            ], 0.1),
        "FOCUSED": ([
            Sprite(fimage1, pg.Vector2(1, 1)),
            Sprite(fimage2, pg.Vector2(1, 1)),
            ], 0.1)
        })

    king = em.add_entity("king")
    sprite = Sprite(image, size)
    transform = Transform(
            pos=pos,
            size=size,
            z=1
            )
    piece = Piece(kind=PieceKind.Pawn, color=color, pos=pos)
    king.add_component(sprite)
    king.add_component(transform)
    king.add_component(piece)
    king.add_component(animation)
    return king

def create_queen(
        em: EntityManager,
        assets: Any,
        pos: pg.Vector2, 
        size: pg.Vector2, 
        color: Color
        ) -> Entity:
    if color == Color.Black:
        color_str = "BLACK"
    else:
        color_str = "WHITE"
    image: pg.Surface = assets["IMAGE_" + color_str + "_QUEEN"]
    fimage1: pg.Surface = assets["IMAGE_" + color_str + "_QUEEN_FOCUSED1"]
    fimage2: pg.Surface = assets["IMAGE_" + color_str + "_QUEEN_FOCUSED2"]

    animation = Animation({
        "IDLE": ([
            Sprite(image, pg.Vector2(1, 1)),
            ], 0.1),
        "FOCUSED": ([
            Sprite(fimage1, pg.Vector2(1, 1)),
            Sprite(fimage2, pg.Vector2(1, 1)),
            ], 0.1)
        })

    king = em.add_entity("queen")
    sprite = Sprite(image, size)
    transform = Transform(
            pos=pos,
            size=size,
            z=1
            )
    piece = Piece(kind=PieceKind.Pawn, color=color, pos=pos)
    king.add_component(sprite)
    king.add_component(transform)
    king.add_component(piece)
    king.add_component(animation)
    return king
