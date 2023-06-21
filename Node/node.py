"""
    Written By: Jui Kai Hang
    Copyright (c) 2023 Jui Kai Hang
"""

class Node:
    """
        The Node class is used to represent the node which contain data and one or more links to other nodes in the CatsTrie.
    """
    
    def __init__(self):
        """
            Function description: Constructor of the Node.
            
            Apporach description: This function will initialise the frequency of the cat's word, a list of 27 elements represent a terminal and 26 characters that store the next character of the cat's word, 
            the index of the predicted character and the frequency of the predicted character.
            
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
        self.frequency = 0
        self.prediction = [None] * 27
        self.prediction_index = None
        self.prediction_frequency = None