class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        ptr = self.head
        while ptr.next:
            ptr = ptr.next

        ptr.next = newnode
        newnode.prev = ptr

    def display(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end=" <-> ")
            ptr = ptr.next
        print("None")
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

dll.display()
