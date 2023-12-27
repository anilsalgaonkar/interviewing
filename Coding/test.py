CustomerDB =  {1: {'name':"Anil", 'email': 'anil@gmail.com'}}
productDB = {1:{'name' :"Music Concert", 'location':'NYC', 'link':"https://stubhub.com/ticket/1"}}

tmpdb= {"tmplate1" : "Hi {}, Welcome to stubhub. Thanks for purchasing this {} ",
"tmplate2" : "Hi {name}, Your tickets are here. Please click here for to download the tickets. {} "}



def generateEmail(customerid,templateid,compaign):
    customer = CustomerDB.get(customerid,{})
    product = productDB.get(compaign,{})
    template = tmpdb.get(templateid,{})

    #validate()
    email = template.format(customer['name'],product['name'])
    print(email)
    #print(tmpdb["tmplate1"])

generateEmail(1,'tmplate1',1)

from datetime import date, time, datetime, timedelta

date.today()
datetime.now()
date.fromisoformat("2023-12-24")

tomorrow = timedelta(days=+1)



a = datetime(2022, 12, 28, 23, 55, 59, 342380)

print("Year =", a.year)
print("Month =", a.month)
print("Hour =", a.hour)
print("Minute =", a.minute)
print("Timestamp =", a.timestamp())

import heapq

inp = [4,5,8,2]
heapq.heapify(inp)
print(inp)
heapq.heappush(inp,3)
print(inp)
heapq.heappush(inp,6)
print(inp)
heapq.heappop(inp)
print(inp)


inp = [4,5,8,2]
print(inp)
inp = [x * -1 for x in inp]
heapq.heapify(inp)
heapq.heappush(inp,35 * -1)
print(inp)

inp = [(39,1,2),(39,4,7),(39, 0,7)]
heapq.heapify(inp)
print(inp)


#grammarly

class Student:
    def __init__(self, name, grade, age, begin, end):
        self.name = name
        self.grade = grade
        self.age = age
        self.begin = begin
        self.end = end
    def __repr__(self):
        return repr((self.name, self.grade, self.age, self.begin, self.end))

    def __eq__(self, other):
        return self.age == other.age

    def __lt_(self, other):
        return self.age < other.age
    
    def __gt_(self, other):
        return self.age > other.age

    def length(self):
        return len(self.name)
    







def getSuggestions():
    l = 0 
    r = 1
    out = []
    while r < len(students) and l <= r:
        left = students[l]
        right = students[r]

        if left.end >= right.begin:
            
            #check smaller
            if left.age == right.age:
                if left.length() <= right.length():
                    out.append(left)
                else:
                    out.append(right)
            else:
                out.append(left)
        else:
            out.append(left)
        l = r + 1
        r = l + 1
    if l < len(students):
        out.append(students[l])
    print("result : ", out)


def suggest(students):
    out = [students[0]]

    for curr in students[1:]:
        last = out[-1]
        if curr.begin <= last.end:
            if curr.age == last.age:
                if curr.length() < last.length():
                    out[-1] = curr
        else:
            out.append(curr)
    print("Suggestions:", out)



student_objects = [
    Student('john', 'A', 2, 100, 125),
    Student('jane', 'B', 2, 120, 130),
    Student('dave', 'B', 1, 132, 156),
    Student('mar', 'B', 1, 132, 156)
]

students = sorted(student_objects, reverse= True , key=lambda student: student.age)   # sort by age

print(students)
suggest(students)
        





        
    
    
