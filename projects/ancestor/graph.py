"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertext
            v = q.dequeue()

            # If vertex has not been visited
            if v not in visited:
                # Visit it
                print(v)

                # Mark it as visited
                visited.add(v)

                # Add all its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Used stack, LIFO
        # We need an empty stack to store our visited nodes
        s = Stack()
        # put ID of starting vertext
        s.push(starting_vertex)

        # Set to store visited verts
        visited = set()

        # While the stack is not empty
        while s.size() > 0:
            # pop the first verts
            v = s.pop()

            # Check to see if v has been visited
            if v not in visited:
                # Print it
                print(v)

                # Mark it as visited
                visited.add(v)

                # Add all its neighbors to the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check base case
        if visited is None:
            return

        visited.add(starting_vertex)
        print(starting_vertex)

        for next_vert in self.vertices[starting_vertex]:
            if next_vert not in visited:
                self.dft_recursive(next_vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        # start = starting_vertex
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() >= 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the path
            print(path)
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:
                visited.add(v)
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                else:
                    # Then add A PATH TO its neighbors to the back of the queue
                    for next_vert in self.get_neighbors(v):
                        new_path = list(path)
                        new_path.append(next_vert)
                        # APPEND THE NEIGHOR TO THE BACK
                        q.enqueue(new_path)

    def dfs(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])

        all_list = []

        while s.size() > 0:
            path = s.pop()
            v = path[-1]
            for next_vert in self.get_neighbors(v):
                new_path = list(path)
                new_path.append(next_vert)
                s.push(new_path)
                all_list.append(new_path)
        return all_list

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Check base case
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(starting_vertex)
        path = path + [starting_vertex]
        # loop through nodes
        if starting_vertex == destination_vertex:
            return path

        for next_vert in self.get_neighbors(starting_vertex):
            if next_vert not in visited:
                new_path = self.dfs_recursive(
                    next_vert, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path
        return None

        # for edge in self.vertices[starting_vertex]:
        #     if edge not in visited:
        #         self.dft_recursive(edge, visited)


# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('1', '0')
# graph.add_edge('0', '3')
# graph.add_edge('3', '0')
# # graph.add_edge('0', '4')

# print(graph.vertices)
# graph.bft('0')
# print('--------')
# graph.dft('0')

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

#     '''
#     Should print:
#         {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     '''
    print(graph.vertices)

#     '''
#     Valid BFT paths:
#         1, 2, 3, 4, 5, 6, 7
#         1, 2, 3, 4, 5, 7, 6
#         1, 2, 3, 4, 6, 7, 5
#         1, 2, 3, 4, 6, 5, 7
#         1, 2, 3, 4, 7, 6, 5
#         1, 2, 3, 4, 7, 5, 6
#         1, 2, 4, 3, 5, 6, 7
#         1, 2, 4, 3, 5, 7, 6
#         1, 2, 4, 3, 6, 7, 5
#         1, 2, 4, 3, 6, 5, 7
#         1, 2, 4, 3, 7, 6, 5
#         1, 2, 4, 3, 7, 5, 6
#     '''
    graph.bft(1)

#     '''
#     Valid DFT paths:
#         1, 2, 3, 5, 4, 6, 7
#         1, 2, 3, 5, 4, 7, 6
#         1, 2, 4, 7, 6, 3, 5
#         1, 2, 4, 6, 3, 5, 7
#     '''
    # graph.dft(1)
    graph.dft_recursive(1)

#     '''
#     Valid BFS path:
#         [1, 2, 4, 6]
#     '''
    print(graph.bfs(1, 6))

#     '''
#     Valid DFS paths:
#         [1, 2, 4, 6]
#         [1, 2, 4, 7, 6]
#     '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
