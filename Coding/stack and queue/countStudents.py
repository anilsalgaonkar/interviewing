#https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

from collections import deque
def countStudents(students, sandwiches):
    #  sandwiches are stacked. hence converting into a stack by reversing the list
    sandwiches = sandwiches[::-1]
    counter = {}
    for s in students:
        counter[s] = counter.get(s,0) + 1

    # students are in a queue. hence converting to a queue
    students = deque(students)

    topsandwich = sandwiches[-1]
    while sandwiches and counter[topsandwich] != 0:
        firstStudent = students.popleft()
        if firstStudent == topsandwich:
            counter[topsandwich] -= 1
            sandwiches.pop()
            if sandwiches:
                topsandwich = sandwiches[-1]
        else:
            students.append(firstStudent)
    
    return len(students)


assert countStudents([1,1,0,0],[0,1,0,1])==0, "count should be 0"
assert countStudents([1,1,1,0,0,1],[1,0,0,0,1,1])==3, "count should be 3"

import unittest
class Test(unittest.TestCase):
    def test_uc1(self):
        assert countStudents([1,1,0,0],[0,1,0,1])==0, "count should be 0"
    
    def test_uc2(self):
        assert countStudents([1,1,0,0],[0,1,0,1])==0, "count should be 0"

unittest.main()