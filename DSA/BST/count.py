class Node():
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
def add(root,data):
  if root is None:
    return Node(data)
  if data<root.data:
    root.left=add(root.left,data)
  else:
    root.right=add(root.right,data)
  return root
def inorder(root):
  if root:
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
def count(root):
  if root is None:
    return 0
  return count(root.left)+count(root.right)+1
root=None
arr=[100,20,10,30,200,150,300]
for x in arr:
  root=add(root,x)
inorder(root)
print("Total Number of Nodes:",count(root))