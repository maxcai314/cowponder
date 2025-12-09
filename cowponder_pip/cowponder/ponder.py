from textwrap import wrap
import argparse
from random import SystemRandom
from os import path, popen
import requests

# TODO: could make configurable and use a ~/.cowponder/cowthoughts.txt path
# instead of global /etc path if the user has no write permissions to /etc
cowthoughts_path = "/etc/cowthoughts.txt"
random = SystemRandom() # more random

class NoThoughtsCowHeadEmptyError(Exception):
    def __init__(self, thoughtbook_path):
        super().__init__(f"Could not load thoughtbook from {thoughtbook_path}. Please check that it is there, or call update_thoughtbook() to re-download.")

class EvilThoughtsError(Exception):
    def __init__(self, thoughttype):
         super().__init__(f"Cow cannot think a {repr(thoughttype)}. Please pass strings.")

class PondererNotReachedError(Exception):
     def __init__(self, error):
          super().__init__(f"Failed to download cowthoughts.txt (HTTP error {error}). No changes written to local thoughtbook.")

def ponder(max_width=None, no_error=False):
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
    if max_width is None:
         return thought
    return wrap(thought, width=max_width)

def cow(eyes="oo", tongue=" "):
    return (
f"""      o  ^__^             
       o ({eyes})\________    
         (__)\        )\/\\
          {tongue}   ||----w |   
              ||     ||   """)

def cowponder(mode="", width=40):
    faces = dict(
       b=("==", " "),
       d=("XX", "U"),
       g=("$$", " "),
       p=("@@", " "),
       s=("**", "U"),
       y=("..", " ")
    )
    if mode:
        args = faces[mode[-1]]
    else:
        args = ("oo", " ")
    
    thought = ponder(width, no_error=True)
    truewidth = max(map(len, thought))
    out = ' ' + '_'*(truewidth+2) + '\n'
    out += '\n'.join([f"( {i.ljust(truewidth)} )" for i in thought])
    out += '\n '+'-'*(truewidth+2) + '\n'
    return out+cow(*args)

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

def update_thoughtbook(no_errors=False):
    """updates the thoughtbook from the server.

    Args:
        no_errors (bool, optional): if True, exceptions will be returned instead of raised. Defaults to False.

    Raises:
        PondererNotReachedError: indicates failure to connect to the server and download the thoughtbook.

    Returns:
        str | Exception: a success message or an exception. 
    """
    try:
        response = requests.get('https://max.xz.ax/cowponder/cowthoughts.txt')
        if response.status_code == 200:
            with open(cowthoughts_path, 'w') as f:
                f.write(response.content.decode('utf-8'))
            return "updated thoughtbook (moo)"
        else:
            raise PondererNotReachedError("failed to download cowthoughts.txt")
    except Exception as e:
        if no_errors:
            return e
        else:
            raise e

def main():
    ap = argparse.ArgumentParser(prog="ponder", description="provides the functionality of `cowponder` minus the bovine centerpiece, allowing users to pipe the output to their contemplative creature of choice.")
    ap.add_argument("-v", "--version", action='store_true', help="Print version information and exit.")
    ap.add_argument("-u", "--update",  action='store_true', help="Update thoughtbook from the server. This *will* overwrite any changes made with cowponder --add.")
    ap.add_argument("-a", "--add", help="Add custom thought to thoughtbook.")

    args = vars(ap.parse_args())

    if args['version']:
        print("cowponder version 0.0.3-pip")
        exit()

    thought = args['add']
    if thought:
        add_thoughts(thought)
        exit()

    if args["update"]:
        print(update_thoughtbook(no_errors=True))
        exit()

    print(ponder())

if __name__ == "__main__":
    main()