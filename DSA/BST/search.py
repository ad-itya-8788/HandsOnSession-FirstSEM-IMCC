class Node:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
def add(root,data):
  if root is None:
    return Node(data)
  if data < root.data:
    root.left=add(root.left,data)
  else:
    root.right=add(root.right,data)
  return root
def search(root,x):
  ptr=root
  level=0
  while ptr:
    if x==ptr.data:
      return level
    elif x<ptr.data:
      ptr=ptr.left
    else:
      ptr=ptr.right
    level+=1
  return -1


root=None
arr=[44,33,77,22,76,54]
for x in arr:
  root=add(root,x)
print("Search 22 level  is",search(root,22))