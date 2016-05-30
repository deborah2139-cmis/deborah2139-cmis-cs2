#My script will let you make choices about what to buy. It will sometimes make you do some work like hiking unless you are lucky and you make a wise choice

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

def whathat(whattype):
	if whattype == "cowboyhat":
		return True
	else:
		return False

def moneyleft(dollars):
	if float(dollars) < 15 and not float(dollars) < 0:
		yourmoney = random.random() * 100
		return yourmoney

def jacket(number1, number2):
	return random.randint(number1, number2)

def thechosenone(mynumb, chosennumb):
	if mynumb < chosennumb and not mynumb == chosennumb:
		dif = abs(chosennumb - mynumb)
		return "Your number is over by {}".format(dif)
	if mynumb > chosennumb or not mynumb < chose:
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
	whattype = raw_input("Choose between a beanie and a cowboyhat: ")
	whathatt = whathat(whattype)
	print "Do you like the hat?: {}".format(whathatt)
	dollars = float(raw_input("Type a number less than 15 and more than 0! (Can be a decimal): "))
	themoney = moneyleft(dollars)
	print "You have ${} left!".format(dollars)
	number1 = int(raw_input("Type any number: "))
	number2 = int(raw_input("Type another number: "))
	print "I'm thinking of a number from {} to {}. If you guess the number right, you get 3 different jackets.".format(number1, number2)
	mynumb = int(jacket(number1, number2))
	chosennumb = int(raw_input("Take a guess!!: "))
	wrong = thechosenone(mynumb, chosennumb)
	return output(mynumb, chosennumb, wrong)

main()
