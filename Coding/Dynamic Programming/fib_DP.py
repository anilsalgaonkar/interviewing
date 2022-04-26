#from memory_profiler import profile


#@profile()
def fib_memo(num, memo={}):
    print(num, ' ')
    if (num in memo): return memo[num]
    if (num <= 2): return 1

    memo[num] = fib_memo(num - 1, memo) + fib_memo(num - 2, memo)
    return memo[num]


print(fib_memo(5, {}))


#@profile()
def fib_tab(num):
    fibarr = [0] * (num + 1)
    fibarr[1] = 1

    for i, val in enumerate(fibarr):
        # print("before --> ",i, fibarr[i], fibarr[i+1],fibarr[i+2])
        if i < num:
            fibarr[i + 1] += fibarr[i]
        if i < num - 1:
            fibarr[i + 2] += fibarr[i]
        # print("after --> ",i)
        # print(fibarr)

    print(fibarr)
    return fibarr[num]


#print(fib_tab(5))


# space complexity  == 3+n =n
# time complexity == n
def fib_simple(n):
    a = 0
    b = 1
    c = 0
    for i in range(n):
        c = a + b
        a = b
        b = c
    return c


print(fib_simple(0))

