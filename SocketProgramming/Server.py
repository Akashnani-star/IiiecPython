import socket

#udp protocol
protocol = socket.SOCK_DGRAM

#net address family : ipv4
naf  = socket.AF_INET

s = socket.socket(naf,protocol)


port = 1234
ip= "192.168.43.229"
# we have to this for s referenced socket
# so we have to use s.bind
# we have to send the tuple of ip and port
s.bind((ip,port))


# and the recvfrom is also belongs to socket class
# that 1024 means the buffersize
while True:
	a = s.recvfrom(1024)
	print(a)
