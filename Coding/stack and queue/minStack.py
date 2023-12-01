#https://leetcode.com/problems/min-stack/

class MinStack(object):

    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        elif val < self.minstack[-1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1]) 
        

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        self.minstack.pop()
        return val
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
        

ops = ["MinStack","push","push","push","getMin","pop","top","getMin"]
val  = [[],[-2],[0],[-3],[],[],[],[]]

ms = MinStack()
out = [None]
for i,op in enumerate(ops):


    if op == "push":
        ms.push(val[i])
        out.append(None)
    if op == "pop":
        ms.pop()
        out.append(None)
    if op == "top":
        out.append(ms.top())
    if op == "getMin":
        out.append(ms.getMin())

print(out)





# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()