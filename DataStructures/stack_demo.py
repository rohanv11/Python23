class Stack:
    def __init__(self) -> None:
        self.head = -1
        self.stack = []
    
    def insert(self, value):
        self.stack.append(value)
        self.head += 1
    
    def show(self):
        print("Head", self.head)
        for i in range(self.head+2):
            print(self.stack[i])

    def pop(self):
        if self.head >= 0:
            self.head -= 1


        

s = Stack()
s.insert(1)
s.insert(10)
s.pop()
s.insert(100)


s.show()