# https://leetcode.com/problems/linked-list-cycle-ii/submissions/1157553974/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head 
        fast = head
        visited = {slow:[0,1]}
        i = 1

        while not (fast is None or fast.next is None):
            fast = fast.next.next
            slow = slow.next
            visited[slow] = visited.get(slow,[i,0])
            visited[slow][1] += 1

            if fast == slow:
                while visited[slow][1] <= 1:
                    slow = slow.next
                    i += 1
                    visited[slow] = visited.get(slow,[i,0])
                    visited[slow][1] += 1
                return slow

            i += 1
        return None