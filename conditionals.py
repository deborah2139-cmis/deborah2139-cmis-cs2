#My script will let you make choices about what to buy.

def shoes(choices):
	if choices == "flip flops":
		print "You chose flip flops and got kicked out of the shop! [^,^]"
	elif choices == "tennis shoes":
		print "What a nice choice! You get to work in the farm for 4 days starting from tomorrow! xD"
	elif choices == "sandals":
		print"Get $400 :D"
	else:
		print "You only have 3 choices man :("

def free(gender):
	if gender == "female":
		print "I hope you're not lying cuz here, you get a super short mini skirt for free"
	elif gender == "male":
		print "I hope you're not lying cuz here, you get pants for males for free"
	else:
		print "You gotta be a male or a female... X("

def pants(kind):
	if kind == "long denim pants":
		print "I'm sorry man, you need to hike in those :P"
	elif kind == "short pants":
		print "Wise choice :)"
	elif kind == "skirts":
		print "I'll assume that you are a female ;)"
	else:
		print "NOOOO YOU ONLY HAVE THREE CHOICES!"

def main():
	choices = raw_input("Choose one of these flip flops, tennis shoes, sandals: ")
	choice = shoes(choices)
	gender = raw_input("Are you a male or a female?: ")
	femormale = free(gender)
	kind = raw_input("Choose one of these long denim pants, short pants, skirts:")
	undclothes = pants(kind)

main()
