class Node():
  def __init__(self,data):
    self.data=data
    self.next=next
class queue:
  def __init__(self):
    self.front=self.rear=None
  def add(self,data):
    newnode=Node(data)
   if self.front is None:
    self.front=newnode
   else:
    self.rear=newnode
    self.front=rear