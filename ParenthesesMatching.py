class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def match(open,c):
    if open == '(' and c == ')':
        return True
    elif open == '[' and c == ']':
        return True
    elif open == '{' and c =='}':
        return True
    else:
        return False

str = "( 3 + 2 ) / { 4**5 }"
s = Stack()
error = False
for c in str:
    if c in '({[':
        s.push(c)
    elif c in ')}]':
        if s.isEmpty():
            error = True
        else:
            open = s.pop()
            if match(open,c) == False:
                error = True

if error:
    print('MISMATCH')
else:
    if s.isEmpty():
        print('MATCH')
    else:
        print('MISMATCH open paren. exceed')

print(s.items)
