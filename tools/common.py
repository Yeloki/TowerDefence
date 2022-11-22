import os
from pathlib import Path
from typing import List
from secrets import token_hex


def get_files_from_path(path: Path) -> List[Path]:
    result = []
    for file in path.iterdir():
        file = Path(file)
        if file.is_file():
            result.append(file)
    return result


def get_dirs_from_path(path: Path) -> List[Path]:
    result = []
    for file in path.iterdir():
        file = Path(file)
        if file.is_dir():
            result.append(file)
    return result


def find_settings() -> Path:
    pwd = Path(os.path.abspath(os.path.curdir))
    while pwd != pwd.parent:
        for path in pwd.iterdir():
            if path.is_file() and path.name == 'settings.yaml':
                return path
        pwd = pwd.parent
    raise RuntimeError("Cannot find settings.yaml file, "
                       "try to run script from another directory")


def get_base_path() -> Path:
    from .settings import SETTINGS
    project_name = SETTINGS['project']['name']
    pwd = Path(os.path.abspath(os.path.curdir))
    while pwd != pwd.parent:
        for path in pwd.iterdir():
            if path.is_dir() and path.name == project_name:
                return path
        pwd = pwd.parent
    raise RuntimeError(f"Cannot find {project_name} directory,\n"
                       "rename directory or change settings.yaml file"
                       "and try again")


def generate_uid() -> str:
    return token_hex(16)
