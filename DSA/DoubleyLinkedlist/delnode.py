class Node():
  def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None
class dl:
  def __init__(self):
    self.head=None
  def add(self,data):
    newnode=Node(data)
    if self.head is None:
      self.head=newnode
    else:
      ptr=self.head
      while ptr.next!=None:
        ptr=ptr.next
      ptr.next=newnode
      newnode.prev=ptr
  def display(self):
    ptr=self.head
    while ptr:
      print(ptr.data,end="->")
      ptr=ptr.next
    print("None")
  def delnode(self, y):
    ptr = self.head
    if ptr and ptr.data == y:
        self.head = ptr.next
        if self.head:
            self.head.prev = None
        return

    while ptr:
        if ptr.data == y:
            if ptr.next:
                ptr.next.prev = ptr.prev
            if ptr.prev:
                ptr.prev.next = ptr.next
            return
        ptr = ptr.next


x=dl()
arr=[1,2,3,4,5,6,7,8,9,10,11,22,33]
for i in arr:
  x.add(i)
x.display()
y=int(input("Enter Node for Delete:"))
x.delnode(y)
x.display()