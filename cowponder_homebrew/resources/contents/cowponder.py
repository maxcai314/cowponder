#!/usr/bin/env python3

import argparse
import subprocess
from random import SystemRandom
from os import path, popen

cowthoughts_path = path.join(popen("brew --prefix").read().strip(), "etc", "cowthoughts.txt")

random = SystemRandom() # more random
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
	subprocess.run(["brew", "info", "cowponder"])
	# print("cowponder version 0.0.1")
	exit()

if thought := args["add"]:
        subprocess.run(["ponder", "--add", thought])
        exit()

if args["update"]:
        subprocess.run(["ponder", "--update"])
        exit()

thought = subprocess.check_output("ponder", shell=True, stderr=subprocess.STDOUT, text=True)

prefix = "".join([i for i in arglist if args[i]])
if len(prefix) > 0:
	subprocess.run(["cowthink", "-"+prefix, thought])
else:
	subprocess.run(["cowthink", thought])
