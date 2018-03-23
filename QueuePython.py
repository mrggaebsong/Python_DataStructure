class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enqueue(self,i):
        self.items.append(i)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

q = Queue()
print(q.isEmpty())
name = "Chananya"
for i in range(len(name)):
    q.enqueue(name[i])
    print(q.items)
    print(q.size())
print(q.isEmpty())
print(q.items)
while q.size() != 0:
    q.dequeue()
    print(q.items)
print(q.isEmpty())


