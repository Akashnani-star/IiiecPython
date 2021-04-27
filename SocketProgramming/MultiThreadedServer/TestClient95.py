import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto('Client95'.encode(),("192.168.88.177",1234))

