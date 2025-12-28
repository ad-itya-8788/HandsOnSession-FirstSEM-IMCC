# ================================
# Doubly Linked List - All In One
# ================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DL:
    def __init__(self):
        self.head = None

    # add at end
    def add(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return

        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = newnode
        newnode.prev = ptr

    # display list
    def display(self):
        ptr = self.head
        while ptr:
            print(ptr.data, end="->")
            ptr = ptr.next
        print("None")

    # add after position
    def addpos(self, data, pos):
        ptr = self.head
        count = 1
        newnode = Node(data)

        while ptr:
            if count == pos:
                newnode.next = ptr.next
                if ptr.next:
                    ptr.next.prev = newnode
                ptr.next = newnode
                newnode.prev = ptr
                return
            ptr = ptr.next
            count += 1

        print("Invalid position")

    # delete a node by value
    def delnode(self, val):
        ptr = self.head

        # delete head
        if ptr and ptr.data == val:
            self.head = ptr.next
            if self.head:
                self.head.prev = None
            return

        while ptr:
            if ptr.data == val:
                if ptr.next:
                    ptr.next.prev = ptr.prev
                if ptr.prev:
                    ptr.prev.next = ptr.next
                return
            ptr = ptr.next

        print("Value not found")

    # delete alternate nodes (2nd, 4th, 6th...)
    def del_alternate(self):
        ptr = self.head
        while ptr and ptr.next:
            ptr.next = ptr.next.next
            if ptr.next:
                ptr.next.prev = ptr
            ptr = ptr.next

    # delete 1st, 3rd, 5th...
    def del_first_third(self):
        if not self.head:
            return

        # delete first
        self.head = self.head.next
        if self.head:
            self.head.prev = None

        ptr = self.head
        while ptr and ptr.next:
            ptr.next = ptr.next.next
            if ptr.next:
                ptr.next.prev = ptr
            ptr = ptr.next

    # reverse doubly linked list
    def revnode(self):
        ptr = self.head
        last = None

        while ptr:
            ptr.prev, ptr.next = ptr.next, ptr.prev
            last = ptr
            ptr = ptr.prev

        if last:
            self.head = last



x = DL()
arr = [1, 2, 3, 4, 5, 6, 7]
for i in arr:
    x.add(i)
print("\nInitial List:")
x.display()

print("\nAdd 90 after position 3:")
x.addpos(90, 3)
x.display()

print("\nDelete node 4:")
x.delnode(4)
x.display()

print("\nDelete alternate nodes:")
x.del_alternate()
x.display()

print("\nDelete 1st, 3rd, 5th nodes:")
x.del_first_third()
x.display()

print("\nReverse list:")
x.revnode()
x.display()
