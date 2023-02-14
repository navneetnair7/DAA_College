def bubble(a, n):
    count = 0
    if n == 1:
        return
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            count += 1
    if count == 0:
        return
    bubble(a, n - 1)

a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble(a, 10)
print(a)