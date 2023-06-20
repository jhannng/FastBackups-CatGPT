"""
    Written By: Jui Kai Hang
    Copyright (c) 2023 Jui Kai Hang
"""

class Vertex():
    """
        The Vertex class represents the vertices in the graph. Each vertex will have a unique id and a list of edges that are connected to other vertices.
    """
    
    def __init__(self, id) -> None:
        """
            Function description: This function initialise the id of the vertex, a list of edges, a boolean variable that use to indicate if the vertex has been visited, a boolean variable which use to 
            indicate if the vertex has been discovered, a boolean variable which use to indicate if the vertex is target, a variable which use to indicate the previous edge.
            
            :Input:
                argv1: id (int): unique id of the vertex
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant
        """
        self.id = id
        self.edges = []
        
        self.target = False
        self.visited = False
        self.discovered = False
        
        self.previous_edge = None
        
    def get_id(self):
        """
            Function description: This function return the unique id of vertex.

            :Input:
                None
                
            :Output, return or postcondition:
                return: the unique id of vertex
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        return self.id
        
    def add_edge(self, edge):
        """
            Function description: This function add an edge to the list of edges in the vertex.

            :Input:
                argv1: edge (type[Edge]): the edge of the vertex
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant
        """
        self.edges.append(edge)
        
    def is_target(self):
        """
            Function description: This function return boolean to indicate that current vertex is target or not.

            :Input:
                None
                
            :Output, return or postcondition:
                return: boolean to indicate that current vertex is target or not
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        return self.target
    
    def set_target(self):
        """
            Function description: This function set current vertex as a target.

            :Input:
                None
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        self.target = True
        
    def is_discovered(self):
        """
            Function description: This function return boolean to indicate that current vertex is discovered or not.

            :Input:
                None
                
            :Output, return or postcondition:
                return: boolean to indicate that current vertex is discovered or not
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        return self.discovered
        
    def set_discovered(self):
        """
            Function description: This function set current vertex as discovered.

            :Input:
                None
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        self.discovered = True
    
    def is_visited(self):
        """
            Function description: This function return boolean to indicate that current vertex is visited or not.

            :Input:
                None
                
            :Output, return or postcondition:
                return: boolean to indicate that current vertex is visited or not
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        return self.visited
        
    def set_visited(self):
        """
            Function description: This function set current vertex as visited.

            :Input:
                None
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        self.visited = True
        
    def get_previous_edge(self):
        """
            Function description: This function return the previous edge of current vertex.

            :Input:
                None
                
            :Output, return or postcondition:
                return: the previous edge of current vertex
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        return self.previous_edge
    
    def set_previous_edge(self, previous_edge):
        """
            Function description: This function set the previous edge of current vertex.

            :Input:
                argv1: previous_edge (type[Edge]): the previous edge of current vertex
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        self.previous_edge = previous_edge
        
    def __str__(self) -> str:
        """
            Function description: This function return a string which represent the vertex.

            :Input:
                None
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        return f"Vertex {self.id}"