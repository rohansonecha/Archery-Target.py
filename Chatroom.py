# connecttochat.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("155.68.78.232",8001))


msg = "HELLO"
msg = msg.encode("utf-8")
s.send(msg)
