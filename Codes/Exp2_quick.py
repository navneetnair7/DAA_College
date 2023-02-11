def partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

def quickSort(a, low, high):
    if low < high:
        p = partition(a, low, high)
        quickSort(a, low, p - 1)
        quickSort(a, p + 1, high)

a = []
for i in range(10):
    a.append(50 + 51 * i)

print("The array which we will use is: ")
print(a)
print("\nFor best case: ", a)
quickSort(a, 0, 9)
print("Sorted array: ", a)
print("\nFor worst case:", a[::-1])
quickSort(a[::-1], 0, 9)
print("Sorted array: ", a)
print("\nFor random case: ", a[5:7] + a[7:] + a[3:5] + a[:3])
quickSort(a[5:7] + a[7:] + a[3:5] + a[:3], 0, 9)
print("Sorted array: ", a)