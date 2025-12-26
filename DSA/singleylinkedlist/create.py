class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def add(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        ptr = self.head
        while ptr.next:
            ptr = ptr.next

        ptr.next = newnode

    def display(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end="  ")
            ptr = ptr.next


s = Linkedlist()
s.add(3)
s.add(4)
s.add(55)
s.add(34)
s.display()
