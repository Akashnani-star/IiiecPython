import threading
def a():
	while True:
		print("aaaa")

def v():
	while True:
		print("vvvv")




t1 = threading.Thread(target=a)
t2 = threading.Thread(target=v)



t1.start()
t2.start()