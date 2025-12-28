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
  def delalter(self):
    ptr=self.head
    while ptr and ptr.next:
      ptr.next=ptr.next.next
      if ptr.next:
        ptr.next.prev=ptr
      ptr=ptr.next


x=dl()
x.add(12)
x.add(3)
x.add(34)
x.add(56)
x.display()
x.delalter()
x.display()