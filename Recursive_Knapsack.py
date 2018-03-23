def printsack(sack, max):
    global good
    global name
    for i in range(max+1):
        print(good[sack[i]], end = ' ')
    print()

def pick(sack, i, left, ig):
    global n
    global good
    if ig < n:
        price = good[ig]
        if left < price:
            pick(sack, i, left, ig+1)
        else:
            left -= price
            sack[i] = ig
            if left == 0:
                printsack(sack,i)
            else:
                pick(sack,i+1,left,ig+1)
            pick(sack,i,left+price,ig+1)

good = [20,10,5,5,3,2,20,10]
name = ['soap', 'potato chips', 'loly pop', 'toffy', 'pencil', 'rubber', 'milk','cookie']
n = len(good) # numbers of good
sack = n*[-1] # empty sack
left = 20 # money left
i = 0 # sack index
ig = 0 # good index
pick(sack, i, left,ig)
