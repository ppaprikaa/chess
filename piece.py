from engine.component import Component
from enum import Enum
from color import Color

import pygame as pg

class PieceKind(Enum):
    Pawn = 1
    Knight = 2
    Bishop = 3
    Rook = 5 
    Queen = 6
    King = 7

KIND_TO_SYMBOLS = { 
           PieceKind.Pawn: "p", 
           PieceKind.Rook: "r",
           PieceKind.Knight: "n",
           PieceKind.Bishop: "b",
           PieceKind.Queen: "q",
           PieceKind.King: "k"
        }

class PieceState(Enum):
    Free = 1
    Focused = 2


class Piece(Component):
    def __init__(
            self, 
            kind: PieceKind, 
            color: Color, 
            pos: pg.Vector2
            ) -> None:
        self.kind = kind
        self.color = color
        self.pos = pos #transform parsed to chess board cords
        self.pos_to_move = pos
        self.state = PieceState.Free
        self.captured = False

    def get_symbol(self) -> str:
        if self.color == Color.White:
            return KIND_TO_SYMBOLS[self.kind].upper()

        return KIND_TO_SYMBOLS[self.kind]
