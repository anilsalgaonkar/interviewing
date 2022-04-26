# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return dummy.next


            


def create_linked_list(list_num):
    if(list_num):
        linked_list = ListNode(list_num[0])
        if(len(list_num)>1):
            temp = linked_list
            for i in range (1,len(list_num)):
                temp.next = ListNode(list_num[i])
                temp = temp.next
        return linked_list

list1 = create_linked_list([7, 14, 21, 28])
list2 = create_linked_list([])

Solution().mergeTwoLists(list1,list2)
