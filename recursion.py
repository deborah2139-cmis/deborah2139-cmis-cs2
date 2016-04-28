import numpy

def countup(n):
	if n >= 11:
		print "Blastoff!"
	else:
		print n
		countup(n+1)
	pass

def countdown(n):
	if n <= 0:
		print "Blastoff!"
	else:
		print n
		countdown(n-1)
	pass

def countup_from_to(start, stop):
	if start >= stop:
		print "Blastoff!"
	else:
		print start
		countup(start+1)
	pass

def countdown_from_to(start, stop):
	if start <= stop:
		print "Blastoff!"
	else:
		print start
		countdown(start-1)
	pass

def adder(continueadding):
	n = float(raw_input("n: "))
	if n == "":
		print "The sum is {}".format(continueadding)
	else n == 


	adder()


def main():
	adder()
	countup(1)
	countdown(10)
	countup_from_to(20, 34)
	countdown_from_to(30, 12)
	

main()
