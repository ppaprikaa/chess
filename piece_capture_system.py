from chess import Board
from color import Color
from engine.entity import Entity
from engine.system import System
from piece import Piece

class PieceCaptureSystem(System):
    def __init__(self, board: Board, orientation: Color) -> None:
        self.orientation = orientation
        self.board = board


    def apply(self, entity: Entity) -> None: 
        piece = entity.get_component(Piece)
        if piece and piece.captured:
            entity.kill()
