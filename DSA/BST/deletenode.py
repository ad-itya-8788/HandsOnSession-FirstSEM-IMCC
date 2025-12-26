class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def add(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = add(root.left, data)
    else:
        root.right = add(root.right, data)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def deleteNode(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = deleteNode(root.left, data)

    elif data > root.data:
        root.right = deleteNode(root.right, data)

    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        temp = root.right
        while temp.left:
            temp = temp.left

        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)

    return root


root = None
arr = [100,20,10,30,200,150,300]
for x in arr:
    root = add(root, x)

print("Before delete:")
inorder(root)

root = deleteNode(root, 20)

print("\nAfter delete:")
inorder(root)
