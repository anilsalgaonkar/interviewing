#https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")  # remove all the white space 
        return self.eval(s)

    def eval(self,s):
        if s.isnumeric():
            return int(s)
        i = 0
        first = '' 
        pre = ''
        op_stack = []
        print(s)
        while i < len(s) and (s[i] != "*" or s[i] != "/"):
            first = '' 
            while i < len(s) and s[i].isdigit() : #find first operator
                first += s[i]
                i += 1 
            first = int(first) if first else first
            if op_stack:  
                prev_op, prev_operand = op_stack.pop()
                
                if prev_op == "+":
                    first += prev_operand
                if prev_op == "-":
                    first = prev_operand - first
            print(s[i], i)
            if s[i] == "-" or s[i] == "+":
                op_stack.append((s[i],first))
            
            i += 1


        op = s[i] # operator
        second = self.eval(s[i+1:]) # second operand
        return self.eval_op(first, second, op)

    def eval_op(self, first, second, op):
        if op == "+":
            return first + second
        if op == "-":
            return first - second
        if op == "*":
            return first * second
        if op == "/":
            return first // second


sol = Solution()
print(sol.calculate("1-1+1"))


"""
inp = " 3+2*2 "
inp = "3+2*2"
eval("3+2*2") = 7

first = 3
op = + 
second = 4
eval_op(3,4,+) = 7


inp = "2*2"
first = 2
op = *
second = 2
eval_op (2,2,*) = 4


inp = "2"



"""