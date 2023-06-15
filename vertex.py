class Vertex():
    """
        The Vertex class represents the vertices in the graph. Each vertex will have a unique id and a list of edges that are connected to other vertices. The concept of the vertex
        implementation is based on the Malaysia FIT2004 lecture slides. Howver, modified it to suit the requirement of question 1.
    """
    
    def __init__(self, id):
        """
            Function description: Constructor of the Vertex.

            Approach description: This function initialise the id of the vertex, a list of edges, a boolean variable that use to indicate if the vertex has been visited, a boolean 
            variable which use to indicate if the vertex has been discovered, a boolean variable which use to indicate if the vertex has a passenger, a boolean variable which use to 
            indicate if the vertex is using carpool lane, a integer variable which use to indicate the time taken between vertices, and a variable which use to indicate the previous vertex.
            
            :Input:
                argv1: id (int): unique id of the vertex
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Input: O(1), since the memory necessary for storing an integer is constant
                Aux: O(1), since the amount of memory necessary for this function is constant
        """
        self.id = id
        
        self.edges = []
        
        self.visited = False
        self.discovered = False
        self.has_passenger = False
        self.using_carpool_lane = False
        
        self.time = 0
        
        self.previous = None
        
    def add_edge(self, edge):
        """
            Function description: This function add an edge to the list of edges in the vertex.
            
            Approach description: Since the number of edge for each vertex is not fixed, so it might be better to use append method to store the edge in the list of edges. Instead of 
            initialising the size at the begining and use pointer to store it. 

            :Input:
                argv1: edge (type[Edge]): the edge of the vertex
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Input: O(1), since the memory necessary for storing Edge is constant
                Aux: O(1), since the amount of memory necessary for this function is constant
        """
        self.edges.append(edge)
        
    def discover_node(self):
        """
            Function description: This function assign True to discovered variable of Vertex, which indicate that vertex being discovered.

            Approach description: To avoid violating the OOD principle, the function will reassign the value of discovered variable to True when the function being called. Instead of 
            reassigning the value of discovered outside the class.
            
            :Input:
                argv1: None
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Input: O(1)
                Aux: O(1), since the amount of memory necessary for this function is constant
        """
        self.discovered = True
        
    def visit_node(self):
        """
            Function description: This function assign True to visited variable of Vertex, which indicate that vertex being visited.
            
            Approach description: To avoid violating the OOD principle, the function will reassign the value of visited variable to True when the function being called. Instead of 
            reassigning the value of visited outside the class.

            :Input:
                argv1: None
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Input: O(1)
                Aux: O(1), since the amount of memory necessary for this function is constant
        """
        self.visited = True