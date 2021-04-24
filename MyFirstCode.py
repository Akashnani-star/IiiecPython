import pyttsx3 as p
import speech_recognition as sr
import webbrowser as wb
import os
p.speak("Welcome to our Services")
while True:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("start say")
		audio = r.listen(source)
	inp = r.recognize_google(audio)
	print(inp)
	if ("open" in inp) and ("Chrome" in inp):
		os.system("chrome")
	elif(("open" in inp)or("run" in inp))and(("Notepad" in inp)or("text editor" in inp)):
		os.system("notepad")
	elif ("open" in inp)and(("media player" in inp) or ("windows media player" in inp)):
		os.system("wmplayer")
	elif ("open" in inp) and (("Paint" in inp) or ("mspaint" in inp)):
		os.system("mspaint")
	elif ("Google" in inp) and ("open " in inp):
		os.system("curl https://www.google.com")
	elif(("Date" in inp)or("date" in inp)):
		os.system("curl http://192.168.43.116/cgi-bin/hello.py?cmd=date")
	elif("calendar" in inp):
		os.system("curl http://192.168.43.116/cgi-bin/hello.py?cmd=cal")
	elif(("ip" in inp) or ("IP" in inp)) and (("address" in inp) or ("Address" in inp)) and (("server" in inp) or ("Server" in inp)):
		os.system("curl http://192.168.43.116/cgi-bin/hello.py?cmd=ifconfig+enp0s3")
	elif ("exit" in inp) or ("stop" in inp) or((("Switch" in inp) or("switch in inp")) and ("off" in inp)):
		break
	else:
		print("Does not Support")
print("Thanks For Using Our Services")