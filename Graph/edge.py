"""
    Written By: Jui Kai Hang
    Copyright (c) 2023 Jui Kai Hang
"""

class Edge():
    """
        The Edge class represents the edges in both of the graph's vertices. While the Edge is directed and one way only.
    """
    
    def __init__(self, u, v, w) -> None:
        """
            Function description: This function will initialise the ID of the data centre from which the communication channel departs, the ID of the data centre to which the communication channel arrives, a
            positive integer that representing the maximum throughput of that channel and the backward flow of current forward flow.

            :Input:
                argv1: u (type[Vertex]): the ID of the data centre from which the communication channel departs
                argv2: v (type[Vertex]): the ID of the data centre to which the communication channel arrives
                argv3: w (int): a positive integer that representing the maximum throughput of that channel
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        self.u = u
        self.v = v
        self.w = w
        
        self.backward_flow = None
        
    def get_u(self):
        """
            Function description: This function return the ID of the data centre from which the communication channel departs.

            :Input:
                None
                
            :Output, return or postcondition:
                return: the ID of the data centre from which the communication channel departs
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        return self.u
    
    def set_u(self, u):
        """
            Function description: This function set the ID of the data centre from which the communication channel departs.

            :Input:
                argv1: u (type[Vertex]): the ID of the data centre from which the communication channel departs
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        self.u = u
        
    def get_v(self):
        """
            Function description: This function return the ID of the data centre to which the communication channel arrives.

            :Input:
                None
                
            :Output, return or postcondition:
                return: the ID of the data centre to which the communication channel arrives
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        return self.v
    
    def set_v(self, v):
        """
            Function description: This function set the ID of the data centre to which the communication channel arrives.

            :Input:
                argv1: v (type[Vertex]): the ID of the data centre to which the communication channel arrives
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        self.v = v
        
    def get_w(self):
        """
            Function description: This function return the maximum throughput of that channel.

            :Input:
                None
                
            :Output, return or postcondition:
                return: a positive integer that representing the maximum throughput of that channel
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        return self.w
    
    def set_w(self, w):
        """
            Function description: This function set the maximum throughput of that channel.

            :Input:
                argv1: w (int): a positive integer that representing the maximum throughput of that channel
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        self.w = w
        
    def get_backward_flow(self):
        """
            Function description: This function return the opposite direction of the current edge.

            :Input:
                None
                
            :Output, return or postcondition:
                return: the opposite direction of the current edge
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        return self.backward_flow
    
    def set_backward_flow(self, backward_flow):
        """
            Function description: This function set the opposite direction of the current edge.

            :Input:
                argv1: backward_flow (type[Edge]): the opposite direction of the current edge
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        self.backward_flow = backward_flow
        
    def __str__(self):
        """
            Function description: This function return a string which represent the edge.

            :Input:
                None
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        return f"Edge: {self.u} -> {self.v} with maximum throughput: {self.w}"