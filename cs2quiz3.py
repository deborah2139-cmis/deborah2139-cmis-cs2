#Section 1: Terminology
# 1) What is a recursive function?
# A recursive function is when the function keeps on calling itself infinitely. (Not if there is a base case)
#corr
#
# 2) What happens if there is no base case defined in a recursive function?
#Then the recursive function will keep on calling itself
#corr
#
# 3) What is the first thing to consider when designing a recursive function?
#You need to set a base case so you know when it will stop calling itself
#corr
#
# 4) How do we put data into a function call?
#Put in an argument
#corr
# 
# 5) How do we get data out of a function call?
#Base case
#wrong (return)
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 8			check
#a2 = 8			check
#a3 = -1		check

#b1 = 2			check
#b2 = 2			check
#b3 = 0

#c1 = -1
#c2 = 4			check
#c3 = 15

#d1 = 6			check
#d2 = 6
#d3 = 4			check


#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.


import math

def enter(number):
	n = raw_input("n: ")
	if n == "":
		return
	else:
		number += int(n)
		enter(number)

def main():
	enter(0)
main()
