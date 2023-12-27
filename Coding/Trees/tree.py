class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




class BinarySearchTree:
    def __init__(self):
        self.root = Node(None)
    
    def addNode(self,node, val):
        if node.val == None: 
            self.root = Node(val)
        elif node.val > val: 
            if(node.left): self.addNode(node.left,val)
            else: node.left = Node(val)
        else:
            if(node.right): self.addNode(node.right,val)
            else: node.right = Node(val)

    def printInOrder(self,node):
        if(node):
            self.printInOrder(node.left)
            print(node.val)
            self.printInOrder(node.right)
    
    def printPreOrder(self,node):
        if(node):
            print(node.val)
            self.printPreOrder(node.left)
            self.printPreOrder(node.right)

    def printPostOrder(self,node):
        if(node):
            self.printPostOrder(node.left)
            self.printPostOrder(node.right)
            print(node.val)

# this implementation is using recursion, we can also do it using queue for VFT
    def breadth_first_traversal(self,node):
            if node:
                if self.root == node: print(node.val)
                if node.left: print(node.left.val)  # printing means visiting a node left node in this case
                if node.right: print(node.right.val) # printing means visiting a node
                self.breadth_first_traversal(node.left) # traversing left tree
                self.breadth_first_traversal(node.right)  # traversing right tree
                
# this implementation is using , we can also do it using queue for VFT
    def breadth_first_traversal_queue(self,node):
            if node:
                to_visit = [node]
                while(len(to_visit) > 0):
                    visited = to_visit.pop(0)
                    print(visited.val)
                    if visited.left is not None: to_visit.append(visited.left)
                    if visited.right is not None: to_visit.append(visited.right)


    def depth_first_traversal(self, node):
        if node:
            # visit root
            if node == self.root: 
                print(node.val)

            # traverse deep into left sub tree    
            self.depth_first_traversal(node.left)
            #visit the node
            if node.left:
                print(node.left.val)
            
            # traverse deep into right sub tree 
            self.depth_first_traversal(node.right)
            
            #visit the right node
            if node.right:
                print(node.right.val)
            
            


bst = BinarySearchTree()
'''
import random
for i in random.sample(range(1,10),5):
    print(i)
    bst.addNode(bst.root,i)
print(bst.root.val)
'''

bst.addNode(bst.root,4)
bst.addNode(bst.root,6)
bst.addNode(bst.root,7)
bst.addNode(bst.root,2)
bst.addNode(bst.root,8)
bst.addNode(bst.root,3)
bst.addNode(bst.root,4)

#in order traversal of nodes --> left tree, node, right tree
print("="*20 + "In Order" + "=" *20)
bst.printInOrder(bst.root)

#Pre order traversal of node --> node, left tree, right tree
print("="*20 + "Pre Order" + "=" *20)
bst.printPreOrder(bst.root)

#Post order traversal of node --> left tree, right tree , node
print("="*20 + "Post Order" + "=" *20)
bst.printPostOrder(bst.root)

#Breadth first  traversal of node --> left node, right node , Left tree, Right Tree
print("="*20 + "Breadth First Traversal of BST using recursion" + "=" *20)
bst.breadth_first_traversal(bst.root)

#Breadth first  traversal of node --> left node, right node , Left tree, Right Tree
print("="*20 + "Breadth First Traversal of BST using Queue" + "=" *20)
bst.breadth_first_traversal_queue(bst.root)

#Depth first  traversal of node --> Left tree, Right Tree, left node, right node , 
print("="*20 + "Depth First Traversal of BST using Recursion" + "=" *20)
bst.depth_first_traversal(bst.root)



            