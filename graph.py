"""
    Written By: Jui Kai Hang
    Copyright (c) 2023 Jui Kai Hang
"""

from edge import Edge
from vertex import Vertex

class Graph():
    """
        The Graph class is used to represent the connections network. The network will include the maximum throughput of the channels, maximum amount of incoming data that data centres can process per second,
        and the maximum amount of outgoing data that data centres can process per second.
    """
    
    def __init__(self, maximum_vertex):
        """
            Function description: Since the number of vertex in each graph is not fixed, we can iterate over a sequence which according to the argv1 (maximum_vertex) that used to identify the maximum number of
            vertices and create a list of vertices.
            
            :Input:
                argv1: maximum_vertex (int): the maximum number of vertices in the graph
                
            :Output, return or postcondition:
                return: None
            
            :Time complexity:
                O(n), where n is the maximum number of vertices in the graph.
                
            :Space complexity:
                Aux: O(n), where n is the maximum number of vertices in the graph
        """
        self.vertices = [None] * (maximum_vertex)
        for vertex in range((maximum_vertex)):
            self.vertices[vertex] = Vertex(vertex)

    def get_vertices(self):
        """
            Function description: This function return a list of vertex within the graph.

            :Input:
                None
                
            :Output, return or postcondition:
                return: a list of vertex within the graph
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        return self.vertices
    
    def add_edges(self, edges, maximum_vertex):
        """
            Function description: This function add all potential edges to each vertex in the graph. Since each of the vertex might have more than one edges, we can iterate over the list of edges which pass 
            in as argv1 (edges) and add each edges to the list of edges in the vertex. Additionally, maximum_vertex is used for identify the index of list that the vertex is located since the edges are 
            connected from current outgoing vertex to another incoming vertex.
            
            :Input:
                argv1: edges (List[Tuple[int, int, int]]): a list of tuple which containes the information of edges
                argv2: maximum_vertex (int): the maximum number of vertices in the graph
                
            :Output, return or postcondition:
                return: None
            
            :Time complexity:
                O(E), where E is the number of edge in the edges list
                
            :Space complexity:
                Aux: O(E), where E is the number of edge in the edges list
        """
        for edge in edges:
            a = self.vertices[edge[0] + (maximum_vertex * 2)]
            b = self.vertices[edge[1] + maximum_vertex]
            t = edge[2]
            
            current_edge = Edge(a, b, t)
            a.add_edge(current_edge)
            
    def reset_graph(self):
        """
            Function description: This function reset the necessary information of vertices in the graph to its default value. Since breadth-first search will search throught all the possbile path in each 
            iteration. Thus, it requires to reset the necessary information of vertices in the graph to its default value. Therefore, the vertices which have been visited will not be missed in the next 
            iteration.
            
            :Input:
                argv1: None
                
            :Output, return or postcondition:
                return: None
            
            :Time complexity:
                O(V), where V is the number of vertices in the graph
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant
        """
        for vertex in self.get_vertices():
            vertex.visited = False
            vertex.discovered = False
            vertex.previous_edge = None
            
    def breadth_first_search(self, origin):
        """
            Function description: This function is used to find the augmenting path from the origin to the target. Breadth-first search is used to search the graph for the augmenting path. The algorithm will 
            start from the origin according to the arg1 and search all edges at the current deapth level before moving to the next vertex and it will stop when the target is found. The algorithm will also 
            keep track of the previous edge of each vertex to form the augmenting path.
            
            :Input:
                argv1: origin (int): an integer that specifies the origin of the data centre where the data to be backed up is located
                
            :Output, return or postcondition:
                return: the target of data centres that are deemed appropriate locations for the backup data to be stored
                
            :Time complexity:
                O(V + E), where V is the number of vertices in the graph, and E is the number of edges for each vertex
                
            :Space complexity:
                Aux: O(V), where V is the number of vertices in the graph
        """
        self.reset_graph()
        
        discovered = []
        backtracking_target = None
        
        origin = self.get_vertices()[origin]
        origin.set_discovered()
        
        discovered.append(origin)
        
        while len(discovered) > 0:
            u = discovered.pop(0)
            u.set_visited()
            
            if u.is_target():
                backtracking_target = u
                break
            
            for edge in u.edges:
                v = edge.get_v()
                
                # To indicate the vertex is not discovered and visted, and the edge has a positive flow
                if v.is_discovered() == False and edge.get_w() > 0:
                    v.set_discovered()
                    v.set_previous_edge(edge)
                    discovered.append(v)
        
        return backtracking_target
    
    def get_augmenting_path(self, origin):
        """
            Function description: This function is used to find the augmenting path and the residual capacity of the augmenting path, which calling the breadth-first search function to find the augmenting path,
            then start backtracking the augmenting path from the target to the origin to store the edges in the list. Addtitionally, the function will find the residual capacity of the augmenting path which is
            the minimum capacity along the augmenting path.
            
            :Input:
                argv1: origin (int): an integer that specifies the origin of the data centre where the data to be backed up is located
                
            :Output, return or postcondition:
                return: the residual capacity of the augmenting path and a list of edges that is in the augmenting path
                
            :Time complexity:
                O(V + E), where V is the number of vertices in the graph, and E is the number of edges for each vertex
                
            :Space complexity:
                O(V), where V is the number of vertices that is in the augmenting path
        """
        
        backtracking_target = self.breadth_first_search(origin)
        augmenting_path = []
        
        # Use to back track the connections to indicate the communication channel has been visited
        while backtracking_target != None and backtracking_target.get_previous_edge() != None:
            augmenting_path.append(backtracking_target.get_previous_edge())
            backtracking_target = backtracking_target.get_previous_edge().get_u()
        
        augmenting_path.reverse()
        
        residual_capacity = None
        # To get the residual capacity by finding the minimum capacity of the path
        for edge in augmenting_path:
            if edge is not None and residual_capacity is None:
                residual_capacity = edge.get_w()
            elif edge is not None:
                residual_capacity = min(residual_capacity, edge.get_w())
                
        if residual_capacity is None:
            residual_capacity = 0
            
        return residual_capacity, augmenting_path
    
    def augment_flow(self, residual_capacity, augmenting_path):
        """
            Function description: This function is used to augment the flow of the graph, which reducing the capacity of the edges in the augmenting path by the residual capacity, and will check if the backward
            flow is exist. If the backward flow is exist, the function will increase the capacity of the backward flow by the residual capacity. Otherwise, the function will create a new backward flow and add 
            it to the graph.
            
            :Input:
                argv1: residual_capacity (int): the residual capacity of the augmenting path
                argv2: augmenting_path (List[Edge]): a list of edges that is in the augmenting path
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(V), where V is the number of vertices that is in the augmenting path
                
            :Space complexity:
                O(1), since the amount of memory necessary for this function is constant
        """
        for edge in augmenting_path:
            if edge is not None:
                edge.set_w(edge.get_w() - residual_capacity)
                
                # To add or update the backward flow
                if edge.get_backward_flow() is not None:
                    edge.get_backward_flow().set_w(edge.get_backward_flow().get_w() + residual_capacity)
                else:
                    edge.set_backward_flow(Edge(edge.get_v(), edge.get_u(), residual_capacity))
                    edge.get_b().add_edge(edge.get_backward_flow())
                    
    def __str__(self):
        """
            Function description: This function return a string which represent the graph.

            :Input:
                None
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(E), where E is the number of edge in the edges list
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        graph_visualization = ""
        graph_visualization += f"ID: {self.id} \n"
        
        # for edge in self.edges:
        #     u = edge.u.id
        #     v = edge.v.id
        #     w = edge.w
            
        #     graph_visualization += f"  Edge: <{u}, {v}, {w}> \n"
            
        return graph_visualization