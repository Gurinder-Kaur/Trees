class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insertHelp(self.root,new_val)

    def insertHelp(self,ptr,new_val):
        if ptr.value<new_val:
            if ptr.right:
                self.insertHelp(ptr.right,new_val)
            else:
                ptr.right=Node(new_val)
        else:
            if ptr.left:
                self.insertHelp(ptr.left,new_val)
            else:
                ptr.left=Node(new_val)

    def search(self, find_val):
        ptr=self.root
        while ptr:
            if ptr.value==find_val:
                return True
            elif ptr.value<find_val:
                ptr=ptr.right
            else:
                ptr=ptr.left
        return False

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))
