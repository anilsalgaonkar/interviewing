#https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode()
        dummy = tail
        carry = 0
        while l1 and l2:
            op1 = l1.val
            op2 = l2.val
            curr_sum = op1 + op2 + carry
            carry = 0
            if curr_sum >= 10:
                carry = curr_sum // 10
                curr_sum = curr_sum % 10
            tail.next = ListNode(curr_sum)
            tail = tail.next
            l1 = l1.next
            l2 = l2.next
  
        while l1:
            curr_sum = carry + l1.val
            print(carry, l1.val , curr_sum)
            carry = 0
            if curr_sum >= 10:
                carry = curr_sum // 10
                curr_sum = curr_sum % 10
            tail.next = ListNode(curr_sum)
            tail = tail.next
            l1 = l1.next

        while l2:
            curr_sum = carry + l2.val
            print(carry, l2.val , curr_sum)
            carry = 0
            if curr_sum >= 10:
                carry = curr_sum // 10
                curr_sum = curr_sum % 10
            tail.next = ListNode(curr_sum)
            tail = tail.next
            l2 = l2.next
        
        if carry:
            tail.next = ListNode(carry)

        return dummy.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

        