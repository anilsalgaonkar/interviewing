class Node:
    def __init__(self,val):
        self.next = None
        self.prev = None
        self.val = val


class Deque:
    
    def __init__(self):
        self.head = Node(None)
        self.tail =  self.head

    def isEmpty(self) -> bool:
        return self.head.val == None:


    def append(self, value: int) -> None:
        lastnode = Node(value)
        self.tail.next = lastnode
        self.tail = lastnode

    def appendleft(self, value: int) -> None:
        firstnode = Node(value)
        firstnode.next = self.head
        self.head = firstnode


    def pop(self) -> int:
        self.tail.prev.next = None
        self.tail = self.tail.prev
        

    def popleft(self) -> int:
        self.head.next.prev = None
        self.head = self.head.next