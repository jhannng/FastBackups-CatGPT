class Edge():
    """
        The Edge class represents the edges in both of the graph's vertices. While the Edge is directed and one way only. The concept of the edge implementation is based on the Malaysia 
        FIT2004 lecture slides. However, modified it to suit the requirement of question 1.
    """
    def __init__(self, a, b, c, d):
        """
            Function description: Constructor of the Edge.
            
            Approach Description: This function will initialise the starting location of the road (a), the ending location of the road (b), the time taken for travelling from the starting
            location to the ending location (c), and the time taken for travelling from the starting location to the ending location by using carpool lane (d).

            :Input:
                argv1: a (type[Vertex]): the starting location of the road
                argv2: b (type[Vertex]): the ending location of the road
                argv3: c (int): the time taken for travelling from the starting location to the ending location
                argv4: d (int): the time taken for travelling from the starting location to the ending location by using carpool lane
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of assigning a value to a variable is constant
                
            :Space complexity:
                Input: O(1), since the memory necessary for storing Vertex and integer is constant 
                Aux: O(1), since the amount of memory necessary for this function is constant 
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d