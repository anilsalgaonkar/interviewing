# In addition to linked list this code also covers dynamic programming
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def create_linked_list(list_num):
    if(list_num):
        linked_list = Node(list_num[0])
        if(len(list_num)>1):
            temp = linked_list
            for i in range (1,len(list_num)):
                temp.next = Node(list_num[i])
                temp = temp.next
        return linked_list

def display(linked_list):
    if(linked_list):
        print(linked_list.data, end = " ")
        while linked_list.next is not None:
            print(linked_list.next.data, end = " ")
            linked_list = linked_list.next



# using recursive solution
# input is the head of a linked list
def reverse_using_recursive(head):
  # no need to reverse if head is null 
  # or there is only 1 node.
  if (head == None or head.next == None):
    return head
  reversed_list = reverse_using_recursive(head.next)
  head.next.next = head
  head.next = None
  return reversed_list

# using iterative solution
# input is the head of a linked list
  def reverse_using_iterative(head):
      


list_head = create_linked_list([7, 14, 21, 28])
print ("Original: ")
display(list_head)
list_head = reverse_using_recursive(list_head)
print("\nAfter Reverse: ")
display(list_head)