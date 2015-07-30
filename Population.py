# Author: Rohan Sonecha
# Population.py
# finds population

def main():
    print("This program will give you an approximate population for any year after or before(- yrs after)")
    secPerYear = 365 * 24 * 60 * 60
    currentPop = 318900000
    yrsAfter = input("How many years after 2015 is it: ")
    yrsAfter = eval(yrsAfter)
    approxPop = currentPop + yrsAfter * (secPerYear / 7 + secPerYear / 35 - secPerYear / 13)
    print("The approximate population in ",2015 + yrsAfter," would be ",round(approxPop))
main()
