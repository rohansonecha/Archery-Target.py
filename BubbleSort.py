# Author: Rohan Sonecha
# Bubble Sorting.py
import random


def bubble(li,i,timeSwap):
    
    while (i < len(li)-1):
        if (li[i] == li[i + 1]):
            pass
        elif (li[i] > li[i + 1]):
            pass
        else:
            a = li[i]
            b = li[i + 1]
            li[i] = b
            li[i + 1] = a
            timeSwap += 1
            
        i += 1    

    if (timeSwap == 0):
        print("List has been sorted")
    else:
        i = 0
        timeSwap = 0
        bubble(li,i,timeSwap)
    return li
def main():
    li = []
    i = 0
    timeSwap = 0
    for i in range(6):
        li.append(random.randint(1,100))
    print (li)
    answer = bubble(li,i,timeSwap)
    print ("Your list is sorted: ",li)
main()


'''
    
    obj1 = li[i]
    obj2 = li[i + 1]

while (i <= len(li)):

    elif (li[i] == li[i + 1]):
        pass
    elif (li[i] < li[i + 1]):
        pass
    else:
        a = li[i]
        li[i] = li[i + 1]
        li[i + 1] = a
    i += 1

obj3 = li[0]
obj4 = li[1]
for c in range(len(li)):
    if (i == len(li)-1):
        break
    elif (obj3 >= obj4):
        obj3 = li[c]
        obj4 = li[c + 1]
        timeSwap += 1

'''
