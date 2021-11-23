from get_graph import find_by_name


from utils import *

def print_res(r):
    print(r)




def get_duration(graph):
    duration = 0





def run_algo(graph):
    visited = 0
    queue = []
    for task in graph:
        if task.indegree == 0:
            queue.append(task)
    if len(queue) is 0:
        display_error("THE GRAPH YOU GAVE IS NOT DAG!")

    get_duration(graph)
