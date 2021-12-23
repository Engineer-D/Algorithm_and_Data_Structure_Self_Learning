class Stack:
    def __init__(self):
        self.item = []
        self.length = 0
    
    def is_empty(self):
        return self.item == []
    
    def push(self, item):
        self.item.append(item)
        self.length += 1
    
    def  pop(self):
        assert not self.is_empty()
        self.length -= 1
        return self.item.pop()
    
    def peek(self):
        assert not self.is_empty()
        return self.item[-1]
    
    def size(self):
        return self.length