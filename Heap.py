class node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def add(root,data):
    if not root :
        return node(data)
    else:
        if data < root.data:
            root.left = add(root.left,data)
        else:
            root.right = add(root.right,data)
    return root

def print90(list,index,level):
    if index < len(list) - 1:
        print90(list,2*index+1,level+1)
        print('   '*level,list[index],sep=' ')
        print90(list,index*2,level+1)

def printList(list,index):
    if index == len(list):
        pass
    else:
        print(list[index],end = ' ')
        printList(list,index+1)

def max_heap_sort(list):
    for i in range(len(list)-1,0,-1):
        max_heapify(list, i)
        
        temp = list[0]
        list[0] = list[i]
        list[i] = temp

	
def max_heapify(list, end):
    last_parent = int((end-1)/2)

    for parent in range(last_parent,-1,-1):
        current_parent = parent

        while current_parent <= last_parent:
            child = 2*current_parent + 1
            if child + 1 <= end and list[child] < list[child+1]:
                child = child + 1

            if list[child] > list[current_parent]:
                temp = list[current_parent]
                list[current_parent] = list[child]
                list[child] = temp

                current_parent = child
            else:
                break
		

def min_heap_sort(list):
    for i in range(0, len(list)-1):
        min_heapify(list, i)
	

def min_heapify(list, start):
    end = len(list)-1
    last_parent = int((end-start-1)/2)

    for parent in range(last_parent,-1,-1):
        current_parent = parent

        while current_parent <= last_parent:
            child = 2*current_parent + 1
            if child + 1 <= end-start and list[child+start] > list[child+1+start]:
                child = child + 1

            if list[child+start] < list[current_parent+start]:
                temp = list[current_parent+start]
                list[current_parent+start] = list[child+start]
                list[child+start] = temp

                current_parent = child
            else:
                break

l = [68,65,32,24,26,21,19,13,16,14]
printList(l,0)
print()
print90(l, 1, 0)
print()
h = []
for ele in l:
    h.append(ele)

print(h)
max_heap_sort(h)
print(h)
min_heap_sort(h)
print(h)