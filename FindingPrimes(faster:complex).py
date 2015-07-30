# Author: Rohan Sonecha
# FindingPrimes(faster/complex).py
# finds primes using The Sieve of Eratosthenes

def main():
    print("I will take a number that you choose and see if it is prime or not")
    num = input("What is your number: ")
    num = eval(num)
    n = num
    sievep1 = []
    sievep2 = []
    while(n >= 2):
        sievep1.append(n)
        n -= 1
    print (sievep1)
    for i in sievep1:
        print(i)
        for c in range(i+1,num):
            print(c)
            if (c % i == 0 and c not in sievep2):
                sievep2.append(c)
    print (sievep2)
    print (sievep1)
    for i in sievep2:
        sievep1.remove(i)
    print ("The prime numbers below ",num,"are ",sievep1)
        
main()
