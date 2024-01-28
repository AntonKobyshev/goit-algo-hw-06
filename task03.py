from task01 import graph
from dijkstra import dijkstra

def format_graph(graph):
    formatted_graph = dict()

    for edge in graph:
        from_node = edge[0]
        to_node = edge[1]
        weight = edge[2]["weight"]

        if from_node in formatted_graph:
            formatted_graph[from_node][to_node] = weight
        else:
            formatted_graph[from_node] = {to_node: weight}

    return formatted_graph


def main():
    formatted_graph = format_graph(graph)
    start_node = "Alice"
    distances: dict = dijkstra(formatted_graph, start_node)

    print(f"Distances from {start_node} to nodes\n")
    print(f"| {'To node':^16} | {'Distance':^16} |")
    print(f"| {'-'*16} | {'-'*16} |")

    for node in distances.keys():
        print(f"| {node:^16} | {distances[node]:^16} |")

if __name__ == "__main__":
    main()