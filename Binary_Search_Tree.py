class node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setData(self,data):
        self.data = data

    def setLeft(self,left):
        self.left = left

    def setRight(self,right):
        self.right = right

class BST:
    def __init__(self,root = None):
        self.root = root

    def addI(self,data):
        if self.root is None:
            self.root = node(data)
        else:
            f = None
            s = self.root
            while s:
                f = s
                if data < s.data:
                    s = s.left
                else:
                    s = s.right
            if data < f.data:
                f.left = node(data)
            else:
                f.right = node(data)

    def add(self,data):
            self.root = BST._add(self.root,data)

    def _add(root,data):
        if root is None:
            return node(data)
        else:
            if data < root.data:
                root.left = BST._add(root.left,data)
            else:
                root.right = BST._add(root.right,data)
        return root

    def inOrder(self):
        BST._inOrder(self.root)
        print()

    def _inOrder(root):
        if root:
            BST._inOrder(root.left)
            print(root.data, end=' ')
            BST._inOrder(root.right)

    def preOrder(self):
        BST._preOrder(self.root)
        print()

    def _preOrder(root):
        if root:
            print(root.data, end=' ')
            BST._preOrder(root.left)
            BST._preOrder(root.right)

    def postOrder(self):
        BST._postOrder(self.root)
        print()

    def _postOrder(self):
        if root:
            BST._postOrder(root.left)
            BST._postOrder(root.right)
            print(root.data, end=' ')

    def printSideway(self):
        BST._printSideway(self.root, 0)
        print()

    def _printSideway(root,level):
        if root:
            BST._printSideway(root.right, level+1)
            print('   '*level, root.data, sep='')
            BST._printSideway(root.left, level+1)

    def search(self,data):
        if root.data == data:
            return root.data
        else:
            if data < root.data:
                return root.left.data
            elif data > root.data:
                return root.right.data
            else:
                return None


    
import random
t = BST()
for i in range(10):
    t.addI(random.randint(0,30))

t.inOrder()
t.printSideway()
t.add(10)
t.preOrder()
t.printSideway()