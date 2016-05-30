import numpy

def countup(n):
	if n >= 11:
		print "Blastoff!"
	else:
		print n
		countup(n+1)

def countdown(n):
	if n <= 0:
		print "Blastoff!"
	else:
		print n
		countdown(n-1)

def countup_from_to(start, stop):
	if start >= stop:
		print "Blastoff!"
	else:
		print start
		countup(start+1)

def countdown_from_to(start, stop):
	if start <= stop:
		print "Blastoff!"
	else:
		print start
		countdown(start-1)

def adder(total):
	print "Running total: {}".format(total)
	n = raw_input("n: ")
	if n == "":
		print "Byee!!"
	else:
		total += int(n)
		adder(total)

def biggest(big):
	n = raw_input("Number: ")
	if n == "":
		return big
	else:
		n = float(n)
		if n > big:
			big = n
		return biggest(big)

def smallest(small):
	n = raw_input("Number: ")
	if n == "":
		return small
	else:
		n = float(n)
		if n < small:
			small = n
		return smallest(small)

#def pow(x, n):
#	if n == 0:
#		return 1
#	else:
#		return x * pow(x, n-1)

def main():
	adder(0)
	print biggest(-float('inf'))
	print smallest(float('inf'))
	countup(1)
	countdown(10)
	countup_from_to(20, 34)
	countdown_from_to(30, 12)
	

main()
