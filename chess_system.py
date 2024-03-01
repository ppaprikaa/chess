from engine.system import System
from engine.entity import Entity
from engine.transform import Transform
from engine.execution_context import ExecutionContext

from piece import Piece
from color import Color, opposite_color
from square_parsing import get_square_from_pos

from typing import Dict, Tuple
import chess
import pygame as pg

class ChessSystem(System):
    def __init__(
            self, 
            context: ExecutionContext,
            board: chess.Board, 
            orientation: Color
            ) -> None:
        self._context = context
        self._board = board
        self._orientation = orientation
        self._to_capture: Dict[
                Tuple[int, int, Color],
                bool
                ] = {}
        self._castle_move: Dict[
                Tuple[int, int, Color],
                Tuple[int, int] | None
                ] = {}


    def apply(self, entity: Entity) -> None:
        piece = entity.get_component(Piece)
        transform = entity.get_component(Transform)
        if not piece or not transform:
            return

        capturable = self._to_capture.get((
                int(piece.pos.x),
                int(piece.pos.y),
                piece.color
                ))
        if len(self._to_capture):
            print(self._to_capture)
        if capturable:
            self._to_capture.pop(
                    (int(piece.pos.x),
                     int(piece.pos.y), 
                     piece.color)
                    )
            entity.kill()
            return

        key = (int(piece.pos.x), int(piece.pos.y), piece.color)
        castle_move = self._castle_move.get(key)
        if castle_move:
            transform.pos = pg.Vector2(castle_move[0], castle_move[1])
            piece.pos = pg.Vector2(castle_move[0], castle_move[1])
            piece.pos_to_move = pg.Vector2(castle_move[0], castle_move[1])
            
            self._castle_move.pop(key)
            return

        square_from = get_square_from_pos(piece.pos, self._orientation)
        square_to = get_square_from_pos(piece.pos_to_move, self._orientation)
        move = chess.Move(
                from_square=square_from,
                to_square=square_to
                )
        if self._board.is_game_over():
            outcome = self._board.outcome()
            if outcome and outcome.winner == chess.WHITE:
                if self._orientation == Color.White:
                    self._context.set_scene_to_switch("WIN")
                else:
                    self._context.set_scene_to_switch("LOSE")
                self._context.switch_to_next()
                return
            elif outcome and outcome.winner == chess.BLACK:
                if self._orientation == Color.Black:
                    self._context.set_scene_to_switch("WIN")
                else:
                    self._context.set_scene_to_switch("LOSE")
                self._context.switch_to_next()
                return
            else:
                self._context.set_scene_to_switch("DRAW")
                self._context.switch_to_next()
                return

        if self._board.is_legal(move):
            if self._board.is_capture(move):
                if not self._board.is_en_passant(move):
                    capturable = self._board.piece_at(
                            square_to
                            )
                    if capturable:
                        self._to_capture[(
                            int(piece.pos_to_move.x),
                            int(piece.pos_to_move.y),
                            opposite_color(piece.color)
                            )] = True
                else:
                    if piece.color == self._orientation:
                        diff = 1
                    else:
                        diff = -1

                    capturable = self._board.piece_at(
                                get_square_from_pos(
                                pg.Vector2(
                                    piece.pos_to_move.x,
                                    piece.pos_to_move.y + diff,
                                    ),
                                self._orientation,
                                )
                            )
                    if capturable:
                        self._to_capture[(
                            int(piece.pos_to_move.x),
                            int(piece.pos_to_move.y + diff),
                            opposite_color(piece.color)
                            )] = True


            elif self._board.is_queenside_castling(move):
                if self._orientation == Color.Black:
                    if piece.color == Color.Black:
                        self._castle_move[(7, 7, piece.color)] = \
                                (4, 7)
                    if piece.color == Color.White:
                        self._castle_move[(7, 0, piece.color)] = \
                                (4, 0)
                else:
                    if piece.color == Color.White:
                        self._castle_move[(0, 7, piece.color)] = \
                                (3, 7)
                    if piece.color == Color.Black:
                        self._castle_move[(0, 0, piece.color)] = \
                                (3, 0)
            elif self._board.is_kingside_castling(move):
                if self._orientation == Color.White:
                    if piece.color == Color.White:
                        self._castle_move[(7, 7, piece.color)] = \
                                (5, 7)
                    if piece.color == Color.Black:
                        self._castle_move[(7, 0, piece.color)] = \
                                (5, 0)
                else:
                    if piece.color == Color.Black:
                        self._castle_move[(0, 7, piece.color)] = \
                                (2, 7)
                    if piece.color == Color.White:
                        self._castle_move[(0, 0, piece.color)] = \
                                (2, 0)

                 

            self._board.push(move)
            piece.pos = piece.pos_to_move
            transform.pos = piece.pos
