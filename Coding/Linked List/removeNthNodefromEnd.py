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