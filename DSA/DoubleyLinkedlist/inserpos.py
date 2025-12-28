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
  def addpos(self,data,pos):
    ptr=self.head
    count=1
    newnode=Node(data)
    while ptr:
      if count==pos:
        newnode.next=ptr.next
        if ptr.next:
          ptr.next.prev=newnode
        ptr.next=newnode
        newnode.prev=ptr
        return
      count+=1
      ptr=ptr.next
arr=[1,2,3,4,5,6,7]
x=dl()
for i in arr:
  x.add(i)
x.display()
print("In Reverse Order:",end=" ")
pos=int(input("90 add at position :"))
x.addpos(90,pos)
x.display()

