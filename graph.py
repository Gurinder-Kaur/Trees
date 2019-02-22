class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge:
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph:
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        #from_found.edges.append(new_edge)
        #to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        edge_list=[]
        for e in self.edges:
            tri=(e.value,e.node_from.value,e.node_to.value)
            edge_list.append(tri)

        return edge_list

    """def get_adjacency_list(self):
        max=self.max_index()
        adj_list=[None]*(max+1)
        for e in self.edges:
            if adj_list[e.node_from.value]:
                adj_list[e.node_from.value].append((e.node_to.value,e.value))
            else:
                adj_list[e.node_from.value]=[(e.node_to.value,e.value)]

        return adj_list"""

    def get_adjacency_list(self):
        max=self.max_index()
        adj_list=[[] for i in range(max+1)]
        for e in self.edges:
            adj_list[e.node_from.value].append((e.node_to.value,e.value))

        return adj_list


    def get_adjacency_matrix(self):
        max=self.max_index()
        adj_matrix=[[0 for i in range(max+1)]for j in range(max+1)]
        for e in self.edges:
            adj_matrix[e.node_from.value][e.node_to.value]=e.value
        return adj_matrix

    def max_index(self):
        max=-1
        for n in self.nodes:
            if n.value>max:
                max=n.value
        return max

graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print (graph.get_edge_list())
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print (graph.get_adjacency_list())
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print (graph.get_adjacency_matrix())
