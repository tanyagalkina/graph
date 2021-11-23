from get_graph import find_by_name
import operator
from get_graph import Task

from utils import *

######TODO: JUST WRITE THE PRINT
def print_res(r):
    print(r)


def get_duration(graph):
    durations = []
    for task in graph:
        durations.append(task.begin_start + task.duration)
    return max(durations)


def algo_function(visited, queue, graph):


    if visited != len(graph) and len(queue) is 0:
        display_error("THE GRAPH YOU GAVE IS NOT DAG!")

    for t in queue:
        t.indegree -= 1 #setting it to -1 so we dont consider the node anymore
        visited +=1
        if t.begin_start is -1:
            t.begin_start = 0 # for the first iteration only
        for sl in t.slaves:
            slave = find_by_name(sl, graph)
            slave.indegree -= 1
            if slave.begin_start < (t.begin_start + t.duration):
                slave.begin_start = t.begin_start + t.duration
            if slave.indegree is 0:
                queue.append(slave)
    queue.pop(0)
    if queue:
        algo_function(visited, queue, graph)


def set_begin_end(task, graph, end):

    if task.slaves:
        earliest = -1
        starts = []
        for sl in task.slaves:
            slave = find_by_name(sl, graph)
            starts.append(slave.begin_start)
        if starts:
            earliest = min(starts)

        if earliest is not -1 and (task.begin_start + task.duration) < earliest:
            task.begin_end = earliest - task.duration
    else:
        if (task.begin_start + task.duration) < end:
            task.begin_end = end - task.duration



def run_algo(graph):
    visited = 0
    queue = []
    for task in graph:
        if task.indegree == 0:
           queue.append(task)
    algo_function(visited, queue, graph)

    project_duration = get_duration(graph)

    for task in graph:
        set_begin_end(task, graph, project_duration)
    sorted_graph = sorted(graph, key=lambda k: (k.begin_start, k.duration, k.nickname))

    print_res(sorted_graph)

