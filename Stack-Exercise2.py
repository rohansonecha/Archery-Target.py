# Author: Rohan Sonecha
# Stack-Exercise2.py
# reverses a random string
def push(li,a):
    li.append(a)
def pop(li):
    return li.pop()
def peek(li):
    topItem = li[len(li)-1]

def main():
    string = input("What is your string: ")
    li = []
    for i in string:
        push(li,i)
        print (i)
    print ("")
    for c in li:
        print (c)
        print (pop(li))
main()
