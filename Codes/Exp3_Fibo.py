def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

print(fibo(8))
print(fibo(16))
print(fibo(32))
print(fibo(36))
print(fibo(40))

