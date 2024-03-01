from enum import Enum
from typing import Tuple, Dict, Any
import json
import pygame as pg


def load_input_actions_from_file(
        filepath: str
        ) -> Tuple[Any, Dict[str, Enum], Dict[str, int], int]:
    with open(filepath, "r") as f:
        input_actions = json.load(f)

    action_to_keyboard: Dict[str, Enum] = {}
    action_to_mouse: Dict[str, int] = {}

    actions = list(input_actions.keys())
    Actions = Enum("Actions", actions)

    for action in Actions:
        input_tag = input_actions[action.name]
        if input_tag.startswith("K_"):
            action_to_keyboard[action.name] = getattr(
                    pg, 
                    input_actions[action.name]
                    )
        if input_tag.startswith("M_"):
            if input_tag.removeprefix("M_").isnumeric():
                action_to_mouse[action.name] = int(
                        input_tag.removeprefix("M_")
                        )
    

    return Actions,\
            action_to_keyboard,\
            action_to_mouse,\
            len(set(action_to_mouse.values()))
