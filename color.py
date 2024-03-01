from enum import Enum

class Color(Enum):
    White = 1
    Black = 2


def opposite_color(color: Color) -> Color:
    if color == Color.White:
        return Color.Black

    return Color.White
