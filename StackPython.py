class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self,i):
        self.items.append(i)
        
    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

s = Stack()
print(s.isEmpty())
name = "Chananya"
for i in range(len(name)):
    s.push(name[i])
    print(s.items)
    print(s.size())
    print(s.peek())

print(s.items)

while s.size() != 0:
    s.pop()
    print(s.items)
    print(s.isEmpty())
    



        




