class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if not vertex in self.adj_list:
            self.adj_list[vertex] = []
            return True
        else:
            return False

    def add_edge(self, start, end):
        if start in self.adj_list and end in self.adj_list:
            self.adj_list[start].append(end)
            self.adj_list[end].append(start)

            return True

        return False

    def remove_edge(self, start, end):
        if start in self.adj_list and end in self.adj_list:
            try:
                self.adj_list[start].remove(end)
                self.adj_list[end].remove(start)

            except ValueError:
                pass

            return True
        return False

    def remove_vertex(self, vertex):
        if not vertex in self.adj_list:
            return False

        for other_vertex in self.adj_list[vertex]:
            self.adj_list[other_vertex].remove(vertex)

        del self.adj_list[vertex]

        return True


my_graph = Graph()

my_graph.add_vertex("A")

my_graph.print_graph()


"""
    EXPECTED OUTPUT:
    ----------------
    A : []

"""


my_graph = Graph()

my_graph.add_vertex(1)
my_graph.add_vertex(2)

my_graph.add_edge(1, 2)

my_graph.print_graph()


"""
    EXPECTED OUTPUT:
    ----------------
    1 : [2]
    2 : [1]

"""


my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")

my_graph.add_edge("A", "B")
my_graph.add_edge("B", "C")
my_graph.add_edge("C", "A")

print("Graph before remove_edge():")
my_graph.print_graph()


my_graph.remove_edge("A", "C")


print("\nGraph after remove_edge():")
my_graph.print_graph()


"""
    EXPECTED OUTPUT:
    ----------------
    Graph before remove_edge():
    A : ['B', 'C']
    B : ['A', 'C']
    C : ['B', 'A']

    Graph after remove_edge():
    A : ['B']
    B : ['A', 'C']
    C : ['B']
    
"""


my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")

my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "D")
my_graph.add_edge("C", "D")


print("Graph before remove_vertex():")
my_graph.print_graph()


my_graph.remove_vertex("D")


print("\nGraph after remove_vertex():")
my_graph.print_graph()


"""
EXPECTED OUTPUT:
----------------
    Graph before remove_vertex():
    A : ['B', 'C', 'D']
    B : ['A', 'D']
    C : ['A', 'D']
    D : ['A', 'B', 'C']

    Graph after remove_vertex():
    A : ['B', 'C']
    B : ['A']
    C : ['A']

"""
