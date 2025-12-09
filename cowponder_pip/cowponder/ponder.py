from textwrap import wrap
import argparse
from random import SystemRandom
from os import path, makedirs
import io
import requests
import sys
from platformdirs import site_data_dir, user_data_dir

random = SystemRandom() # more random

APPNAME = "cowponder"
VERSION = "cowponder version 0.1.8 (pip)"

def _get_site_thoughtbook_path() -> str:
    """Get the system-wide thoughtbook path."""
    return path.join(site_data_dir(APPNAME), "cowthoughts.txt")

def _get_user_thoughtbook_path() -> str:
    """Get the fallback user-local thoughtbook path."""
    return path.join(user_data_dir(APPNAME), "cowthoughts.txt")

def get_cowthoughts_path() -> str:
    """Get the path to cowthoughts.txt, preferring system-wide if it exists, else user-local."""
    site_path = _get_site_thoughtbook_path()
    user_path = _get_user_thoughtbook_path()
    
    # Prefer system-wide if it exists
    if path.exists(site_path):
        return site_path
    elif path.exists(user_path):
        return user_path
    else:
        # Neither exists - return site path as default (will lead to error)
        return site_path

class NoThoughtsCowHeadEmptyError(Exception):
    def __init__(self, thoughtbook_path):
        super().__init__(f"Could not load thoughtbook from {thoughtbook_path}. Please check that it is there, or call update_thoughtbook() to re-download.")

class EvilThoughtsError(Exception):
    def __init__(self, thoughttype):
         super().__init__(f"Cow cannot think a {repr(thoughttype)}. Please pass strings.")

class PondererNotReachedError(Exception):
     def __init__(self, error):
          super().__init__(f"Failed to download cowthoughts.txt (HTTP error {error}). No changes written to local thoughtbook.")

def _handle_no_thoughts(cowthoughts_path, max_width, no_error):
    if no_error:
        if max_width is None:
            return "No thoughts, head empty. Please run 'cowponder --update' to download the default thoughtbook."
        else:
            return [
                "No thoughts, head empty.",
                "Please run 'cowponder --update'",
                "to download the default thoughtbook."
            ]  # list of lines
    else:
        raise NoThoughtsCowHeadEmptyError(cowthoughts_path)

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
    cowthoughts_path = get_cowthoughts_path()
    if not path.exists(cowthoughts_path):
        return _handle_no_thoughts(cowthoughts_path, max_width, no_error)
    with io.open(cowthoughts_path, encoding="utf-8") as thinkbook:
        thoughts = thinkbook.read().splitlines()
        if not thoughts:
            return _handle_no_thoughts(cowthoughts_path, max_width, no_error)
        thought = random.choice(thoughts)
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
    
    thought = ponder(max_width=width, no_error=True)
    if isinstance(thought, str):
        thought = [thought]
    truewidth = max(map(len, thought))
    out = ' ' + '_'*(truewidth+2) + '\n'
    out += '\n'.join([f"( {i.ljust(truewidth)} )" for i in thought])
    out += '\n '+'-'*(truewidth+2) + '\n'
    return out+cow(*args)

def _verify_thoughtbook(cowthoughts_path, no_error=False):
    if not path.exists(cowthoughts_path):
        if no_error: return NoThoughtsCowHeadEmptyError(cowthoughts_path)
        else: raise NoThoughtsCowHeadEmptyError(cowthoughts_path)
    else: return True

def _verify_thought(thought):
    if '\n' in thought:
        raise EvilThoughtsError('\n')
    if not isinstance(thought, str):
        raise EvilThoughtsError(type(thought))

def add_thoughts(*thoughts):
    """adds all thoughts passed to the thoughtbook.

    Args:
        *thoughts (str): pass any number of strings to be added to the thoughtbook. Thoughts may not include a newline character.
    """
    initialize_thoughtbook()  # ensure thoughtbook path exists
    cowthoughts_path = get_cowthoughts_path()
    _verify_thoughtbook(cowthoughts_path)
    with io.open(cowthoughts_path, "a", encoding="utf-8") as f:
        for thought in thoughts:
            _verify_thought(thought)
            print(thought, file=f, end='\n')

def initialize_thoughtbook():
    """
    initializes a thoughtbook if not present.
    calling this function may change the result
    of subsequent calls to get_cowthoughts_path().
    """
    # First try system-wide location
    site_path = _get_site_thoughtbook_path()
    site_dir = path.dirname(site_path)
    try:
        if not path.exists(site_dir):
            makedirs(site_dir, exist_ok=True)
        if not path.exists(site_path):
            with io.open(site_path, 'w', encoding="utf-8") as f:
                pass  # create empty thoughtbook
            return
    except (IOError, OSError, PermissionError):
        # Failed to write to system location, fall back to user location
        user_path = _get_user_thoughtbook_path()
        user_dir = path.dirname(user_path)
        print(f"Warning: Could not write to system-wide location {site_path}", file=sys.stderr)
        print(f"Permission denied. If you want a system-wide thoughtbook, try running with elevated privileges.", file=sys.stderr)
        print(f"\nFalling back to user-local location: {user_path}", file=sys.stderr)
        if not path.exists(user_dir):
            makedirs(user_dir, exist_ok=True)
        if not path.exists(user_path):
            with io.open(user_path, 'w', encoding="utf-8") as f:
                pass  # create empty thoughtbook
            return

def print_info():
    """Print information about the thoughtbook location and status."""
    site_path = _get_site_thoughtbook_path()
    user_path = _get_user_thoughtbook_path()
    
    if path.exists(site_path):
        thoughtbook_path = site_path
        print(f"system-wide thoughtbook: {thoughtbook_path}")
    elif path.exists(user_path):
        thoughtbook_path = user_path
        print(f"user-local thoughtbook: {thoughtbook_path}")
    else:
        print("No thoughtbook found.")
        print("Please run 'cowponder --update' to download the default thoughtbook.")
        return
    with io.open(thoughtbook_path, encoding='utf-8') as f:
        print(f"thought count: {len(f.read().splitlines())}")


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
        initialize_thoughtbook()  # ensure thoughtbook path exists

        response = requests.get('https://max.xz.ax/cowponder/cowthoughts.txt')
        if response.status_code != 200:
            raise PondererNotReachedError(f"HTTP {response.status_code}")
        
        content = response.content.decode('utf-8')
        
        cowthoughts_path = get_cowthoughts_path()
        with io.open(cowthoughts_path, 'w', encoding="utf-8") as f:
            f.write(content)
        return "updated thoughtbook (moo)"
    except Exception as e:
        if no_errors:
            return e
        else:
            raise e

def main():
    ap = argparse.ArgumentParser(prog="ponder", description="provides the functionality of `cowponder` minus the bovine centerpiece, allowing users to pipe the output to their contemplative creature of choice.")
    ap.add_argument("-v", "--version", action='store_true', help="Print version information and exit.")
    ap.add_argument("-u", "--update",  action='store_true', help="Update thoughtbook from the server. This *will* overwrite any changes made with cowponder --add.")
    ap.add_argument("-i", "--info", action='store_true', help="Print thoughtbook information and exit.")
    ap.add_argument("-a", "--add", help="Add custom thought to thoughtbook.")

    args = vars(ap.parse_args())

    if args['version']:
        print(VERSION)
        exit()

    if args['info']:
        print_info()
        exit()

    thought = args['add']
    if thought:
        add_thoughts(thought)
        exit()

    if args["update"]:
        print(update_thoughtbook(no_errors=True))
        exit()

    print(ponder(no_error=True))

if __name__ == "__main__":
    main()