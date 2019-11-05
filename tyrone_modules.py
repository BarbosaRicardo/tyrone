from datetime import date, datetime
#modules for Tyrone 

def payMe():
	print("What's the most you are willing to pay Tyrone for his advice?")
	
	try:
		myvalue = float(input("The more you pay, the better the answer! (minimum price $3): "))
	except ValueError as e:
			print("\nYou entered an invalid float that", e)
			
	if (myvalue < 3):
		return False 
	else:
		print("I guess $" + "{:,.2f}".format(myvalue) + " seems like a fair price...\n")
		return True 
"""
Checks if minumum payment is 975.46 
Returns boolean False 
"""

def getTarget(question):
	global target
	if question.lower().startswith("who"):
		target = "who"
	elif question.lower().startswith("what"):
		target = "what"
	elif question.lower().startswith("when"):
		target = "when"
	elif question.lower().startswith("where"):
		target = "where"
	elif question.lower().startswith("why"):
		target = "why"
	elif question.lower().startswith("how"):
		target = "how"
	else:
		target = "unknown"
	return target

"""
Checks type of question asked (who what when where why how)
Returns first word of question
"""
	
def createList(target):
	try:
		#creates an empty list 
		global display_list
		display_list = []
	
		filename = "tyrone.txt"

		with open(filename, "r") as file:
			for line in file:
				if line.lower().startswith(target) == True:
					display_list.append(line)
	except FileNotFoundError:
		print("File not found. Tyrone is not in.")
		exit()
		
	#creates variables for each line beginning with target
	#only one variable created when target is unknown	
	targetOne = display_list[0]
	if target != "unknown":
		targetTwo = display_list[1]
		targetThree = display_list[2]
	
	#eliminates target from each line 
	variableOne = targetOne[len(target)+1:]
	if target != "unknown":
		variableTwo = targetTwo[len(target)+1:]
		variableThree = targetThree[len(target)+1:]
	
	#stores edited line into list
	if target == "unknown":
		display_list = [variableOne]
	else:
		display_list = [variableOne, variableTwo, variableThree]
	
	return display_list

"""
Opens and reads file 
Appends lines from file to list 
Returns list 
"""	
				
def spinTheWheel(username, display_list):
	global answer
	numelements = len(display_list)
	if numelements < 0:
		remainder = 0
		answer = display_list[remainder]
		print(answer)
	else: 
		now = datetime.now()
		formatted_time = now.strftime("%S")		
		remainder = int(formatted_time) % numelements
		answer = display_list[remainder]
	
	while True:	
		enter = input("\nPress Enter to Activate the ARPANET Protocol")
		if enter != "":
			continue 
		break
	print("\nLoading....")
	
	print("\nAttention " + username +"! Tyrone declares:... " + answer + "\n")
	
	return answer 

"""
Selects list depending on the time 
returns answer
"""				
		
		
	