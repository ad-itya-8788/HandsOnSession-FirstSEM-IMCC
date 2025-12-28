# =========================
# STACK USING LINKED LIST
# ALL IN ONE PROGRAM
# =========================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    # PUSH
    def push(self, data):
        newnode = Node(data)
        newnode.next = self.top
        self.top = newnode

    # DISPLAY
    def display(self):
        ptr = self.top
        while ptr:
            print(ptr.data, end=" ")
            ptr = ptr.next
        print()

    # POP
    def pop(self):
        if self.top is None:
            print("Stack Empty")
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    # PEEK
    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    # REVERSE STACK USING ARRAY (ONLY DISPLAY)
    def revstack(self):
        arr = []
        ptr = self.top
        while ptr:
            arr.append(ptr.data)
            ptr = ptr.next
        for i in range(len(arr)-1, -1, -1):
            print(arr[i], end=" ")
        print()

    # REVERSE STACK USING ANOTHER STACK
    def revusingstack(self, x2):
        ptr = self.top
        while ptr:
            x2.push(ptr.data)
            ptr = ptr.next

    # REVERSE STRING USING STACK
    def revstring(self, s):
        for ch in s:
            self.push(ch)
        while self.top:
            print(self.pop(), end="")
        print()


# =========================
# MAIN DRIVER CODE
# =========================

if __name__ == "__main__":

    x = stack()
    arr = [1, 2, 3, 4, 5, 6, 7]

    for i in arr:
        x.push(i)

    print("Stack elements:")
    x.display()

    print("Pop element:", x.pop())
    print("After pop:")
    x.display()

    print("Peek element:", x.peek())

    print("Reverse stack using array:")
    x.revstack()

    x2 = stack()
    x.revusingstack(x2)

    print("Reverse stack using another stack:")
    x2.display()

    print("Reverse string using stack:")
    x3 = stack()
    x3.revstring("ADITYA")
