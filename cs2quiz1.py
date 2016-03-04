#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
#It is used to put a value into a variable.
#
#correct
#
#2 3pts) Write a technical definition for 'function'
#Function is a named sequence of statements that performs a computation.
#
#correct
#
#3 1pt) What does the keyword "return" do?
#The keyword "return" spits out the output if you put in the input.
#
#correct
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: boolean - True, False
#	2:integer - 4, -192
#	3:floating point - 3.4, -2324.23
#	4:string - "Hellow"
#	5:tuple - ("Hello", 8320)
#   4
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#A function call is an expression containing a simple type name an a parenthesized argument list. A functioni definition specifies the name of new function and the sequence of statements that execute when the function is called.
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:input - returns what the user typed as a string
#	2:main - code will be executed even if the script was imported as a module with out this
#	3:output - information provided by a computer program
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

import math

def main():
	x = raw_input("Area of C1: ")
	y = raw_input("Area of C2: ")
	z = raw_input("Area of C3: ")
	z2 = raw_input("Circle Diameter")
	
main()

def diameter_of_C1(a):
	return sqrt(x/math.pi)
print diameter_of_C1(a)

def diameter_of_C2(b):
	return sqrt(y/math.pi)
print diameter_of_C2(b)

def diameter_of_C3(c):
	return sqrt(z/math.pi)
print diameter_of_C3(c)
