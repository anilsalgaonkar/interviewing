
#recursive
def fib(num):

    if num <=1:
        return num
    return fib(num-1) + fib(num-2)

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(6))