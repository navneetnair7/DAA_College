def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

print("The 8th fibonacci number is: ", fibo(8))
print("The 16th fibonacci number is: ", fibo(16))
print("The 32nd fibonacci number is: ", fibo(32))
print("The 36th fibonacci number is: ", fibo(36))
print("The 40th fibonacci number is: ", fibo(40))