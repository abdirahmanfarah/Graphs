
from graph import Graph
from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):
    # instantiate graph
    # put parents and children in set
    graph = Graph()
    # p_c = set()

    for parent, child in ancestors:
        if parent not in graph.vertices:
            graph.add_vertex(parent)
        if child not in graph.vertices:
            graph.add_vertex(child)

        graph.add_edge(parent, child)
    # for i in ancestors:

    print(graph.vertices)
    # pass


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1))  # 10
