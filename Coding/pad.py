my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_lst_str = ''.join(map(str,my_lst))
print(my_lst_str[:])

for i in range(0,2):
    print(my_lst.pop(i))


print(my_lst)

d = {}
d['s'] = 1
d['e'] = 2
d['r'] = 3

for c in enumerate(d):
    print(c)


#Python3 code to demonstrate working of
# Get all substrings of string
# Using list comprehension + string slicing
  
# initializing string 
test_str = "Geeks"
  
# printing original string 
print("The original string is : " + str(test_str))
  
# Get all substrings of string
# Using list comprehension + string slicing
res = ["(" + str(i) +  "," + str(j) + ")" for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1)]

print(res)


set1  = set()
set1.add(1)
set1.add(2)
set1.add(1)
print(set1)

a1 = []
a1.append(1)
print(a1)
a1.append(2)
a1.pop()
print(a1)

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def link_list_find_rec(head, target):
    if head is None:
        return False
    return head.val == target or link_list_find_rec(head.next, target)

def link_list_find_iter(head,target):
    current = head
    while current is not None:
        if current.val == target:
            return True
        current = current.next
    return False



def linked_list_values(head):
    #base case
    if not head:
        return []  
    return [head.val] + linked_list_values(head.next)
    

def link_list_iterative(head):
    current = head
    values = []

    while current is not None:
        values.append(current.val)
        current =  current.next
    
    return values


def get_node_val(head, index):
    count = 0
    current = head
    while current is not None:
        if count == index:
            return current.val
        count += 1
        current = current.next
    return None


def get_node_val_rec(head, index):
    if head is None:
        return None
    if index == 0:
        return head.val
    return get_node_val_rec(head.next, index - 1 )
    
def reverse_list(head):
    current = head
    prev = None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next      
    return prev

# def reverse_list_rec(head):
#     if head is None:
#         return None
#     next = head.next
#     head.next = 
    


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

print("aaaaa")
print(linked_list_values(reverse_list(None)))
# print(linked_list_values(reverse_list_rec(a)))
print(get_node_val(a,7))
print(get_node_val_rec(a,2))
print(linked_list_values(a))
print(link_list_iterative(a))
print(link_list_find_rec(a, 'w'))
print(link_list_find_iter(a, 'c'))


def sum_list_rec(head):
    if head is None:
        return 0
    return head.val + sum_list_rec(head.next)

def sum_list_iter(head):
    total = 0
    current = head
    while current is not None:
        total += current.val
        current = current.next
    return total



a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e
print(sum_list_rec(a))
print(sum_list_iter(a))



badge_records = [
  ["Paul", "1355"],
  ["Jennifer", "1910"],
  ["Jose", "835"],
  ["Jose", "830"],
  ["Paul", "1315"],
  ["Chloe", "0"],
  ["Chloe", "1910"],
  ["Jose", "1615"],
  ["Jose", "1640"],
  ["Paul", "1405"],
  ["Jose", "855"],
  ["Jose", "930"],
  ["Jose", "915"],
  ["Jose", "730"],
  ["Jose", "940"],
  ["Jennifer", "1335"],
  ["Jennifer", "730"],
  ["Jose", "1630"],
  ["Jennifer", "5"],
  ["Chloe", "1909"],
  ["Zhang", "1"],
  ["Zhang", "10"],
  ["Zhang", "109"],
  ["Zhang", "110"],
  ["Amos", "1"],
  ["Amos", "2"],
  ["Amos", "400"],
  ["Amos", "500"],
  ["Amos", "503"],
  ["Amos", "504"],
  ["Amos", "601"],
  ["Amos", "602"],
  ["Paul", "1416"],
]



def gettime(records):
    
    users = {}
    
    for record in records:
        value = record[1]
        if len(value) == 1:
            while len(value) <3:
                value = value + "0"
        if len(value) == 2:
            while len(value) <4:
                value = value + "0"
        


        if record[0] not in users:
            users[record[0]] = [value]
        
        else:
            users.get(record[0]).append(value)
        
    print(users)

    out = {}
    for user in users:
        #print(sorted(users[user]))
        list =  sorted(users[user])
        slist = [list[0]]
        
        for i in range(1, len(list)):
                
            if int(list[i]) - int(list[i-1]) <100:
                        slist.append(list[i])
            else:
                if len(slist)==1:
                    slist.pop()
                    slist.append(list[i])
        out[user] = slist
    
    print(out)

                
                
gettime(badge_records)

def binsearch(input,start,end,target):
    #base case
    if not input or end-start+1<1:
        return False

    mid = (end+start)//2
    
    if input[mid]==target:
        return True
    #recursive case
    elif target > input[mid]:
        return binsearch(input,mid+1,end,target)
    else:
        return binsearch(input,start,mid,target)

def search(input,target):
    return binsearch(input,0,len(input)-1,target)

print(search([5,6],7))

