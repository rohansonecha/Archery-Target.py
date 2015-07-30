# Author: Rohan Sonecha
# binSearch.py
# finds number in list of numbers

def binSearch(li,a):
    if (li == []):
        return False
    pivot = len(li)//2
    mid = li[pivot]
    if (mid == a):
        return a
    if (a < mid):
        sublist = li[0:pivot]
        return binSearch(sublist,a)
    if(a > mid):
        sublist = li[pivot + 1:]
        return binSearch(sublist,a)
def main():
    a = input("What number would you like to search for: ")
    a = eval(a)
    li = [4,8,12,15,24,34]
    result = binSearch(li,a)
    print ("There is a ",result, " in your list.")
main()
