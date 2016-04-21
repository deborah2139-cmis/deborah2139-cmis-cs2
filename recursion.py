def countdown(n):
	if n <= 0:
		print "Blastoff!"
	else:
		print n
		countdown(n-1)

def countup(n):
	if n>= 0:
		print "Blastoff!"
	else:
		print n


def main():
	countup(-10)
	countup(0)
	countup(10)

main()
