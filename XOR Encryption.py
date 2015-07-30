# Author: Rohan Sonecha
# XOR Encryption
def binconvert(base10):
    binary = bin(base10)
    return binary

def stringAscii(li,message):
    for i in message:
        i = ord(i)
        li.append(i)
        print (i)
    return li

def main():
    key = ['0','1','0','0','0','0','1','1','0','1','1','0','1','0','0','0','0','1','1','0','0','1','0','1','0','1','1','0','0','0','1','1','0','1','1','0','1','0','1','1']
    message = input("What is your message: ")
    messli = []
    
    messli = stringAscii(messli,message)
    li = []
    for i in messli:
        print (i)
        binaryletter = binconvert(i)
        li.append(binaryletter)
    print ("Your message is ",li," in binary")
    

    if (len(li) > len(key)):
        lengthOfList = len(li)
        for i in range(len(li)-len(key)):
            key.append(key[i])
    elif (len(li) < len(key)):
        lengthOfList = len(li)
        for i in range(len(key)-len(li) + 1):
            key.remove(lengthOfList-i)
    finalmess = ''
    i = 0
    while (i < len(li)):
        if li[i] == key[i]:
            finalmess += '0'
        else:
            finalmess += '1'
        i += 1
    
main()
