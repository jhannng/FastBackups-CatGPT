class MinHeap():
    """
        In accordance with Daniel Anderson's FIT2004 Algorithm and Data Strucutre Course Note and the heap.py file from FIT1008 Introduction to Conputer Science, MinHeap turns out to be the MaxHeap 
        implementation which has been modified correspond with this assignment.
        
        MinHeap is a Binary Heap where used to store data effiecienly and get the min element based on its structure. This indicates that the root node is the smallest value in the tree and each parent 
        nodes will smaller than the other two child nodes.
    """
    
    def __init__(self, size):
        """
            Function description: Constructor of the MinHeap.
            
            Approach description: To avoid on this array being linked to other extra things, so the array will be initialised with a fixed size and the item declared as None. 
            
            :Input:
                argv1: size (int): the size of the MinHeap
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(n), where n is the size of an array
                
            :Space complexity:
                Input: O(1), since the memory necessary for storing integer is constant
                Aux: O(n), where n is the size of an array
        """
        self.length = 0
        self.array = [None] * (size + 1)
        
    def __len__(self):
        """
            Function desciption: This function return current length of the MinHeap.
            
            Approach description: Instead of call the method for returning the current size of MinHeap, using magic method will provide a simply way to make objects behave like built-in 
            types, also easily to trap potential errors and fix them.
            
            :Input:
                argv1: None
                
            :Output, return or postcondition:
                int: current length of the MinHeap
                
            :Time complexity:
                O(1), since the operation of returning a value is constant
                
            :Space complexity:
                Input: O(1)
                Aux: O(1), since the amount of memory necessary for this function is constant
        """     
        return self.length
    
    def is_full(self):
        """
            Function desciption: This function indicate the MinHeap is currently full or available.
            
            Approach description: To check is the MinHeap full or not, compare the length of the MinHeap with the length of the array. The function return True if the MinHeap is full, 
            otherwise return False.
            
            :Input:
                argv1: None
                
            :Output, return or postcondition:
                return: True if the MinHeap is full, False if the MinHeap is not full
                
            :Time complexity:
                O(1), since the operation of comparing intergers is constant
                
            :Space complexity:
                Input: O(1)
                Aux: O(1), since the amount of memory necessary for this function is constant
        """    
        return self.length + 1 == len(self.array)
        
    def insert(self, edge):
        """
            Function desciption: This function add an edge to MinHeap.
            
            Approach description: Before adding the edge into the MinHeap, it indicate the avalability of array, if the array is not full, add an edge to it and update the length, then 
            perform the rise function to maintain the MinHeap structure.
            
            :Input:
                argv1: edge (Tuple[int, type[Vertex]]): a tuple which contain time and vertex that will be added to the MinHeap
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(log n), where n is the number of edge in MinHeap
                
            :Space complexity:
                Input: O(1), since the memory necessary for storing Vertex and integer is constant
                Aux: O(1), since the amount of memory necessary for this function is constant
        """    
        if not self.is_full():
            self.length += 1
            self.array[self.length] = edge
            self.rise(self.length)

    def serve(self):
        """
            Function desciption: This function removes and returns smallest edge based on the int which represent time taken in th MinHeap.
            
            Approach description: Before removing the edge from the MinHeap, it swap the position of the root node and the last node, then store the last node, which will use to return later. 
            Following, update the length and perform the sink function to maintain the MinHeap structure.
            
            :Input:
                argv1: None
                
            :Output, return or postcondition:
                return: a tuple which contain time taken and vertex
                
            :Time complexity:
                O(log n), where n is the number of edge in MinHeap
                
            :Space complexity:
                Input: O(1)
                Aux: O(1), since the amount of memory necessary for this function is constant
        """   
        self.swap(1, self.length)
        return_edge = self.array[self.length]
        
        self.array[self.length] = None
        self.length -= 1
        self.sink(1)
        
        return return_edge
    
    def swap(self, position1, position2):
        """
            Function desciption: This function swap the items of MinHeap.
            
            Approach description: It will swap the items of MinHeap based on the position of the items, which refer to the index of the array.
            
            :Input:
                argv1: position1 (int): the position of the first item
                argv2: position2 (int): the position of the second item
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(1), since the operation of swapping two items is constant
                
            :Space complexity:
                Input: O(1)
                Aux: O(1), since the amount of memory necessary for this function is constant
        """   
        self.array[position1], self.array[position2] = self.array[position2], self.array[position1]
        
    def rise(self, position):
        """
            Function desciption: This function rise the element to its correct position.
            
            Approach description: Before rising the edge to its correct position, it will compare the time taken of the edge with its parent, if the time taken of the edge is smaller than its 
            parent, swap the edge with its parent and repeat the process until the root of the MinHeap is the smallest time taken among all edges.
            
            :Input:
                argv1: position (int): the position of the item that will be rise
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(log n), where n is the number of edge in MinHeap
                
            :Space complexity:
                Input: O(1)
                Aux: O(1), since the amount of memory necessary for this function is constant
        """   
        parent = position // 2
        
        while parent >= 1:
            if self.array[parent][0] > self.array[position][0]:
                self.swap(parent, position)
                position = parent
                parent = position // 2
            else:
                break
            
    def sink(self, position):
        """
            Function desciption: This function sink the element to its correct position.
            
            Approach description: Before sinking the edge to its correct position, it will compare the time taken of the edge with its child, if the time taken of the edge is smaller than its
            child, swap the edge with its child and repeat the process until the last node of the MinHeap is the smallest time taken among all edges.
            
            :Input:
                argv1: position (int): the position of the item that will be sink
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(log n), where n is the number of edge in MinHeap
                
            :Space complexity:
                Input: O(1)
                Aux: O(1), since the amount of memory necessary for this function is constant
        """   
        child = position * 2
        
        while child <= self.length:
            if child < self.length and self.array[child + 1][0] < self.array[child][0]:
                child += 1
            if self.array[position][0] > self.array[child][0]:
                self.swap(position, child)
                position = child
                child = 2 * position
            else:
                break