'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
Given the head of a linked list, remove the nth node from the end of the list and return its head.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    """ Uses a hash map that creates a index to each node
        used the index to by pass the Nth node
        Time complexity : O(n)
        Space complexity : O(n)
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        dummy = ListNode()
        cur = dummy
        dummy.next = head
        
        nodemap = {}
        i = 0
        while cur.next:
            nodemap[i] = cur
            cur = cur.next
            i = i+1
        nodemap[i-n].next = nodemap[i-n].next.next
        return dummy.next


    # using a block of n that slides to the end to gives the handle to previous node of N
    # Time complexity : O(n)
    # Space complexity : O(1)
    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = dummy

        for _ in range(n):
            right = right.next

        while right and right.next:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next


    """
    Very interesting
    recursive method that returns index back wards.
    """
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        index = 1
        def getNodeFromBack(node):
            

            if not node:
                return 0, node  # 0 index is returned from the last node in the linkedlist.
            
            index, node.next = getNodeFromBack(node.next)
            index += 1  # increment backwards
            
            if index == n:
                node = node.next # very clever, return the next node if this is the nth node.
            
            return index, node
        
        i, head = getNodeFromBack(head)
        
        return head