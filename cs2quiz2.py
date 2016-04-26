#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#1a) 3 == 3
#2b) 3!=2
#3c) 3<7
#
#4 2) What does 'return' do?
# It spits out the result to the calling function.
#
#
#
#3) What are 2 ways indentation is important in python code?
#5a) The program will not work.
#6b) It shows when the code starts and ends. x
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#7problem1_a) -36
#8problem1_b) square root of 3
#9problem1_c) 0
#10problem1_d) -5
#
#11problem2_a) True
#12problem2_b) False
#13problem2_c) False
#14problem2_d) False x
#
#15problem3_a) 0.3
#16problem3_b) 0.5
#17problem3_c) 0.5
#18problem3_d) 0.5
#
#19problem4_a) 7
#20problem4_b) 2
#21problem4_c) 0.125
#22problem4_d) 2.5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

def userchoice(num1, num2, num3):
	if num1 > num2 and num1 > num3:
		return "The largest number was {}".format(no1)#num1
	if num2 > num1 and num2 > num3:
		return "The largest number was {}".format(no2)#num2
	if num3 > num1 and num3> num2:
		return "The largest number was {}".format(no3)#num3
	else:
		print "You didn't follow directions"

def main():
	print "Type in 3 different numbers (decimals are OK): "
	choice1 = float(raw_input("A: "))
	choice2 = float(raw_input("B: "))
	choice3 = float(raw_input("C: "))
	choice = float(userchoice(num1, num2, num3))

main()

#27- 30, 32
