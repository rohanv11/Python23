class Stack:
    def __init__(self) -> None:
        self.head = -1
        self.stack = []
    
    def insert(self, value):
        self.stack.append(value)
        self.head += 1
    
    def show(self):
        print("Head", self.head)
        print(self.stack)
        

s = Stack()
s.insert(1)
s.insert(10)
s.insert(100)


s.show()