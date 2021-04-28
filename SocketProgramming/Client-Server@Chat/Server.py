import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("192.168.88.177",1234))

while True:
	username = {1234:"Akash"}
	msg = s.recvfrom(1024)
	username[msg[1][1]] = "Another"
	print("{0} : {1}".format(username[msg[1][1]],msg[0].decode()))
	ins = input("Enter what you want to send to {0} : ".format(username[msg[1][1]]))
	s.sendto(ins.encode(),msg[1])