import math

def momentum1(m, v):
	return """The momentum of first ball:
{} * {} = {}""".format(m, v, P)

def momentum2(m2, v2):
	return m2 * v2

def output(m, v, P):
	return """
The momentum of first ball:
{} * {} = {}
""".format(m, v, P)
	return """
the momentum of second ball:
{} * {} = {}
""".format(m2, v2, P2)


def main():
	mass1 = raw_input("Mass of a ball: ")
	velocity1 = raw_input("Velocity of a ball: ")
	P = momentum1(m, v)
	mass2 = raw_input("Mass of second ball: ")
	velocity2 = raw_input("Velocity of second ball: ")
	P2 = momentum2(m2, v2)
	return output(m, v, P)
main()
