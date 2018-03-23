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
print(fromList)
h = None
h = createLfromlist(h, i)
printList(h)

def delete(h, d):
    h = h.head
    if h.next.data == d:
        h.next = h.next.next
    delete(h.next,d)
    return h

h = delete(h,5)
