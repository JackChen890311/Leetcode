# Selection Sort
```python
s = time.time()
selection = unorder.copy()

for i in range(len(selection)):
    min = 1e10
    minidx = -1
    for j in range(i,len(selection)):
        if selection[j] < min:
            min = selection[j]
            minidx = j
    swap(selection,i,minidx)

# print(selection)
assert selection == timsort
e = time.time()
```

# Insertion Sort
```python
s = time.time()
insertion = unorder.copy()

for i in range(1,len(insertion)):
    item = insertion[i]
    for j in range(i):
        if insertion[j] > item or j == i:
            _ = insertion.pop(i)
            insertion.insert(j,item)
            break
        
# print(insertion)
assert insertion == timsort
e = time.time()
```

# Bubble Sort
```python
s = time.time()
bubble = unorder.copy()

for i in range(len(bubble)):
    for j in range(len(bubble)-i-1):
        if bubble[j] > bubble[j+1]:
            swap(bubble,j,j+1)

# print(bubble)
assert bubble == timsort
e = time.time()
print('Assertion Passed! Time:',e-s)
```

# Merge Sort
```python
s = time.time()
merge = unorder.copy()

def mergesort(list):
    l = len(list)
    if l == 1:
        return list

    left = mergesort(list[:l//2])
    right = mergesort(list[l//2:])
    leftcnt = 0
    rightcnt = 0
    result = []

    while leftcnt < len(left) and rightcnt < len(right):
        if left[leftcnt] < right[rightcnt]:
            result.append(left[leftcnt])
            leftcnt += 1
        else:
            result.append(right[rightcnt])
            rightcnt += 1
    
    remainder = right if leftcnt == len(left) else left
    remaindercnt = rightcnt if leftcnt == len(left) else leftcnt

    while remaindercnt < len(remainder):
        result.append(remainder[remaindercnt])
        remaindercnt += 1

    return result
merge = mergesort(merge)

# print(merge)
assert merge == timsort
e = time.time()
```

# Quick Sort
```python
s = time.time()
quick = unorder.copy()

def quicksort(list,s,e):
    if s >= e:
        return 
    elif s == e-1:
        _ = swap(list,s,e) if list[s] > list[e] else None
        return

    pivot = list[s]
    leftcnt = s+1
    rightcnt = e

    while leftcnt != rightcnt:
        while list[leftcnt] <= pivot and leftcnt < rightcnt:
            leftcnt += 1
        while list[rightcnt] > pivot and leftcnt < rightcnt:
            rightcnt -= 1
        if leftcnt < rightcnt:
            swap(list,leftcnt,rightcnt)
    
    if leftcnt == e and rightcnt != s+1 and pivot > list[leftcnt]:
        leftcnt += 1
    
    swap(list,s,leftcnt-1)

    quicksort(list,s,leftcnt-2)
    quicksort(list,leftcnt,e)
quicksort(quick,0,len(quick)-1)

# print(quick)
assert quick == timsort
e = time.time()
```

# Heap Sort
```python
import math
s = time.time()
heap = unorder.copy()

def heapify(list, pos, stop):
    if 2 * pos + 1 <= stop:
        maxNode = max(list[pos], list[2 * pos + 1])
        maxPos = pos if maxNode == list[pos] else 2 * pos + 1
        if 2 * pos + 2 <= stop:
            maxNode = max(maxNode, list[2 * pos + 2])
            maxPos = maxPos if maxNode != list[2 * pos + 2] else 2 * pos + 2
        if maxPos != pos:
            swap(list, pos, maxPos)
            heapify(list, maxPos, stop)

def heapsort(list):
    N = len(list)
    haveChild = math.ceil(N/2) - 1
    for i in range(haveChild, -1, -1):
        heapify(list, i, N-1)
    for i in range(N):
        swap(list, 0, N-1-i)
        heapify(list, 0, N-2-i)
heapsort(heap)

# print(heap)
assert heap == timsort
e = time.time()
```