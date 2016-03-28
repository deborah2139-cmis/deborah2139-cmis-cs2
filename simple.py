import math

def momentum1(mass1, velocity1):
	return mass1 * velocity1

def momentum2(mass2, velocity2):
	return mass2 * velocity2

def output(mass1, velocity1, P1, mass2, velocity2, P2):
	print """
The momentum of first ball:
{} * {} = {}
The momentum of second ball:
{} * {} = {}
""".format(mass1, velocity1, P1, mass2, velocity2, P2)
	
def main():
	mass1 = int(raw_input("Mass of a ball: "))
	velocity1 = int(raw_input("Velocity of a ball: "))
	mass2 = int(raw_input("Mass of second ball: "))
	velocity2 = int(raw_input("Velocity of second ball: "))
	P1 = int(momentum1(mass1, velocity1))
	P2 = int(momentum2(mass2, velocity2))
	return output(mass1, velocity1, P1, mass2, velocity2, P2)

main()
