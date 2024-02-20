#https://leetcode.com/problems/middle-of-the-linked-list/submissions/1157063320/

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:

    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow