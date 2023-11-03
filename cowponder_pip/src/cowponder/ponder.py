from textwrap import wrap
import argparse
import subprocess
from random import SystemRandom
from os import path, popen
cowthoughts_path = "/etc/cowthoughts.txt"
random = SystemRandom() # more random

class NoThoughtsCowHeadEmptyError(Exception):
    def __init__(self, thoughtbook_path):
        super().__init__(message = f"Could not load thoughtbook from {thoughtbook_path}. Please check that it is there, or call update_thoughtbook() to re-download.")
class EvilThoughtsError(Exception):
    def __init__(self, thoughttype):
         super().__init__(message=f"Cow cannot think a {repr(thoughttype)}. Please pass strings.")

def ponder(max_width: int|None =None, no_error: bool=False) -> str|list[str]:
    """gets a random thought from the thoughtbook.

    Args:
        max_width (int, optional): The maximum line length (in characters) of the thought. If None, no wrapping will be performed. Defaults to None.
        no_error (bool, optional): if True, returns 'No thoughts, head empty' instead of raising an error if no thoughtbook is found. Defaults to False.

    Raises:
        NoThoughtsCowHeadEmptyError: if the thoughtbook file is missing.

    Returns:
        str | list[str]: the randomly selected thought. If wrapping was requested, a list of lines is returned (no final newlines).
    """
    if not path.exists(cowthoughts_path):
        if no_error: return "No thoughts, head empty."
        else: raise NoThoughtsCowHeadEmptyError(cowthoughts_path)
    with open(cowthoughts_path) as thinkbook:
        thought = random.choice([thought for thought in thinkbook.read().split("\n") if thought])
    thought = wrap(thought, width=max_width)
    return thought

def _verify_thoughtbook(path, no_error=False):
    if not path.exists(cowthoughts_path):
        if no_error: return NoThoughtsCowHeadEmptyError(cowthoughts_path)
        else: raise NoThoughtsCowHeadEmptyError(cowthoughts_path)
    else: return True

def _verify_thoughts(thoughts):
    for thought in thoughts:
         if '\n' in thoughts:
              raise EvilThoughtsError('\n')
         if not isinstance(thought, str):
              raise EvilThoughtsError(type(thought))

def add_thoughts(*thoughts):
    """adds all thoughts passed to the thoughtbook.

    Args:
        *thoughts (str): pass any number of strings to be added to the thoughtbook. Thoughts may not include a newline character.
    """
    _verify_thoughtbook(cowthoughts_path)
    _verify_thoughts(thoughts)
    with open(cowthoughts_path, "a") as f:
        print(thoughts, file=f, sep="\n")