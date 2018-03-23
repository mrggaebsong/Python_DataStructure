class node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)

def preOrder(root):
    if root:
        print(root.data, end=' ')
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=' ')

def addi(root,data):
    if not root :
        return node(data)
    else:
        if data < root.data:
            root.left = addi(root.left,data)
        else:
            root.right = addi(root.right,data)
    return root

def add(root,data):
    if root is None:
        return node(data)
    else:
        if data < root.data:
            root.left = add(root.left, data)
        else:
            root.right = add(root.right, data)
    return root

def printSideWay(root,level):
    if root:
        printSideWay(root.right, level+1)
        print(' ' * 3 * level, root.data)
        printSideWay(root.left, level+1)

def height(root):
    if not root:
        return -1
    else:
        hleft = height(root.left) + 1
        hright = height(root.right) + 1
        if hleft > hright:
            return hleft
        else:
            return hright

def path(root,data):
    if root.data != data:
        print(root.data, end = ' ')
        if data < root.data:
             path(root.left,data)
        else:
             path(root.right,data)
    else:
        print(data)

def search(root,data):
    if not root:
        return None
    if root.data == data:
        return root
    else:
        if data < root.data:
            search(root.left,data)
        else:
            search(root.right,data)

def depth(root,data):
    if root.data == data:
        return 0
    else:
        if data < root.data:
            return depth(root.left,data)+1
        else:
            return depth(root.right,data)+1

def doubleMore(root,data):
    if root:
        if root.data > data:
            print("double node goes: ",root.data,"->",root.data*2)
            root.data *= 2
            doubleMore(root.left,data)
            doubleMore(root.right,data)
        else:
            print("double node goes: ",root.data)
            doubleMore(root.right,data)
    return root

def presuccessor(root):
    if root.right == None:
        return root
    else:
        return presuccessor(root.right)

def delete(root,data):
    if search(root.data,data):
        if root != None:
            if data < root.data:
                if data == root.left.data:
                    if root.left.left == root.left.right == None:
                        root.left = None
                    elif root.left.left == None:
                        root.left = root.left.right
                    elif root.left.right == None:
                        root.left = root.left.left
                    else:
                        pre = presuccessor(root.left.left)
                        delete(root,pre.data)
                        root.left.data = pre.data
                else:
                    delete(root.left,data)
            else:
                if data == root.right.data:
                    if root.right.left == root.right.right == None:
                        root.right = None
                    elif root.right.left == None:
                        root.left = None
                    elif root.right.right == None:
                        root.right = None
                    else:
                        pre = presuccessor(root.right.left)
                        delete(root,pre.data)
                        root.right.data = pre.data
                else:
                    delete(root.right,data)
    return root

l = [14,4,9,7,15,3,18,16,20,5,16]
print('input: ',l)
r = None

for ele in l:
    r = addi(r, ele)

print('inorder:', end = ' ')
inOrder(r)
print()
print('printSideWay:')
printSideWay(r, 0)

print('height of ', r.data, '=', height(r))

d = 5
print('path:', d, '=', end = ' ')
path(r, d)

d = 9
search(r,d)

d = 18
print('depth of node data ', d, '=', depth(r, d))
print()


d = 8
doubleMore(r,d)
printSideWay(r,0)

delete(r,d)
printSideWay(r,0)
