# Author: Rohan Sonecha
# Spell Check.py
def Hamming(word1,word2):
    hamdist = 0
    if (len(word1) < len(word2)):
        word1 = word1 + " " * (len(word2) - len(word1))
        
    if (len(word2) < len(word1)):
        word2 = word2 + " " * (len(word1) - len(word2))
        
    for i in range(len(word1)):
        if (word1[i] != word2[i]):
            hamdist += 1
    
def main():
    sentence = input("What is your sentence: ")
    sentence = sentence.split(" ")
    print(sentence)
    dictionary = open("standictionary.txt","r").readlines()

    for word in sentence:
        if (word+"\n" in dictionary):
            pass
        else:
            print ("This word is misspelled: ", word)
main()
