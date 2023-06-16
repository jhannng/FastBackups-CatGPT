"""
    Written By: Jui Kai Hang
    Copyright (c) 2023 Jui Kai Hang
"""
from edge import Edge
from graph import Graph

class Main():

    def maxThroughput(connections, maxIn, maxOut, origin, targets):
        """
            Function description: This function will determine the maximum possible data throughtput from the data centre (origin) to the data sentres specified in targets. The implementation of Ford-Fulkerson
            algorithm is inspired by the Malaysia FIT2004 lecturer slides.
            
            Approach description: Graphs are an easy approach for illustrating collections of items and repreenting the connections between them since it can show the relationships between object pairs at the most
            fundamental level. In this case, the data centres are the vertices and the communication channels are the edges. The graph is directed and each edge is one way only. Some of the vertices might have 
            backward flow when it is the part of the augmenting path. Meanwhile, this function will use the Ford-Fulkerson algorithm to find the maximum throughput between the data centres. To reduce the complexity
            by runing the breadth-first search algorithm to indicate the whether the augmenting path exist. I utilise it to a boolean variable which use for indicating, if the augmenting path exist the residual 
            capacity of the augmenting path will be a posititve integer, else it will be zero.
            
            :Input:
                argv1: connections (List[Tuple[int, int, int]]): a list of the direct communication channels between data centres
                argv2: maxIn (List[int]): a list of integers specifies the maximum amount of incoming data that data centre can process per second
                argv3: maxOut (List[int]): a list of integers specifies the maximum amount of outgoing data that data centre can process per second
                argv4: origin (int): the integer ID of the data centre where the data to be backed up is located
                argv5: targets (List[int]): a list of data centres that are deemed appropriate locations for the backup data to be stored
            
            :Output, return or postcondition:
                return: the maximum possible data throughput from the data centre (origin) to the data centres specified in targets
            
            :Time complexity:
                O(|D| * |C| ^ 2), where |D| is the data centres, and |C| is the communication channels
            
            :Space complexity:
                Aux: O(|D| + |C|), where |D| is the data centres, and |C| is the communication channels
        """   
        maximum_vertex = len(maxIn)
        total_vertex = (maximum_vertex) * 3
        
        residual_graph = Graph(total_vertex)
        residual_graph.add_edges(connections, maximum_vertex)
        
        # To indicate the target vertex
        for target in targets:
            residual_graph.get_vertices()[target].set_target()
        
        # To add the incoming edges for each vertex 
        for index in range(len(maxIn)):
            residual_graph.get_vertices()[index + maximum_vertex].add_edge(Edge(residual_graph.get_vertices()[index + maximum_vertex], residual_graph.get_vertices()[index], maxIn[index]))
            
        # To add the outgoing edges for each vertex
        for index in range(len(maxOut)):
            residual_graph.get_vertices()[index].add_edge(Edge(residual_graph.get_vertices()[index], residual_graph.get_vertices()[index + (maximum_vertex * 2)], maxOut[index]))
        
        max_throughput = 0
        has_augmenting_path = True
        
        while has_augmenting_path:
            # To take the residual capacity and augmenting path
            residual_capacity, augmenting_path = residual_graph.get_augmenting_path(origin)
            
            # To augment the throughput equal to the residual capacity
            max_throughput += residual_capacity
            
            # To update the residual graph
            residual_graph.augment_flow(residual_capacity, (augmenting_path))
            
            if residual_capacity == 0:
                has_augmenting_path = False

        return max_throughput