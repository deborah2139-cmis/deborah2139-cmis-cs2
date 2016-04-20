import math

def txt():
	print """This  program will ask you for 5 integer or float values. It will calculate the average of all valus from 0 inclusive to 10 exclusive. It will print out whether the resulting average is even or odd."""



def therange(n0, n1, n2, n3, n4):
	if n0 < 0 or n0 > 10:
		return "{} is out of range".format(n0)
	elif n1 < 0 or n1 > 10:
		return "{} is out of range".format(n1)
	elif n2 < 0 or n2 > 10:
		return "{} is out of range".format(n2)
	elif n3 < 0 or n3 > 10:
		return "{} is out of range".format(n3)
	elif n4 < 0 or n4 > 10:
		return "{} is out of range".format(n4)
	else:
		return "?"

def output(n0, n1, n2, n3, n4):
	return"""
def avg(n0, n1, n2, n3, n4):
	average = (n0 + n1 + n2 + n3 + n4)/5
	return average
""". format(n0, n1, n2, n3, n4)

def avg(n0, n1, n2, n3, n4):
	average = (n0 + n1 + n2 + n3 + n4)/5
	return average

def main():
	txt()
	n0 = raw_input("n0: ")
	n1 = raw_input("n1: ")
	n2 = raw_input("n2: ")
	n3 = raw_input("n3: ")
	n4 = raw_input("n4: ")

main()
