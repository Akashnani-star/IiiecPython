import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto('Client26'.encode(),("192.168.88.177",1234))

