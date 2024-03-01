import pygame as pg
import json

from typing import Dict, Any

def load_assets_from_config(filepath: str) -> Dict[str, Any]:
    with open(filepath, "r") as f:
        config_file = json.load(f)

    assets: Dict[str, pg.mixer.Sound | pg.surface.Surface] = {}

    for ae in list(config_file.keys()):
        if ae.startswith("AUDIO_"):
            assets[ae] = pg.mixer.Sound(config_file[ae])
        elif ae.startswith("IMAGE_"):
            assets[ae] = pg.image.load(config_file[ae])

    return assets
