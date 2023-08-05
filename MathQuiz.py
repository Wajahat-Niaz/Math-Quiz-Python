#Math Quiz Game
import random
maxNum = 10
minNum = 1

def quiz(num1,num2,operation,maxNum,minNum):
	if operation == 1:
		print("%d + %d = "%(num1,num2))
		inputQuiz = int(input())
		if inputQuiz == num1+num2:
			print("Correct!")
			randomize(maxNum,minNum)
		else:
			print("Wrong!")
			randomize(maxNum-10,minNum-5)
	elif operation == 2:
		print("%d - %d = "%(num1,num2))
		inputQuiz = int(input())
		if inputQuiz == num1-num2:
			print("Correct!")
			randomize(maxNum,minNum)
		else:
			print("Wrong!")
		randomize(maxNum-10,minNum-5)

def randomize(maxNum, minNum):
	minNum += 5
	maxNum += 10
	num1 = random.randint(minNum,maxNum)
	num2 = random.randint(minNum,maxNum)
	operation = random.randint(1,2)
	quiz(num1,num2,operation,maxNum,minNum)
randomize(maxNum-10,minNum-5)