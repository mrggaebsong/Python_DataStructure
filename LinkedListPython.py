class Term:
    def __init__(self, num, power=0):
        self.num = num
        self.power = power

    def __str__(self):
        if self.num == 0:
            return ''
        else:
            if self.num > 0:
                s = '+'
            else:
                s = ''

            if self.power == 0:
                return s + str(self.num) + ' '
            else:
                if self.num == -1:
                    s += '-'
                else:
                    if self.num != 1:
                        s += str(self.num)
                    else:
                        s += ''
            if self.power not in [1,0]:
                s += 'n' + str(self.power)
            else:
                s += 'n'
            return s + ' '

    def __lt__(self, rhs):
        return self.num < rhs.num

    def __add__(self, rhs):
        if self.power == rhs.power:
            return Term(self.num + rhs.num, self.power)


class OrderedList:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def index(self,i):
        return self.items.index(i)

    def add(self,i):
        if self.isEmpty():
            self.items.append()
        else:
            index = 0
            while index < self.size() and self.items[index] < i:
                index += 1
            if index == self.size() or self.items[index] != 1:
                self.items.insert(index,i)
            else:
                self.items[index] += 1

    def insert(self, i):
        for (idx, x) in enumerate(self.items):
            if x.power == i.power:
                self.items[idx] = x + i
                break
        else:
            self.items.append(i)
        self.items.sort(key=lambda x: x.power, reverse=True)

    def __str__(self):
        return ''.join(str(i) for i in self.items)

    def __add__(self, rhs):
        for t in rhs.items:
            self.insert(t)
        return self
    
    def solve(self, i):
        ans = 0
        for t in self.items:
            ans += t.num * (i ** t.power)
        return ans

    def remove(self,i):
        self.items.remove(i)

    def search(self,i):
        if i in self.items:
            return True
        else:
            return False

    def pop(self,p = None):
        if p == None:
            return self.items.pop()
        else:
            return self.items.pop(p)


A = OrderedList()
A.insert(Term(3, 95))
A.insert(Term(10, 4))
A.insert(Term(1, 7))
print(A)

B = OrderedList()
B.insert(Term(-1, 1))
B.insert(Term(1))
B.insert(Term(15, 3))
B.insert(Term(-2, 4))
B.insert(Term(4, 2))
B.insert(Term(21, 100))
B.insert(Term(-7, 95))
print(B)
C = A + B
print(C)