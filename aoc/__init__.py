import os
import subprocess
from datetime import datetime
from pathlib import Path

import requests  # type: ignore[import]


def find_repo_root(start_path: str = ".") -> str:
    try:
        git_root = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=start_path,
            stderr=subprocess.DEVNULL,
            universal_newlines=True,
        ).strip()
        return os.path.normpath(git_root)
    except subprocess.CalledProcessError as e:
        raise FileNotFoundError("Could not find git repository root") from e


repo_root = find_repo_root(os.getcwd())

_SESSION_FILE_NAME = f"{repo_root}/session.txt"
_YEAR_FILE_NAME = f"{repo_root}/year.txt"


def _set_read_file(filename: str, default: str | None = None) -> str | None:
    try:
        with open(filename) as file:
            return file.read()
    except FileNotFoundError:
        if default:
            with open(filename, "w") as file:
                file.write(default)
                return default
        return None


def get_input(day: int, year: int | None = None, overwrite: bool = False) -> str:
    """
    Usage:
    ```python
    import aoc
    data_rows = aoc.get_input(5).splitlines()
    ```python
    """
    if year is None:
        _YEAR = _set_read_file(_YEAR_FILE_NAME)
        if not _YEAR:
            _YEAR = _set_read_file(_YEAR_FILE_NAME, str(datetime.now().year))
            assert _YEAR is not None
        year = int(_YEAR.strip())

    Path(f"{repo_root}/data").mkdir(exist_ok=True)

    file_name = f"{repo_root}/data/{year}_{day}.txt"
    data = None if overwrite else _set_read_file(file_name)
    if not data:
        response = requests.get(
            f"https://adventofcode.com/{year}/day/{day}/input",
            cookies={"session": SESSION},
        )
        if not response.ok:
            if response.status_code == 404:
                raise FileNotFoundError(response.text)
            raise RuntimeError(
                f"Request failed, code: {response.status_code}, message: {response.content}"
            )
        data = _set_read_file(file_name, response.text[:-1])
    if data is None:
        raise FileNotFoundError(f"Data could not be fetched for day {day}")
    return data


SESSION = _set_read_file(_SESSION_FILE_NAME)
if not SESSION:
    SESSION = _set_read_file(_SESSION_FILE_NAME, input("Enter your session cookie: "))
assert SESSION is not None
SESSION = SESSION.strip()
