from board_cursor import BoardCursor, CursorState
from piece import PieceState, Piece
from engine.system import System
from engine.entity import Entity
from engine.animation import Animation

class StateSystem(System):
    def apply(self, entity: Entity) -> None:
        cursor = entity.get_component(BoardCursor)
        if cursor:
            animation = entity.get_component(Animation)
            if animation:
                if cursor.state == CursorState.Free or\
                        cursor.state == CursorState.TryFocus:
                            animation.set_animation("IDLE")
                elif cursor.state == CursorState.Focused or\
                        cursor.state == CursorState.TryRelease:
                            animation.set_animation("FOCUSED")


        piece = entity.get_component(Piece)
        if piece:
            animation = entity.get_component(Animation)
            if animation:
                if piece.state == PieceState.Free:
                    animation.set_animation("IDLE")
                elif piece.state == PieceState.Focused:
                    animation.set_animation("FOCUSED")
