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
def inorder(root):
  if root:
    inorder(root.left)
    print(root.data)
    inorder(root.right)

root=None
arr=[44,22,33]
for x in arr:
  root=add(root,x)
inorder(root)