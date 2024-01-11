class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

# insert nodes into a bst and return the root.
def insert(root,val):
    if not root:
        root = TreeNode(val)
    
    elif val <= root.val:
        root.left = insert(root.left,val)
    else:
        root.right = insert(root.right,val)
    return root

#  remove node from the bst and return the root
def remove(root,val):
    # base case 
    if root is None:
        return None
    if val < root.val:
       root.left =  remove(root.left,val)
    elif val > root.val:
        root.right = remove(root.right, val)
    elif val == root.val:
        if root.left is None:
            return root.right
        elif not root.right:
           return root.left
        else:
            minnode = findmin(root.right) # find the min node in right subtree.
            root.val = minnode.val # assign the min val to current node --> essentially removing the current node
            root.right = remove(root.right,minnode.val) # remove the min node from the right sub tree.
    return root


#loop through left subtree and get the left most leaf
def findmin(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

#loop through right and get the rightmost leaf
def findmax(root):
    curr = root
    while curr and curr.right:
        curr = curr.right
    return curr

def preordertraversal(node):
    if node:
        print(node.val,end = " --> ")
        preordertraversal(node.left)
        preordertraversal(node.right)

def postordertraversal(bst):
    if bst:
        postordertraversal(bst.left)
        postordertraversal(bst.right)
        print(bst.val, end = " --> ")

def inordertraversal(node):
    if node:
        inordertraversal(node.left)
        print(node.val ,end = " --> ")
        inordertraversal(node.right)


#   2
# /  \
#1      3
# \      \
#   2       4
#            \
#               5
bst = None
bst = insert(bst,2)
bst = insert(bst,1)
bst = insert(bst,3)
bst = insert(bst,4)
bst = insert(bst,2)
bst = insert(bst,5)

preordertraversal(bst)
print("\n")
postordertraversal(bst)
print("\n")
inordertraversal(bst)
print("\n")

remove(bst, 2)
remove(bst, 5)
bst = insert(bst,6)

preordertraversal(bst)


