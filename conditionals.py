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
		print "You only have 3 choices :( Bye"

def free(gender):
	if gender == "female":
		print "You get pants for males for free"
	elif gender == "male":
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

def jacket(number1, number2):
	return random.randint(number1, number2)

def main():
	choices = raw_input("Choose one of these: flip flops, tennis shoes, sandals: ")
	choice = shoes(choices)
	gender = raw_input("Are you a male or a female? Do not lie!: ")
	femormale = free(gender)
	kind = raw_input("Choose one of these long denim pants, short pants, skirts: ")
	undclothes = pants(kind)
	number1 = raw_input("Type any number that is not negative: ")
	number2 = raw_input("Type another number that is not negative; ")
	return jacket(number)
	numbjacket = jacket(number)

main()
