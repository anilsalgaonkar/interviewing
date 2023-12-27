
#n   =	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	...
#fib =	0	1	1	2	3	5	8	13	21	34	55	89	144	233	377


#recursive
def fib(num):

    if num <=1:
        return num
    return fib(num-1) + fib(num-2)

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(6))