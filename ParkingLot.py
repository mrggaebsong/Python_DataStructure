class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def isEmpty(self):
        return self.items == []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isFull(self):
        return len(self.items) == 4

    def arrive(self,list):
        if self.isFull():
            return "Car " + str(list) + " cannot arrive: SOI full"
        else:
            self.push(list)
            return "Car " + str(list) + " space " + str(4-self.size())

    def depart(self,list):
        if self.isEmpty():
            return "Car " + str(list) + " cannot depart: SOI empty"
        elif list not in self.items:
            return "Car " + str(list) + " cannot depart: no car " + str(list)
        else:
            soi = []
            for i in range(4):
                if self.items[len(self.items)-i-1] == list and len(self.items)-i-1>=0:
                    print(self.items[len(self.items)-i-1])
                    self.items.pop(len(self.items)-i-1)


s = Stack()
s.arrive(1)
s.arrive(2)
s.arrive(3)
s.arrive(4)
print(s.items)
s.depart(3)
print(s.items)
s.depart(2)
print(s.items)