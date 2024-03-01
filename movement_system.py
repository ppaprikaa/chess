from engine.system import System
from engine.entity import Entity

from engine.transform import Transform
from engine.control import Control
from board_cursor import BoardCursor, CursorState
from color import Color

from piece import Piece, PieceState
from typing import Dict, Tuple

import chess
import square_parsing as sp

class MovementSystem(System):
    def __init__(
            self, 
            board: chess.Board, 
            cursor: BoardCursor, 
            orientation: Color
            ) -> None:
        self._board = board
        self._cursor = cursor
        self._orientation = orientation
        self._turn = Color.White
        self._to_capture: Dict[Tuple[int, int, Color], str | None] = {}


    def apply(self, entity: Entity) -> None:
        transform = entity.get_component(Transform)
        control = entity.get_component(Control)
        cursor = entity.get_component(BoardCursor)
        if transform and control and cursor:
            if not transform.is_moving():
                transform.set_speed(100)
                transform.move()
            if transform.pos.x < 0:
                transform.pos.x = 0
            if transform.pos.x > 7:
                transform.pos.x = 7
            if transform.pos.y < 0:
                transform.pos.y = 0
            if transform.pos.y > 7:
                transform.pos.y = 7
            cursor.pos = transform.pos
            self._cursor = cursor
            return

        piece = entity.get_component(Piece)
        if transform and piece:
            if self._cursor.state == CursorState.TryFocus:

                piece_at = self._board.piece_at(
                        sp.get_square_from_pos(
                            self._cursor.pos,
                            self._orientation
                            )
                        )

                if piece_at is not None:
                    if self._cursor.pos == transform.pos and\
                            piece.color == self._turn:
                                self._cursor.state = CursorState.Focused
                                piece.state = PieceState.Focused
                else:
                    self._cursor.state = CursorState.Free

            if self._cursor.state == CursorState.TryRelease:
                if piece.state == PieceState.Focused and piece.color == self._turn:
                    square_from = sp.get_square_from_pos(
                            transform.pos,
                            self._orientation
                            )

                    square_to = sp.get_square_from_pos(
                            self._cursor.pos,
                            self._orientation
                            )
                    move = chess.Move(
                            from_square=square_from,
                            to_square=square_to,
                            )
                    if self._board.is_legal(move):
                        piece.pos = transform.pos
                        piece.pos_to_move = self._cursor.pos

                        piece.state = PieceState.Free
                        self._cursor.state = CursorState.Free

                        if self._turn == Color.White:
                            self._turn = Color.Black
                        else:
                            self._turn = Color.White
                    else:
                        piece.state = PieceState.Free
                        self._cursor.state = CursorState.Free
        return
