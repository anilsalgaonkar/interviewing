
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        q = deque([root])
        q.append(None)
        prev = q[0]
        while q:
            
            curr = q.popleft()
            print(curr)
            
            if curr == None:
                prev.next = None
                if len(q) >0:
                    prev = q[0]
                    q.append(None) 
                    # continue
            else:
                prev.next = curr
                prev = curr
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return root


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)

one.left = two
one.right = three
two.left = four
two.right = five
three.left = six 
three.right = seven

print(Solution().connect(one))