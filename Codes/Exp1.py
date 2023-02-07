def insertionSort(a, n):
    time = 0
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            time += 1
        a[j + 1] = key
    print("The sorted array using insertion sort is ", a)
    print("The number of exchanges is: ", time)

def selectionSort(a, n):
    time = 0
    for i in range(0, n - 1):
        mini = i
        for j in range(i + 1, n):
            if a[j] < a[mini]:
                mini = j
        if i != mini:
            time += 1
        a[i], a[mini] = a[mini], a[i]
        
    print("The sorted array using selection sort is ", a)
    print("Number of exchanges: ", time)

a = []
for i in range(10):
    a.append(50 + (50 + 1) * i)

print("\nThe array we are using to find out the time complextites is:", a)
print("\nThe input for the Best case is- ", a)
print("The input for the Worst case is- ", a[::-1])
print("Random sample input-", a[5:7] + a[7:] + a[3:5] + a[:3])
print("\nFor best case- ")
print(a)
insertionSort(a, 10)
selectionSort(a, 10)
print("\nFor worst case- ")
print(a[::-1])
insertionSort(a[::-1], 10)
selectionSort(a[::-1], 10)
print("\nFor the random case- ")
print(a[5:7] + a[7:] + a[3:5] + a[:3])
insertionSort(a[5:7] + a[7:] + a[3:5] + a[:3], 10)
selectionSort(a[5:7] + a[7:] + a[3:5] + a[:3], 10)