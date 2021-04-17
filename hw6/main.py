print ("Hello this is our calendar application")
print ("Please choouse your option: ")
print ("1.Write new date")
print ("2.Read all dates")
print ("3.Exit")
messageFromUser = input()

if messageFromUser == "1":
	print ("Enter your new date: ")
	newDate = input()
	calendar = open("calendar.txt", "a")
	calendar.write(newDate + "\n")
	calendar.close()

if messageFromUser == "2":
	calendar = open("calendar.txt", "r")
	print (calendar.read())

if messageFromUser == "3":
	print ("GoodBye!")