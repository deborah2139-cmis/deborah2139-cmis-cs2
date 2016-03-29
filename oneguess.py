import random

def numberChoice(minimumno, maximumno):
	return random.randint(minimumno, maximumno)

def guesserGuess(myChoice, playerGuess):
	if myChoice < playerGuess:
		dif = abs(playerGuess - myChoice)
		return "Your guess is over by {}".format(dif)
	if myChoice > playerGuess:
		dif = abs(myChoice - playerGuess)
		return "Your guess is under by {}".format(dif)

def output(myChoice, playerGuess, incorrect):
	if myChoice == playerGuess:
		print """The target was {}
Your guess was {}
That is correct! Are you a mind(computer) reader?!""".format(myChoice, playerGuess)
	else:
		print """The target was {}
Your guess was {}
{}""".format(myChoice, playerGuess, incorrect)

def main():
	minimumno = int(raw_input("What is the minimum number?: "))
	maximumno = int(raw_input("What is the maximum number?: "))
	print "I'm thinking of a number from {} to {}".format(minimumno, maximumno)
	playerGuess = int(raw_input("What do you think it is?: "))
	myChoice = int(numberChoice(minimumno, maximumno))
	incorrect = guesserGuess(myChoice,playerGuess)
	return output(myChoice, playerGuess,incorrect)

main()
