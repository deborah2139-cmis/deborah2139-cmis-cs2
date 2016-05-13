#My script will let you make choices about what to buy. It will sometimes make you do some work like hiking unless you are lucky and you make a wise choice

#At least 1 must return a boolean value and be used as a part of the flow control.
#Use "not" "or" "and"
#Use random.random()

import random

def shoes(choices):
	if choices == "flip flops":
		print "You chose flip flops and got kicked out of the shop! [^,^]"

	elif choices == "tennis shoes":
		print "What a nice choice! You get to work in the farm for 7 days starting from tomorrow! xD"

	elif choices == "sandals":
		print"Get $400 :D"
	else:

		print "You only have 3 choices :( Bye :("

def free(gender):
	if gender == "female":
		print "You get pants for males for free"

	elif gender != "female":
		print "You get a super short mini skirt for free"

	else:
		print "You gotta be a male or a female... X( Bye"

def pants(kind):
	if kind == "long denim pants":
		print "I'm sorry, you need to hike in those :P"

	elif kind == "short pants":
		print "Wise choice :)"

	elif kind == "skirts":
		print "I'll just assume that you are a female ;)"

	else:
		print "NOOOO YOU ONLY HAVE THREE CHOICES! BYEE!"

#def whathat(whattype):
	#if whattype == True:
	#	msg = "You are very lucky!! You get $1000"
	#else:
	#	msg = "Wrong!! I'm sorry but there's no prize for a loser :("
	#return """
#{}""".format(msg)

def jacket(number1, number2):
	return random.randint(number1, number2)

def thechosenone(mynumb, chosennumb):
	if mynumb < chosennumb:
		dif = abs(chosennumb - mynumb)
		return "Your number is over by {}".format(dif)
	if mynumb > chosennumb:
		dif = abs(mynumb - chosennumb)
		return "Your number is under by {}".format(dif)

def output(mynumb, chosennumb, wrong):
	if mynumb == chosennumb:
		print """That was right!!! The number was {}! You get 3 jackets in return!! :D""".format(mynumb)
	elif chosennumb > mynumb:
		return """NOOO!!!! YOUR MAXIMUM NUMBER IS {}!!!""".format(chosennumb)
	else:
		print """Your guess, {}, was not right!! The number was {}. I'm sorry, but there's no second chance :( {}""".format(chosennumb, mynumb, wrong)

def main():
	choices = raw_input("Choose one of these: flip flops, tennis shoes, sandals: ")
	choice = shoes(choices)
	gender = raw_input("Are you a male or a female? Do not lie!: ")
	femormale = free(gender)
	kind = raw_input("Choose one of these long denim pants, short pants, skirts: ")
	undclothes = pants(kind)
	#whattype = raw_input("You need to choose one hat! YOU NEED TO CHOOSE THE RIGHT ONE: snapback, beanie, or cowboyhat: ")
	#whathatt = whathat(whattype)
	number1 = int(raw_input("Type any number: "))
	number2 = int(raw_input("Type another number: "))
	print "I'm thinking of a number from {} to {}. If you guess the number right, you get 3 different jackets.".format(number1, number2)
	chosennumb = int(raw_input("Take a guess!!: "))
	mynumb = int(jacket(number1, number2))
	wrong = thechosenone(mynumb, chosennumb)
	return output(mynumb, chosennumb, wrong)

main()
