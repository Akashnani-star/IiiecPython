import pyttsx3 as p
import os
p.speak("Welcome to my tools")
print("Enter 1 to Open Chrome")
print("Enter 2 to Open notepad")
print("Enter 3 to Open Windows Media Player")
print("Enter 4 to Open ms paint")
print("Enter 5 to Exit")
while True:
	print("Enter Your Choice = ")
	inp = int(input())
	if inp==1:
		os.system("chrome")
	elif inp==2:
		os.system("notepad")
	elif inp==3:
		os.system("wmplayer")
	elif inp==4:
		os.system("mspaint")
	elif inp==5:
		break
	else:
		print("Doesnot Support")