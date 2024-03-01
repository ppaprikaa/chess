from engine.animation_system import Animator
from engine.engine import Engine
from engine.input_system import InputSystem
from engine.input_actions_loading import load_input_actions_from_file
from engine.render_system import Renderer
from engine.asset_loading import load_assets_from_config
import pygame as pg
import chess
from color import Color
from movement_system import MovementSystem
from piece_capture_system import PieceCaptureSystem
from chess_system import ChessSystem
from control_system import ControlSystem
from board_cursor import BoardCursor
from state_system import StateSystem
from create_gameplay_entities import create_cursor,\
        create_pawn, create_rook, create_square,\
        create_knight, create_bishop,\
        create_queen, create_king


def gameplay_scene(engine: Engine, orientation: Color):
    actions, action_to_kbd, action_to_mouse, _ = \
            load_input_actions_from_file("config/input_actions.json")
    
    if orientation == Color.White:
        scene_tag = "GAMEPLAY_WHITE"
    else:
        scene_tag = "GAMEPLAY_BLACK"

    start_scene = engine.add_scene(scene_tag)

    context = engine.context()
    em = start_scene.entity_manager()
    assets = load_assets_from_config("config/assets.json")

    cursor = create_cursor(em, assets)

    def create_board(orientation: Color) -> None:
        if orientation == Color.White:
            colorA = Color.White
            colorB = Color.Black
        else:
            colorA = Color.Black
            colorB = Color.White


        for i in range(0, 8):
            for j in range(0, 8):
                if j % 2 == 0 and i % 2 == 0 or i % 2 != 0 and j % 2 != 0:
                    color = Color.White
                else:
                    color = Color.Black
                create_square(
                        em,
                        assets,
                        pos=pg.Vector2(i, j), 
                        size=pg.Vector2(1, 1),
                        color=color
                        )

        for i in range(0, 8):
            create_pawn(
                    em,
                    assets,
                    pos=pg.Vector2(i, 6),
                    size=pg.Vector2(1, 1),
                    color=colorA
                    )
            create_pawn(
                    em,
                    assets,
                    pos=pg.Vector2(i, 1),
                    size=pg.Vector2(1, 1),
                    color=colorB
                    )

        create_rook(
                em,
                assets,
                pos=pg.Vector2(0, 7),
                size=pg.Vector2(1, 1),
                color=colorA
                )
        create_rook(
                em,
                assets,
                pos=pg.Vector2(7, 7),
                size=pg.Vector2(1, 1),
                color=colorA
                )
        create_rook(
                em,
                assets,
                pos=pg.Vector2(0, 0),
                size=pg.Vector2(1, 1),
                color=colorB
                )
        create_rook(
                em,
                assets,
                pos=pg.Vector2(7, 0),
                size=pg.Vector2(1, 1),
                color=colorB
                )
        create_knight(
                em,
                assets,
                pos=pg.Vector2(1, 0),
                size=pg.Vector2(1, 1),
                color=colorB
                )
        create_knight(
                em,
                assets,
                pos=pg.Vector2(6, 0),
                size=pg.Vector2(1, 1),
                color=colorB
                )
        create_knight(
                em,
                assets,
                pos=pg.Vector2(1, 7),
                size=pg.Vector2(1, 1),
                color=colorA
                )
        create_knight(
                em,
                assets,
                pos=pg.Vector2(6, 7),
                size=pg.Vector2(1, 1),
                color=colorA
                )
        create_bishop(
                em,
                assets,
                pos=pg.Vector2(2, 7),
                size=pg.Vector2(1, 1),
                color=colorA
                )
        create_bishop(
                em,
                assets,
                pos=pg.Vector2(5, 7),
                size=pg.Vector2(1, 1),
                color=colorA
                )
        create_bishop(
                em,
                assets,
                pos=pg.Vector2(2, 0),
                size=pg.Vector2(1, 1),
                color=colorB
                )
        create_bishop(
                em,
                assets,
                pos=pg.Vector2(5, 0),
                size=pg.Vector2(1, 1),
                color=colorB
                )
        if orientation == Color.White:
            create_queen(
                    em,
                    assets,
                    pos=pg.Vector2(3, 7),
                    size=pg.Vector2(1, 1),
                    color=colorA
                    )
            create_queen(
                    em,
                    assets,
                    pos=pg.Vector2(3, 0),
                    size=pg.Vector2(1, 1),
                    color=colorB
                    )
            create_king(
                    em,
                    assets,
                    pos=pg.Vector2(4, 7),
                    size=pg.Vector2(1, 1),
                    color=colorA
                    )
            create_king(
                    em,
                    assets,
                    pos=pg.Vector2(4, 0),
                    size=pg.Vector2(1, 1),
                    color=colorB
                    )
        else:
            create_queen(
                    em,
                    assets,
                    pos=pg.Vector2(4, 7),
                    size=pg.Vector2(1, 1),
                    color=colorA
                    )
            create_queen(
                    em,
                    assets,
                    pos=pg.Vector2(4, 0),
                    size=pg.Vector2(1, 1),
                    color=colorB
                    )
            create_king(
                    em,
                    assets,
                    pos=pg.Vector2(3, 7),
                    size=pg.Vector2(1, 1),
                    color=colorA
                    )
            create_king(
                    em,
                    assets,
                    pos=pg.Vector2(3, 0),
                    size=pg.Vector2(1, 1),
                    color=colorB
                    )

            
    cursor_component = cursor.get_component(BoardCursor)
    if not cursor_component:
        exit(0)

    board = chess.Board()


    create_board(orientation)

    render_sys = Renderer(
            context.camera(), 
            context.window().surface(),
            context.window().tile_size()
            )

    input_system = InputSystem(actions, action_to_kbd, action_to_mouse)
    animation_system = Animator()
    control_system = ControlSystem(start_scene.context())
    movement_system = MovementSystem(board, cursor_component, orientation)
    state_system = StateSystem()
    chess_system = ChessSystem(context, board, orientation)
    piece_capture_system = PieceCaptureSystem(board, orientation)

    start_scene.add_system(piece_capture_system)
    start_scene.add_system(input_system)
    start_scene.add_system(state_system)
    start_scene.add_system(chess_system)
    start_scene.add_system(render_sys)
    start_scene.add_system(control_system)
    start_scene.add_system(movement_system)
    start_scene.add_system(animation_system)
