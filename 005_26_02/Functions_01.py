def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
def NewFac(n):
    if n == 0:
        return 1
    else:
        return n * NewFac(n-1)


print(factorial(12))
print(NewFac(12))