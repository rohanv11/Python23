# TODO
#   add a decorator for every opertation
#   such that it prints the opertion and displays the stack

class Stack:
    def __init__(self) -> None:
        self.head = -1
        self.stack = [0 for i in range(100)]
    
    def insert(self, value):
        self.head += 1
        self.stack[self.head] = value
    
    def show(self):
        print("Head", self.head)
        for i in range(self.head+1):
            print(self.stack[i])

    def pop(self):
        if self.head >= 0:
            self.head -= 1
        else:
            print("no element to pop")



    

s = Stack()
s.insert(1)
s.insert(10)
s.pop()
s.insert(100) # 1, 100
s.pop()
s.insert(56) 
s.pop()
s.insert(200) # 1, 200
s.insert(300)
s.pop()  # 1, 200
s.pop()
s.pop()
s.pop()

# s.show()