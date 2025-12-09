from cowponder.ponder import add_thoughts, update_thoughtbook, cowponder, print_info, VERSION
import argparse

def main():
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
  --info,    -i         Print thoughtbook information and exit.
  --update,  -u         Update the thoughtbook from the interwebs.
                        This *will* erase any changes you've made; 
                        back up anything you want to keep!
  --add, -a [thought]   Add [thought] to the thoughtbook.""", 
    usage="cowponder [-bdgpsy] [-h] [-v] [-u] [-i] [-a <THOUGHT>]", formatter_class=argparse.RawDescriptionHelpFormatter, add_help=True)

    ap.add_argument("-v", "--version", action='store_true', help=argparse.SUPPRESS)
    ap.add_argument("-u", "--update",  action='store_true', help=argparse.SUPPRESS)
    ap.add_argument("-a", "--add", help=argparse.SUPPRESS)
    ap.add_argument("-i", "--info", action='store_true', help=argparse.SUPPRESS)
    arglist = 'bdgpsy'
    for i in arglist:
        ap.add_argument("-"+i, action="store_true", help=argparse.SUPPRESS)


    args = vars(ap.parse_args())
    prefix = "".join([i for i in arglist if args[i]])

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
    
    print(cowponder(mode=prefix))

if __name__ == "__main__":
    main()