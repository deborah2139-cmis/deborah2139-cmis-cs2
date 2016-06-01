import random
def game(compnumber, attempts):
	yourguess = int(raw_input ("Guess de numberrr!!!!!: "))
	if attempts == 0:
		print "You're reeaaally bad at this you know"
		return 0
	elif int(yourguess) > int(compnumber):
		print "That's too high!!!!!!!"
		game(compnumber, attempts - 1)
		return 0
	elif int(yourguess) < int(compnumber):
		print "That's too low!!!!!@!!!!"
		game(compnumber, attempts - 1)
		return 0
	elif compnumber == yourguess:
		print "Correctt"
		return 1

def turns(roundd, correct, attempts):
	compnumber = random.randint (0,100)
	if roundd == 0:
		print correct
	elif roundd != 0:
		computerthinks = ("I am thinking of a number between 0 and 100")
		print computerthinks
		thegame = game(compnumber, attempts)
		adding = correct + thegame
		print "You oonnlyy have {} rounds left".format(roundd - 1)
		turns(roundd - 1, adding, attempts)
def main(): 
	correct = 0
	attempts = 4
	roundd = 3
	turns(roundd, correct, attempts)
main ()
