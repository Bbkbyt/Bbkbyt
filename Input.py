score = float(input("please enter your score here: "))
if((score>10) or (score<0)):
	print("invalid score")
elif(score<=5):
	print("you failed")
elif(score<10):
	print("you passed")
else:
	print("perfect score")