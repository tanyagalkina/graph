import csv
import os
import operator
import sys
from utils import *
import colorama
from colorama import Fore, Style, init


def find_by_name(name, graph):
    for s in graph:
        if s.name == name:
            return s

class Task:
    def __init__(self, line, graph):
        self.nickname = line[0]
        line.pop()
        self.name = line[0]
        line.pop()
        self.duration = line[0]
        line.pop()
        self.masters = line

        self.slaves = []
        if find_by_name(self.name, graph):
            display_error('CANNOT GET TWO IDENTICAL OBJECTS')
        graph.append(self)
        #self.build_strings = []
        #self.level = -1
        #self.stage = -1
        #self.built = False



def get_graph(filename):

    graph = []
    count = 0
    try:
        with open(filename, newline='') as tasks:
            lines = csv.reader(tasks, delimiter=';')

            for line in lines:
                if len(line) is not 0:
                    count += 1
                    print(line)
                    Task(line, graph)
            if count is 0:
                display_error('THE FILE YOU PROVIDED IS EMPTY')

    except FileNotFoundError:
        display_error("FILE NOT FOUND")
    except OSError:
        display_error("OS ERROR")
        #print(f"OS error occurred trying to open {filename}", file=sys.stderr)
        #sys.exit(84)
    except Exception as err:
        print(f"Unexpected error opening {filename} is", repr(err))
        sys.exit(84)

    return graph