class Node:
    def __init__(self,value):
        self.value=value
        self.edges=[]
        self.visited=False

class Edge:
    def __init__(self,value,node_from,node_to):
        self.value=value
        self.node_from=node_from
        self.node_to=node_to

class Graph:
    def __init__(self,nodes=None,edges=None):
        self.nodes=nodes or []
        self.edges=edges or []
        self.node_names=[]
        self._node_map={}

    def set_node_names(self,names):
        self.node_names=list(names)

    def insert_node(self,new_node_val):
        new_node=Node(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val]=new_node
        return new_node

    def insert_edge(self,new_edge_val,node_from_val,node_to_val):
        nodes={node_from_val:None,node_to_val:None}
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value]=node
                if all(nodes.values()):
                    break
        for node_val in nodes:
            nodes[node_val]=nodes[node_val] or self.insert_node(node_val)
        node_from=nodes[node_from_val]
        node_to=nodes[node_to_val]
        new_edge=Edge(new_edge_val,node_from,node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)


    def get_edge_list(self):
        return[(e.value,e.node_from.value,e.node_to.value)
                for e in self.edges]

    def get_edge_list_names(self):
        return [(e.value,self.node_names[e.node_from.value],self.node_names[e.node_to.value]) for e in self.edges]

    def get_adjacency_list(self):
        max_index=self.find_max_index()
        adj_list=[[] for i in range(max_index)]
        for e in self.edges:
            adj_list[e.node_from.value].append((e.node_to.value,e.value))
        return [a or None for a in adj_list]

    def get_adjacency_list_names(self):
        adj_list=self.get_adjacency_list()
        def convert_to_names(pair,graph=self):
            node_number,value=pair
            return(graph.node_names[node_number],value)
        def map_conversion(adjacency_list_for_node):
            if adjacency_list_for_node is None:
                return None
            return map(convert_to_names,adjacency_list_for_node)
        return [map_conversion(adjacency_list_for_node)
                for adjacency_list_for_node in adj_list]

    def get_adjacency_matrix(self):
        max_index=self.find_max_index()
        adj_matrix=[[0]*max_index for _ in range(max_index)]
        for e in self.edges:
            adj_matrix[e.node_from.value][e.node_to.value]=e.value
        return adj_matrix

    def find_max_index(self):
        if len(self.node_names)>0:
            return len(self.node_names)
        max_index=-1
        if len(self.nodes):
            for node in self.nodes:
                if node.value>max_index:
                    max_index=node.value
        return max_index

    def find_node(self,node_number):
        return self._node_map.get(node_number)

    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False

    def dfs_helper(self,start_node):
        ret_list=[start_node.value]
        start_node.visited=True
        edges_out=[e for e in start_node.edges if e.node_to.value != start_node.value]
        for edge in edges_out:
            if not edge.node_to.visited:
                ret_list.extend(self.dfs_helper(edge.node_to))
        return ret_list

    def dfs(self,start_node_num):
        self._clear_visited()
        start_node=self.find_node(start_node_num)
        return self.dfs_helper(start_node)

    def dfs_names(self,start_node_num):
        return [self.node_names[num] for num in self.dfs(start_node_num)]

    def bfs(self,start_node_num):
        node=self.find_node(start_node_num)
        self._clear_visited()
        ret_list=[]
        queue=[node]
        node.visited=True
        def enqueue(n,q=queue):
            n.visited=True
            q.append(n)
        def unvisited_outgoing_edge(n,e):
            return((not e.node_to.visited) and (e.node_from.value==n.value))

        while queue:
            node=queue.pop(0)
            ret_list.append(node.value)
            for e in node.edges:
                if unvisited_outgoing_edge(node,e):
                    enqueue(e.node_to)
        return ret_list

    def bfs_names(self,start_node_num):
        return[self.node_names[num] for num in self.bfs(start_node_num)]

grp=Graph()

grp.set_node_names(('g','u','r','i','n','d','e','r'))

grp.insert_edge(1,0,3)
grp.insert_edge(1,3,0)
grp.insert_edge(1,0,5)
grp.insert_edge(1,5,0)
grp.insert_edge(1,3,5)
grp.insert_edge(1,5,3)
grp.insert_edge(1,5,1)
grp.insert_edge(1,1,5)
grp.insert_edge(1,5,4)
grp.insert_edge(1,4,5)
grp.insert_edge(1,5,6)
grp.insert_edge(1,6,5)
grp.insert_edge(1,2,4)
grp.insert_edge(1,4,2)
grp.insert_edge(1,6,7)
grp.insert_edge(1,7,6)

import pprint
pp=pprint.PrettyPrinter(indent=2)

print("Edge List")
pp.pprint(grp.get_edge_list_names())

print ("\nAdjacency List")
pp.pprint(grp.get_adjacency_list_names())

print ("\nAdjacency Matrix")
pp.pprint(grp.get_adjacency_matrix())

print ("\nDepth First Search")
pp.pprint(grp.dfs_names(5))

print ("\nBreadth First Search")
pp.pprint(grp.bfs_names(5))
