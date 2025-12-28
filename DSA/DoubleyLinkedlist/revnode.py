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
  def revnode(self):
    ptr=self.head
    last=None
    while ptr:
      ptr.prev,ptr.next=ptr.next,ptr.prev
      last=ptr
      ptr=ptr.prev
    if last:
      self.head=last
x=dl()
x.add(12)
x.add(3)
x.add(34)
x.add(56)
x.display()
x.revnode()
x.display()