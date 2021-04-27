import socket
import threading
import time

def Work(*args):
	print(args[0].decode(),end=' ')
	print("work started")
	time.sleep(20)
	print("work stopped")

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


s.bind(("192.168.88.177",1234))

while True:
	data = s.recvfrom(1024)
	t1 = threading.Thread(target=Work,args=(data))
	t1.start()
