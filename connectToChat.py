# connecttochat.py
import random
import socket

dictionary = open("standictionary.txt","r").readlines()
li = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

def main():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("155.68.78.232",8001))
        msg = "access"
        msg = msg.encode("utf-8")
        s.send(msg)

        buf = ""
        while(buf == ""):
            buf = s.recv(512)
            if (len(buf)>0):
                buf = buf.decode("utf-8")
                print("recieved: ",buf)
                s.close()
main()
