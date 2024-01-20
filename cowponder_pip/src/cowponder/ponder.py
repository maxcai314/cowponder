from textwrap import wrap
import argparse
import subprocess
from random import SystemRandom
from os import path, popen
import requests

cowthoughts_path = "/etc/cowthoughts.txt"
random = SystemRandom() # more random

class NoThoughtsCowHeadEmptyError(Exception):
    def __init__(self, thoughtbook_path):
        super().__init__(message = f"Could not load thoughtbook from {thoughtbook_path}. Please check that it is there, or call update_thoughtbook() to re-download.")
class EvilThoughtsError(Exception):
    def __init__(self, thoughttype):
         super().__init__(message=f"Cow cannot think a {repr(thoughttype)}. Please pass strings.")

class PondererNotReachedError(Exception):
     def __init__(self, error):
          super().__init__(message=f"Failed to download cowthoughts.txt (HTTP error {error}). No changes written to local thoughtbook.")

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

def update_thoughtbook(no_errors=False):
        try:
            response = requests.get('https://max.xz.ax/cowponder/cowthoughts.txt')
            if response.status_code == 200:
                with open(cowthoughts_path, 'w') as f:
                        f.write(response.text)
                return "updated thoughtbook (moo)"
            else:
                raise PondererNotReachedError("failed to download cowthoughts.txt")
        except Exception as e:
            if no_errors:
                 return e
            else:
                 raise e

if __name__ == "__main__":
    ap = argparse.ArgumentParser(prog="cowponder", description="""cowponder generates an ASCII art picture of a cow thinking some
fascinating random thoughts. It word-wraps the message at about 40
columns, and prints the cow saying the given message on standard
output.

cowponder also includes ponder, which provides the same functionality
but without the bovine centerpiece so users may pipe the thoughts to
their contemplative creature of choice.

Different modes can be enabled by passing the appropriate option.
For instance -d will enable Dead mode, were the cow shown appears
to be dead. The complete list of options are:

  Borg     -b
  Dead     -d
  Greedy   -g
  Paranoid -p
  Stoned   -s
  Youthful -y

Outside of the cow modes, there are several additional options. 
Note that these are not available for ponder, since the ponder
is the same software as cowponder and shares a thoughtbook.
  --help,    -h         Print this help message and exit.
  --version, -v         Display the version of cowponder and exit.
  --update,  -u         Update the thoughtbook from the interwebs.
                        This *will* erase any changes you've made; 
                        back up anything you want to keep!
  --add, -a [thought]   Add [thought] to the thoughtbook.""", 
  usage="cowponder [-bdgpsy] [-h] [-v] [-u] [-a <THOUGHT>]", formatter_class=argparse.RawDescriptionHelpFormatter, add_help=False)

    ap.add_argument("-v", "--version", action='store_true', help=argparse.SUPPRESS)
    ap.add_argument("-u", "--update",  action='store_true', help=argparse.SUPPRESS)
    ap.add_argument("-a", "--add", help=argparse.SUPPRESS)
    arglist = 'bdgpsy'
    for i in arglist:
        ap.add_argument("-"+i, action="store_true", help=argparse.SUPPRESS)


    args = vars(ap.parse_args())


    if args['version']:
        print("cowponder version 0.0.3-pip")
        exit()

    if thought := args["add"]:
        add_thoughts(thought)
        exit()

    if args["update"]:
        print(update_thoughtbook(no_errors=True))
        exit()