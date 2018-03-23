def bubble_sort(list):
    for last in range(len(list)-1,-1,-1):
        swap = False
        for i in last:
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swap = True
        if not swap:
            break
    return list

l = [5,6,2,3,0,1,4]
print("Bubble Sort")
print(l)
bubble_sort(l)
print(l)
print()

def selection_sort(list):
    for last in range(len(list)-1,-1,-1):
        biggest = l[0]
        biggest_i = 0
        for i in range(1,last+1):
            if l[i] > biggest:
                biggest = l[i]
                biggest_i = i
        l[last], l[biggest_i] = l[biggest_i], l[last]
    return list

l = [6,9,8,5,4]
print("Selection Sort")
print(l)
selection_sort(l)
print(l)
print()


def insertion(list):
    for i in range(1,len(list)):
        iEle = l[i]
        for j in range(i, -1, -1):
            if iEle > l[j-1] and j > 0:
                l[j] = l[j-1]
            else:
                l[j] = iEle
    return list

l = [8,6,7,5,9]
print("Insertion Sort")
print(l)
insertion(l)
print(l)
print()

def merge_sort(list):
    #print("Splitting ",list)
    if len(list)>1:
        mid = len(list)//2
        lefthalf = list[:mid]
        righthalf = list[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k]=lefthalf[i]
                i=i+1
            else:
                list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            list[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",list)

l = [5,3,6,1,2,7,8,4]
print("Merge Sort")
print(l)
merge_sort(l)
print(l)
print()

def quick_sort(list, first, last):
    if first < last:
        pos = partition(list, first, last)
        #print(list[first:pos-1], list[pos+1:last])
        # Start our two recursive calls
        quick_sort(list, first, pos-1)
        quick_sort(list, pos+1, last)

def partition(list, first, last):
    wall = first
    for pos in range(first, last):
        if list[pos] < list[last]: # last is the pivot
            list[pos], list[wall] = list[wall], list[pos]
            wall += 1
    list[wall], list[last] = list[last], list[wall]
    #print(wall)
    return wall

l = [5,1,4,9,6,3,8,2,7,0]
print("Quick Sort")
first = 0
last = len(l) - 1
print(l)
quick_sort(l,first,last)
print(l)
print()
