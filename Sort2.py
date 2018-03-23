def bubble(l):
    for last in range(len(l)-1,-1,-1):
        swaped = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swaped = True
        if not swaped:
            break
    return l

l = [5,6,2,3,0,1,4]
print("Bubble Sort")
print(l)
print(bubble(l))
print()

def selection(l):
    for last in range(len(l)-1,-1,-1):
        biggest = l[0]
        biggest_i = 0
        for i in range(1,last+1):
            if l[i] > biggest:
                biggest = l[i]
                biggest_i = i
        l[last], l[biggest_i] = l[biggest_i],l[last]
    return l

l = [6,9,8,5,4]
print("Selection Sort")
print(l)
print(selection(l))
print()

def insertion(l):
    for i in range(1,len(l)):
        iEle = l[i]
        for j in range(i,-1,-1):
            if iEle < l[j-1] and j > 0:
                l[j] = l[j-1]
            else:
                l[j] = iEle
                break
    return l

l = [4,1,6,5,3,2]
print("Insertion Sort")
print(l)
print(insertion(l))
print()

def shell(l,dIncrement):
    for inc in dIncrement:
        for i in range(inc,len(l)):
            iEle = l[i]
            for j in range(i, -1, -inc):
                if iEle < l[j-inc] and j >= inc:
                    l[j] = l[j-inc]
                else:
                    l[j] = iEle
                    break
    return l

l = [10,11,1,13,2,6,4,12,5,8,7,9,3]
dIncrement = [5,3,1]
print("Shell Sort")
print(l,",",dIncrement)
print(shell(l,dIncrement))
print()

def mergeSort(l,left,right):
    center = (left+right)//2
    if left < right:
        mergeSort(l,left,center)
        mergeSort(l,center+1,right)
        merge(l,left,center+1,right)
    return l

def merge(l,left,right,rightEnd):
    start = left
    leftEnd = right - 1
    result = []
    while left <= leftEnd and right <= rightEnd:
        if l[left] < l[right]:
            result.append(l[left])
            left += 1
        else:
            result.append(l[right])
            right += 1
    while left <= leftEnd:
        result.append(l[left])
        left += 1
    while right <= rightEnd:
        result.append(l[right])
        right += 1
    for ele in result:
        l[start] = ele
        start += 1
        if start > rightEnd:
            break


l = [5,3,6,1,2,7,8,4]
print("Merge Sort")
print(l)
print(mergeSort(l,0,len(l)-1))
print()

def quick(l,left,right):
    if left < right:
        pivot = l[left]
        i, j = left+1, right
        while i < j:
            while i < right and l[i] <= pivot:
                i += 1
            while j > left and l[j] >= pivot:
                j -= 1
            if i < j:
                l[i], l[j] = l[j], l[i]
        if left is not j:
            l[left], l[j] = l[j], pivot
        quick(l,left,j-1)
        quick(l,j+1,right)
    return l

l = [5,1,4,9,6,3,8,2,7,0]
print("Quick Sort")
print(l)
print(quick(l,0,len(l)-1))
print()