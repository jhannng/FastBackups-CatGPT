"""
    Written By: Jui Kai Hang
    Copyright (c) 2023 Jui Kai Hang
"""

from Node.node import Node

class CatsTrie:
    """
        CatsTrie is a class that used to represent the catGPT model, which able to complete the sentences automatically based on the prompt provided, CatsTrie is implemented based on a Trie data structure.
    """
    
    def __init__(self, sentences):
        """
            Function description: Constructor of the CatsTrie.
            
            Apporach description: This function will initialise the root of the CatsTrie and insert the provided sentences.
            
            :Input:
                argv1: sentences (List[str]): a list of cat sentence that map to the 26 letters in the English language
            
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(NM), where N is the number of sentence in sentences, and M is the number of characters in the longest sentence
                
            :Space complexity:
                Input: O(N), where N is the number of sentence in sentences
                Aux: O(NM), where N is the number of sentence in sentences, and M is the number of sharacters in the longest sentence

        """
        self.root = Node()
        for sentence in sentences:
            self.insert(sentence)
        
    def insert(self, sentence):
        """
            Function description: This function will store the cat sentence.
            
            Apporach description: This function will call the insert_aux function to insert the cat sentence and the frequnecy of each sentence.
            
            :Input:
                argv1: sentence (str): a cat sentence that map to the 26 letters in the English language
                
            :Output, return or postcondition:
                return: None
                
            :Time complexity:
                O(M), where M is the number of characters in the longest sentence 
                
            :Space complexity:
                Input: O(M), where M is the number of characters in the longest sentence
                Aux: O(M), where M is the number of characters in the longest sentence
        """
        self.insert_aux(self.root, sentence, char = 0)
                
    def insert_aux(self, current_node, sentence, char):
        """
            Function description: This function will store the each word in the cat sentence over the character.
            
            Apporach description: This function will check whether reach the end of the sentence, if yes, then the index will be zero which pointes to the terminal, indicate that it is the end of the sentence.
            Meanwhile, the frequency of the cat sentence will be increased by one, then proceed with checking the prediction index of the previous node, if the prediction frequency is smaller than the sentence
            frequency, then the prediction index will be updated to the current node, and the prediction frequency will be updated to the sentence frequency. If the prediction frequency is equal to the sentence
            frequency, then the prediction index will be updated based on the lexicogrphicall order. While opposite, then the index will be calculated based on the character's unicode in the sentence, and 
            reassign the current node to the upcoming node. Then, proceed with checking the frequency of the cat sentence and the current node, if the frequency of the cat sentence is greater than the current
            node, then the current node will be updated to the cat sentence frequency. After that, the function will be called recursively until the end of the sentence.
            
            :Input:
                argv1: current_node (type[Node]): current node in the CatsTrie
                argv2: sentence (str): cat sentence that map to the 26 letters in the English language
                argv3: char (int): current character's index in the sentence
                
            :Output, return or postcondition:
                return: the frequency of the cat sentence
                
            :Time complexity:
                O(M), where M is the number of characters in the longest sentence 
                
            :Space complexity:
                Input: O(M), where M is the number of characters in the longest sentence
                Aux: O(M), where M is the number of characters in the longest sentence
        """
        previous_node = current_node
        if len(sentence) == char:
            index = 0
            # If next node exist, then reassign the current node, else create a new node
            if current_node.prediction[index] is None:
                current_node.prediction[index] = Node()
                
            current_node = current_node.prediction[index]
            current_node.frequency += 1
            
            # To indicate the prediction index and frequency
            if previous_node.prediction_index is not None and previous_node.prediction_frequency is not None:
                if current_node.frequency > previous_node.prediction_frequency:
                    previous_node.prediction_index, previous_node.prediction_frequency = index, current_node.frequency
                    
                if current_node.frequency == previous_node.prediction_frequency and index < previous_node.prediction_index:
                    previous_node.prediction_index, previous_node.prediction_frequency = index, current_node.frequency
            else:
                previous_node.prediction_index, previous_node.prediction_frequency = index, current_node.frequency
            
            return current_node.frequency
            
        else: 
            index = ord(sentence[char]) - 97 + 1
            # If next node exist, then reassign the current node, else create a new node
            if current_node.prediction[index] is None:
                current_node.prediction[index] = Node()
                
            current_node = current_node.prediction[index]
            
            sentence_frequency = self.insert_aux(current_node, sentence, char + 1)
            
            # If the sentence show up again, then increase the frequency of current node, else the frequency of current node remain as it is
            if sentence_frequency > current_node.frequency:
                current_node.frequency += 1
            
            # To indicate the prediction index and frequency
            if previous_node.prediction_index is not None and previous_node.prediction_frequency is not None:
                if current_node.frequency > previous_node.prediction_frequency:
                    previous_node.prediction_index, previous_node.prediction_frequency = index, current_node.frequency
                    
                if current_node.frequency == previous_node.prediction_frequency and index < previous_node.prediction_index:
                    previous_node.prediction_index, previous_node.prediction_frequency = index, current_node.frequency
            else:
                previous_node.prediction_index, previous_node.prediction_frequency = index, current_node.frequency
                
            return sentence_frequency
        
    def autoComplete(self, prompt):
        """
            Function description: This function will return a complete cat sentence based on the prompt which is an incomplete sentences.
            
            Apporach description: This function will iterate through the prompt and transverse the CatsTrie to find the complete cat sentence. When the prompt is a complete cat sentence and has the highest frequency
            among the sentences, it will be returned. However, it will return None, if the character can't be found during the transversal. Additioanlly, it will append each character into the list since appending 
            the character into the list, consider as amortised O(1). When the cat's sentence is completed or reach the terminal, then it will join the list to form a string and return the completed sentence with 
            highest frequency among the sentences provided.
            
            :Input:
                argv1: prompt (str): string represents the incomplete sentence that is to be completed by the trie
                
            :Output, return or postcondition:
                return: auto_complete_sentence (str): a string that represents the completed sentences from the prompt
                
            :Time complexity:
                O(X + Y), where X is the length of the prompt, and Y is the length of the most frequency sentence in sentences that begins with the prompt
                
            :Space complexity:
                Input: O(X), where X is the length of the prompt
                Aux: O(Y), where Y is the length of the most frequency sentence in sentences that begins with the prompt
        """
        prediction_sentence = []
        
        current_node = self.root
        for char in prompt:
            index = ord(char) - 97 + 1
            if current_node.prediction[index] is not None:
                current_node = current_node.prediction[index]
                prediction_sentence.append(char)
            else:
                return None
        
        # Start from the current node and traverse based on the prediction index to the terminal node
        prediction_node = current_node.prediction[current_node.prediction_index]
        if prediction_node.prediction_index is not None:
                prediction_sentence.append(chr(current_node.prediction_index + 97 - 1))
                
        while prediction_node is not None and prediction_node.prediction_index is not None:
            if prediction_node.prediction_index > 0:
                prediction_sentence.append(chr(prediction_node.prediction_index + 97 - 1))
            prediction_node = prediction_node.prediction[prediction_node.prediction_index]
        
        auto_complete_sentence = "".join(prediction_sentence)
        
        return auto_complete_sentence