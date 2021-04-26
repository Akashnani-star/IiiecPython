print("Enter ur choices = ",end="")

try:
	inp = input()
	if int(inp)==1:
	    print("1")
	elif int(inp)==2:
	    print("2")
	elif int(inp)==3:
	    print("3")
	else:
	    print("Sorry I can't help")
except ValueError:
	print("Wrong Value Entered....")
	print("Enter only numbers....")
except:
	print("mail to developer")

finally:
	print("mailto..")

	print("bye")

