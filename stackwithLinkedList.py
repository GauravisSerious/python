class Node :
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack :
    def __init__(self):
        self.top = None
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def isEmpty(self):
        return self.top is None

    def pop(self):
        if not self.isEmpty():
            popped_item = self.top.value
            self.top = self.top.next
            print(str(popped_item))

    def iterate(self):
        iterate = self.top
        while iterate is not None:
            print(str(iterate.value), end="")
            iterate = iterate.next

        
