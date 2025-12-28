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
  def revorder(self):
    ptr=self.head
    while ptr.next:
      ptr=ptr.next
    while ptr:
      print(ptr.data,end="<-")
      ptr=ptr.prev
    print("None")

arr=[1,2,3,4,5,6,7]
x=dl()
for i in arr:
  x.add(i)
x.display()
print("In Reverse Order:",end=" ")
x.revorder()