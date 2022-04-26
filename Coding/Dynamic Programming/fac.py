def fac(n):
    tmp = 1
    out = 1
    for i in range(1, n+1):
        out = i * tmp
        tmp = out
        print(out)


fac(10)