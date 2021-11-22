import sys

from colorama import Fore, Style, init

sys.path.insert(1, './tests')
from answers import HOUSE_ANSWER

USAGE = "USAGE\n\t./305construction file\n\nDESCRIPTION\n\tfile\tfile describing the tasks\n"



def display_error(string):

    print(Fore.RED + Style.BRIGHT + string + Style.RESET_ALL)
    sys.stderr.write(USAGE)
    exit(84)


'''def invalid_file():
    sys.stderr.write("\nInvalid file\n\n")
    sys.stderr.write(USAGE)
    exit(84)


def invalid_syntax():
    sys.stderr.write("\nInvalid syntax\n\n")
    sys.stderr.write(USAGE)
    exit(84)'''

def display_help():
    #print(HOUSE_ANSWER)
    print(USAGE)
    exit(0)