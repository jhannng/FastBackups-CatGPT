class Graph():
    """
        The Graph class is used to represent the road network. The networks will include the time taken for travelling from one vertex to another vertex. The concept of the graph
        implementation is based on the Malaysia FIT2004 lecture slides. Howver, modified it to suit the requirement of question 1.
    """
    
    def __init__(self, maximum_vertex):
        """
            Function description: Construtor of the Graph.
            
            Approach description: Since the number of vertex in each graph is not fixed, we can iterate over a sequence which according to the argv1 (maximum_vertex) that use to identify 
            the maximum number of vertices and create a list of vertices.

            :Input:
                argv1: maximum_vertex (int): the maximum number of vertices in the graph
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(n), where n is the maximum number of vertices in the graph
                
            :Space complexity:
                Input: O(1), since the memory necessary for storing an integer is constant
                Aux: O(n), where n is the maximum number of vertices in the graph
        """
        self.vertices = [None] * maximum_vertex
        for vertex in range(maximum_vertex):
            self.vertices[vertex] = Vertex(vertex)
        
    def add_edges(self, edges, allow_to_use_carpool_lane = False):
        """
            Function description: This function add all potential edges to each vertex in the graph.
            
            Approach description: Since each of the vertex might have more than two edges, we can iterate over the list of edges which pass in as argv1 and add each edge to the list of edges 
            in the vertex. While, it will check if the graph permits to use carpool lane, if it does, then assign True to the using_carpool_lane variable of each vertex.

            :Input:
                argv1: edges (List[Tuple[int, int, int, int]]): a list of tuple which contains the information of the edges
                argv2: allow_to_use_carpool_lane (bool, optional): a boolean use for indicating if the graph permits to use carpool lanes, defaults to False
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(n), where n is the number of edges in the graph
                
            :Space complexity:
                Input: O(n), where n is the number of edges in the graph
                Aux: O(1), since the amount of memory necessary for this function is constant
        """
        for edge in edges:
            a = self.vertices[edge[0]]
            b = self.vertices[edge[1]]
            c = edge[2]
            d = edge[3]
            
            current_edge = Edge(a, b, c, d)
            a.add_edge(current_edge)
            
            if allow_to_use_carpool_lane:
                a.using_carpool_lane = True
                b.using_carpool_lane = True