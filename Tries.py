class TriNode:
    def __init__(self):
        self.child = {}
        self.is_word = False

class Tri:
    def __init__(self):
        self.root = TriNode()

    def insert(self,word):
        node = self.root

        for char in word:
            if char not in node.child:
                node.child[char] = TriNode()
            node = node.child[char]
        
        node.is_word = True

    def search(self,word):
        node = self.root
        
        for char in word:
            if char not in node.child:
                return False
            node = node.child[char]
        
        return node.is_word
