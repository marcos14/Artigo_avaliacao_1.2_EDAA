#https://gist.github.com/zjplab/b052af68196bec5ce48dcc39b0acef2f
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.comparisons = 0
        self.level = 0

    def getComparisons(self):
        return self.comparisons
    
    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
             self.left_child=BinarySearchTree(value)
        elif value > self.value and self.right_child:
             self.right_child.insert_node(value)
        else:
             self.right_child =BinarySearchTree(value)
         
    def find_node(self,value):
        # self.comparisons += 1
        if value < self.value and self.left_child:
            self.comparisons += 1
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            self.comparisons += 1
            return self.right_child.find_node(value)

        return value == self.value 
    def clear_node(self):
        self.value=None
        self.left_child=None
        self.right_child=None

    def find_minimum_value(self):      
        if self.left_child:
            return self.left_child.find_minimum_value()
        else:
            return self.value
    def remove_node(self,value,parent):
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value,self)
        elif value < self.value:
            return False
        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value,self)
        elif value > self.value:
            return False
        else:
            if self.left_child is None and self.right_child is None and self == parent.left_child:
                parent.left_child=None
                self.clear_node()
            elif self.left_child is None and self.right_child is None and self == parent.right_child:     
                parent.right_child = None
                self.clear_node()
            elif self.left_child and self.right_child is None and self==parent.left_child:
                parent.left_child=self.left_child
                self.clear_node()
            elif self.left_child and self.right_child is None and self==parent.right_child:
                parent.right_child=self.left_child
            elif self.right_child and self.left_child is None and self==parent.left_child:
                parent.left_child=self.right_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self==parent.right_child:
                parent.right_child=self.right_child
                self.clear_node()
            else:
                self.value = self.right_child.find_minimum_value()
                self.right_child.remove_node(self.value, self)
    
    def height(self, level):
        l_h = 0
        r_h = 0

        if self.left_child == None and self.right_child == None:
            return level-1

        if self.left_child:
            l_h = self.left_child.height(level+1)

        if self.right_child:
            r_h = self.right_child.height(level+1)
 
        if l_h >= r_h:
            return l_h
        else:
            return r_h
#     int h(No *raiz, int nivel){
#     if (raiz)
#     {
#         int esq = h(raiz->esq, nivel+1);
#         int dir = h(raiz->dir, nivel+1);
#         if(esq >= dir){
#             return esq;
#         }else{
#             return dir;
#         }
#     }else{
#         return nivel-1;
#     }
# } 