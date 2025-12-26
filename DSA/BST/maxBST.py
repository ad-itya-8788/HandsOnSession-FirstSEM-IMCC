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
def max(root):
  ptr=root
  while ptr.right:
    ptr=ptr.right
  return ptr.data

root=None
arr=[44,22,33]
for x in arr:
  root=add(root,x)
print("Max is",max(root))