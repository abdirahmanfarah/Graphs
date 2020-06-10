
from graph import Graph
from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):
    # instantiate graph
    # put parents and children in set
    graph = Graph()
    final_list = []

    # loop through ancestors list and input tuples into graph vertices
    ancestors = [x[::-1] for x in ancestors]
    for parent, child in ancestors:
        if parent not in graph.vertices:
            graph.add_vertex(parent)
        if child not in graph.vertices:
            graph.add_vertex(child)

        graph.add_edge(parent, child)

    # print(graph.vertices)

    # loop through vertices and get it's neightbors
    all_lists = graph.dfs(starting_node)

    # if list is has no parents, return 1
    if len(all_lists) == 0:
        return -1
    # find max length of item in list
    max_len = max(len(x) for x in all_lists)

    # loop through all_lists to find the lists that have the biggest length
    for i in range(0, len(all_lists)):
        curr_list = all_lists[i]
        if len(curr_list) == max_len:
            final_list.append(curr_list)

    # if more than 1 list has max_length, find the smallest number
    if len(final_list) > 1:
        smallest = final_list[0][-1]
        for i in final_list:
            if i[-1] < smallest:
                smallest = i[-1]
                return smallest

    return final_list[0][-1]


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 10))  # 10


# for parent, child in ancestors:
#     #     if parent not in graph.vertices:
#     #         graph.add_vertex(parent)
#     #     if child not in graph.vertices:
#     #         graph.add_vertex(child)

#     #     graph.add_edge(child, parent)
#  ancestors = [x[::-1] for x in ancestors]
