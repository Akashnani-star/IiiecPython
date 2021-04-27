import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# we have to send byteString
s.sendto("hello".encode(), ("192.168.43.229",1234))
