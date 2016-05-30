import math

def candies(candy):
	if candy < 0:
		print "Candy Firework!!!!!!!!"
	else:
		print candy
		candies(candy - 1)



def main():
	candy = raw_input("You're in a candy shop and we're counting down from 10 to 0... I promise, we're not suicide bombers :) Wait for it! Something sweet will happen! Type 10: ")
	candies(10)


main()
