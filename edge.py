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
            Function description: Constructor of the Edge.
            
            Approach Description: This function will initialise the ID of the data centre from which the communication channel departs, the ID of the data centre to which the communication channel arrives, a
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
            Function description: Getter of departure data center.

            :Input:
                None
                
            :Output, return or postcondition:
                return: The ID of the data centre from which the communication channel departs
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        return self.u
    
    def set_u(self, u):
        """
            Function description: Setter of departure data center.

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
            Function description: Getter of arrival data center.

            :Input:
                None
                
            :Output, return or postcondition:
                return: The ID of the data centre to which the communication channel arrives
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        return self.v
    
    def set_v(self, v):
        """
            Function description: Setter of arrival data center.

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
            Function description: Getter of maximum throughput of that channel.

            :Input:
                None
                
            :Output, return or postcondition:
                return: A positive integer that representing the maximum throughput of that channel
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        return self.w
    
    def set_w(self, w):
        """
            Function description: Setter of maximum throughput of that channel.

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
            Function description: Getter of backward flow.

            :Input:
                None
                
            :Output, return or postcondition:
                return: The opposite direction of the current edge
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        return self.backward_flow
    
    def set_backward_flow(self, backward_flow):
        """
            Function description: Setter of backward flow.

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
        return f"Edge: {self.u} -> {self.v} with maximum throughput: {self.w}"