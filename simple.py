import math

def mult(m, v):
	return m * v

def output(m, v, P):
	return """
The momentum of first ball:
{} * {} = {}
""". format(m, v, P)


def main():
	mass1 = raw_input("Mass of a ball: ")
	velocity1 = raw_input("Velocity of a ball: ")
	mass2 = raw_input("Mass of second ball: ")
	velocity2 = raw_input("Velocity of second ball: ")
	

main()
