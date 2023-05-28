import numpy as np
from random import randrange
import LinkedList as ll
import BinarySearchTree as bs

class Utils:
    def __init__(self, length_array) -> None:
        self.array = np.arange(length_array)
        np.random.shuffle(self.array)
        
    
    def rondom_search_item(self):
        return self.array[randrange(len(self.array)-1)]
    
    def get_in_array(self):
        self.array.sort()
        return self.array
    
    def get_in_linked_list(self):
        lLinked = ll.LinkedList()
        for index in range(len(self.array)):
            lLinked.addToStart(self.array[index])
        return lLinked
    
    def get_in_binary_tree(self):
        tree = bs.BinarySearchTree(self.array[0])
        for index in range(1, len(self.array)):
            tree.insert_node(self.array[index])
        return tree 