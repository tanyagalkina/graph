import sys

USAGE = "USAGE\n\t./305construction file\n\nDESCRIPTION\n\tfile\tfile describing the tasks"

def invalid_graph():
    sys.stderr.write("\nInvalid graph\n\n")
    sys.stderr.write(USAGE)
    exit(84)


def invalid_file():
    sys.stderr.write("\nInvalid file\n\n")
    sys.stderr.write(USAGE)
    exit(84)


def invalid_syntax():
    sys.stderr.write("\nInvalid syntax\n\n")
    sys.stderr.write(USAGE)
    exit(84)


def display_help():
    print(USAGE)
    exit(0)