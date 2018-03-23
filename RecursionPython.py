def printNdown(n):
    if n > 0:
        print(n)
        printNdown(n-1)

printNdown(10)

def printToN(n):
    if n > 0:
        printToN(n-1)
        print(n)

printToN(10)

def sumToN(n):
    if n == 1:
        return 1
    else:
        return n + sumToN(n-1)

print(sumToN(10))

def printForw(L,i):
    if i < len(L):
        print(L[i])
        printForw(L, i+1)
    else:
        print()

L = [ 2, 3, 5, 7, 11 ]
printForw(L,0)

def printBack(L,i):
    if i < len(L):
        printBack(L, i+1)
        print(L[i])
    else:
        print()

printBack(L,0)

def App(L,i):
    if i == 1:
        L.append(1)
    else:
        App(L, i-1)
        L.append(i)

list = []
App(list,10)
print(list)

def AppB(L,i):
    if i == 1:
        L.append(1)
    else:
        L.append(i)
        AppB(L, i-1)

l = []
AppB(l, 10)
print(l)

#########################################

class node:
    def __init__(self, d, nxt = None):
        self.data = d
        if nxt is None:
            self.next = None
        else:
            self.next = nxt

def printList(h):
    if h is not None:
        print(h.data, end = ' ')
        printList(h.next)

def createL(h, n):
    if n:
        p = node(n, h)
        p = createL(p, n-1)
        return p
    else:
        return h

h = None
h = createL(h, 5)
print(printList(h))

def createLfromlist(h, i):
    global fromList
    if i >= 0:
        p = node(fromList[i], h)
        p = createLfromlist(p, i-1)
        return p
    else:
        return h

fromList = [2,5,4,8,6,7,3,1]
i = len(fromList)-1
print(fromList, 'len =', i+1)
h = None
h = createLfromlist(h, i)
printList(h)
print()

def sumEven(list,i,j):
    sum = 0
    if i > j:
        return sum
    else:
        if list[i] % 2 == 0:
            sum += list[i]
            return sum + sumEven(list, i+1,j)
        else:
            return sum + sumEven(list, i+1,j)

print(sumEven(fromList,0,6))