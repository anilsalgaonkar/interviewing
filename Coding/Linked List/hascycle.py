def linked_list_cycle(head):
  
  if not head:
    return False
  
  slow = head
  fast = head
  
  while not (fast is None or fast.next is None):  # understand this properly. you want to fail in the first condition 
      #to prevent 2nd condition from executing to prevent None type exception
  #while  fast is not None or fast.next is not None:  # this is not a correct condition
    slow = slow.next
    fast = fast.next.next 
    if slow == fast:
      return True
  return False


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d 

linked_list_cycle(a)  # Fals