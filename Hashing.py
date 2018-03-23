from math import sqrt
from itertools import count, islice

def isPrime(n):
    if n<2:
        return False
    for i in islice(count(2), int(sqrt(25))-2):
        if not n % 1:
            return False

class rec:
    def __init__(self,key,data):
        self.key = key
        self.data = data

    def __str__(self):
        s = '(' + str(self.key) + ',' + str(self.data) + ')'
        return s

class hashTable:
    def __init__(self):
        self.size = 4
        self.table = [None]*self.size
        self.total = 0

    def hash(key,tablesize):
        if type(key) is str:
            sum = 0
            for pos in range(len(key)):
                sum = sum + ord(key[pos])
            return sum % tablesize

    def hash2(str,tablesize):
        sum = 0
        for pos in range(len(str)):
            sum = (sum<<5) + ord(str[pos])
        return sum % tablesize

    def rehash(j, firstHV, tablesize):
        return (firstHV + j) % tablesize

    def rehash2(j, firstHV, tablesize):
        return (firstHV + j*j) % tablesize

    def getIndex(self,key):
        index = None
        unsuccessful = False
        found = False
        i = firstHV = hashTable.hash(key,self.size)
        j = 0
        while not found and not unsuccessful:
            if self.table[i] != None and self.table[i].key == key:
                found = True
                index = i
            else:
                j += 1
                i = hashTable.rehash(j,firstHV,self.size)
                if i == firstHV:
                    unsuccessful = True
        return index

    def put(self,key,data):
        print('\n*** putting',key,data,'***')
        if self.total/self.size >= 1.0:
            self.resize()
        i = self.getIndex(key)
        if i is not None:
            print('+++ already have this key, changing data +++')
            self.table[i] = rec(key,data)
        else:
            i = firstHV = hashTable.hash(key,self.size)
            if self.table[firstHV] is None:
                self.table[firstHV] = rec(key,data)
            else:
                j = 1
                print('colission', j, 'at', i)
                i = hashTable.rehash(j,firstHV,self.size)
                unsuccessful = False
                while self.table[i] != None and not unsuccessful:
                    j += 1
                    print('colission',j,'at',i)
                    i = hashTable.rehash(j,firstHV,self.size)
                    if i == firstHV:
                        unsuccessful = True
                self.table[i] = rec(key,data)
            self.total += 1

    def __contains__(self,key):
        pass

    def get(self,key):
        data = None
        unsuccessful = False
        found = False
        i = firstHV = hashTable.hash(key,self.size)
        j = 0
        while self.table[i] != None and not found and not unsuccessful:
            if self.table[i].key == key:
                found = True
                data = self.table[i].data
            else:
                j += 1
                i = hashTable.rehash(j,firstHV,self.size)
                if i == firstHV:
                    unsuccessful = True
        return data

    def __setitem__(self,index,data):
        self.put(key,data)

    def __getitem__(self,key):
        return self.get(key)

    def resize(self):
        oldsize = self.size
        self.size = 2*oldsize
        while not isPrime(self.size):
            self.size += 1
        print('===*** resize from',oldsize,'to',self.size,'***===')
        oldTable = self.table
        self.table = [None]*self.size
        self.total = 0
        for i in range(oldsize):
            if oldTable[i] != None:
                self.put(oldTable[i].key,oldTable[i].data)

    def printTable(self):
        print('----- table size =', self.size, ', total =', self.total, ' -----')
        for i in range(self.size):
            if self.table[i] != None:
                print(i, ':', self.table[i])
        

h = hashTable()

h.put('Ann',2431)
h.printTable()
h.put('Tony',7222)
h.printTable()
h.put('Tony',7221)
h.printTable()
h.put('Jim',1026)
h.printTable()
h.put('Tom', 5555)
h.printTable()