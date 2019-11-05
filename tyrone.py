import tyrone_modules as tyrone
from datetime import date, datetime

#Prompt screen with name of program 
title = "* * Ask Tyrone * *"
title = title.rjust(40)
print(title)
msg = "The Problem With Considering Everything A College Professor Say’s"
msg = msg.rjust(44)
print(msg,"\u2122\n")

#Checks proper value data
while True:
	try:
		while tyrone.payMe() == False:
			print("\nGo Away!")
			exit()
	except UnboundLocalError:
			print("Please enter a numerical value\n")
			continue
	break

#Displays start to user
print("OK, let's get started...\n")

#Prompts user for their name 
while True:
	global username
	username = input("First, tell me your name: ")
	if username != "":
		break

#Prompts user for their question
while True:
	while True:
		global question 
		question = input("\nHello " + username + ", Tyrone is listening... ask away.... ")
		if question != "":
			break		

#Loops until user has no more questions

	#getTarget
	tyrone.getTarget(question)

	#creates list 
	tyrone.createList(tyrone.target)

	#spins wheel 
	tyrone.spinTheWheel(username, tyrone.display_list)
	
	another = input("Do you have another question? Y/N " )
	
	if another.lower() == "y":
		continue
	else:
		break
		
			
		
#returns conclusion with dates
now = datetime.now()
day_of_week = now.strftime("%A")
day_of_month = now.strftime("%d")
month = now.strftime("%B")
year = now.strftime("%Y")


if day_of_month == "1" or day_of_month == "21" or day_of_month == "31":
	print("\nOn this day, "+ day_of_week + ", the " + day_of_month +"st in the month of " + month + " in the year " + year + " Tyrone wants you to go away now!")
elif (day_of_month == "2" or day_of_month == "22"):
	print("\nOn this day, "+ day_of_week + ", the " + day_of_month +"nd in the month of " + month + " in the year " + year + " Tyrone wants you to go away now!")
elif day_of_month == "3" or day_of_month == "23":
	print("\nOn this day, "+ day_of_week + ", the " + day_of_month +"rd in the month of " + month + " in the year " + year + " Tyrone wants you to go away now!")
else:
	print("\nOn this day, "+ day_of_week + ", the " + day_of_month +"th in the month of " + month + " in the year " + year + " Tyrone wants you to go away now!")
exit()

if __name__ =="__main__":
	main()		