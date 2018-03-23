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

    def encode(self,message):
        series= [2,5,6,1,8,3]
        list = [] #String in list
        ascii = [] #num of string
        encode = [] #num to string
        for i in range (len(series)):
            self.enqueue(series[i])

        for i in range (len(message)):
            list.append(message[i])
            if list[i] == ' ':
                num = 32
                ascii.append(num)
            else :
                num = ord(list[i])+q.items[0]
                if num > 122 or (num > 90 and num < 97):
                    num = num-26
                    ascii.append(num)
                    out = self.dequeue()
                    self.enqueue(out)
                else:  
                    ascii.append(num)
                    out = self.dequeue()
                    self.enqueue(out)
            encode.append(chr(ascii[i]))
        for i in range (len(self.items)):
            self.dequeue()
        return "".join(str(x) for x in encode)

    def deCode(self,ceasar):   
        series= [2,5,6,1,8,3]
        list = []
        ascii = []
        decode = []
        for i in range (len(series)):
            self.enqueue(series[i])

        for i in range (len(ceasar)):
            list.append(ceasar[i])
            if list[i] == ' ':
                num = 32
                ascii.append(num)
            else :
                num = ord(list[i])-self.items[0]
                if  num < 65 or (num>90 and num<97):
                    num = num+26
                    ascii.append(num)
                    out = self.dequeue()
                    self.enqueue(out)
                else:  
                    ascii.append(num)
                    out = self.dequeue()
                    self.enqueue(out)
            decode.append(chr(ascii[i]))
        return "".join(str(x) for x in decode)

q = Queue()
s1 = "I love Python"
#series= [2,5,6,1,8,3]
s2 = "K quwm Saynpv"
print(q.encode(s1))
print(q.deCode(s2))
