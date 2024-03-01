from typing import Tuple
from color import Color
import chess
import pygame as pg

def get_square_from_pos(
        pos: pg.Vector2, 
        orientation: Color
        ) -> chess.Square:
    if orientation == Color.White:
        square_pos = (int(pos.x), int(7 - pos[1]))
    else:
        square_pos = (int(7 - pos[0]), int(pos[1]))
    
    return chess.square(square_pos[0], square_pos[1])
