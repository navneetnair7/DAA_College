def merge(a, low, mid, high):
    b = [0] * len(a)
    h, i, j = low, low, mid + 1
    count = 0
    while h <= mid and j <= high:
        if a[h] <= a[j] and j <= high:
            b[i] = a[h]
            h += 1
        else:
            b[i] = a[j]
            count += 1
            j += 1
        i += 1
    
    if h > mid:
        for k in range(j, high+1):
            b[i] = a[k]
            i += 1
    else:
        for k in range(h, mid+1):
            b[i] = a[k]
            i += 1
    
    for k in range(low, high+1):
        a[k] = b[k]

def mergeSort(a, low, high):
    if low < high:
        mid = low + (high - low) // 2
        mergeSort(a, low, mid)
        mergeSort(a, mid + 1, high)
        merge(a, low, mid, high)

a = []
for i in range(0, 10):
    a.append(50 + 51 * i)
print("The array which we will use is: ")
print(a)
print("\nFor best case: ", a)
mergeSort(a, 0, 9)
print("\nFor worst case:", a[::-1])
mergeSort(a[::-1], 0, 9)
print("\nFor random case: ", a[5:7] + a[7:] + a[3:5] + a[:3])
mergeSort(a[5:7] + a[7:] + a[3:5] + a[:3], 0, 9)
mergeSort(a, 0, 3)
print(a)