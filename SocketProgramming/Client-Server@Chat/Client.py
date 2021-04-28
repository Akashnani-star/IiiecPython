import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	username = {1234:"Akash"}
	ins = input("Enter what you want to send to {0} : ".format(username[1234]))
	s.sendto(ins.encode(),("192.168.88.177",1234))
	msg = s.recvfrom(1024)
	print("{0} : {1}".format(username[1234],msg[0].decode()))
	