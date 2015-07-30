# Author: Rohan Sonecha
# Stack1.py
# if sees a letter pushes it into stack, if sees a "*" pops it and prints it
li = []
def push(li,a):
    li.append(a)
def pop(li):
    return li.pop()
def main():
    string = "EUQSAE***Y****NOS*IT****I"
    for char in string:
        if (char == "*"):
            print(pop(li))
                
        else:
            push(li,char)
    print(li)
main()
