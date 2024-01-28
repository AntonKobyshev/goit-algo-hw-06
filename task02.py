from collections import deque
from dfs import dfs
from bfs import bfs
from task01 import graph


def format_graph(graph):
    formatted_graph = dict()

    for edge in graph:
        from_node = edge[0]
        to_node = edge[1]

        if from_node in formatted_graph:
            formatted_graph[from_node].append(to_node)
        else:
            formatted_graph[from_node] = [to_node]

    return formatted_graph

def main():
    formatted_graph = format_graph(graph)

    print("dfs steps:")
    dfs(formatted_graph, "Alice")

    print("\nbfs steps:")
    bfs(formatted_graph, deque(["Alice"]))

if __name__ == "__main__":
    main()
