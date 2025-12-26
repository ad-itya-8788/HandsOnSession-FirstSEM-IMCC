class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newnode = Node(data)
        newnode.next = self.top
        self.top = newnode
        print(data, "pushed into stack")

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        print("Stack elements (top to bottom):")
        ptr = self.top
        while ptr:
            print(ptr.data)
            ptr = ptr.next


s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display()
