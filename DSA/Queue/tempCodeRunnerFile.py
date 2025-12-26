class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        newnode = Node(data)

        if self.rear is None:
            self.front = self.rear = newnode
            print(data, "enqueued into queue")
            return

        self.rear.next = newnode       
        self.rear = newnode
        print(data, "enqueued into queue")

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        print("Queue elements (front to rear):")
        ptr = self.front
        while ptr:
            print(ptr.data, end=" ")
            ptr = ptr.next
        print()


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()
