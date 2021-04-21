import pyttsx3 as p
import os
p.speak("Welcome to our Services")
while True:
    print("Enter Your Requiremetns = ",end='')
    inp = input()
    if ("open" in inp) and ("chrome" in inp):
        os.system("chrome")
    elif(("open" in inp)or("run" in inp))and(("notepad" in inp)or("text editor" in inp)):
        os.system("notepad")
    elif ("open" in inp)and(("media player" in inp) or ("windows media player" in inp)):
        os.system("wmplayer")
    elif ("open" in inp) and (("paint" in inp) or ("mspaint" in inp)):
        os.system("mspaint")
    elif ("exit" in inp) or ("stop" in inp):
        break
    else:
        print("Doesnot Support")
print("Thanks For Using Our Services")