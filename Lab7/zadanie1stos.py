class Stack:
    def __init__(self):
        self.items = []
    def top(self):
        return self.items[len(self.items)-1]
    def empty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def push(self,element):
        self.items.append(element)
    def pop(self):
        return self.items.pop()