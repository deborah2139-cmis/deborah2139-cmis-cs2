def countFromZ(x, y):
	if x > y:
		while x >= y:
			print x
			x -= 1

	elif x < y:
		while x <= y:
			print y
			y -= 1


def addOdds(n):
	sum = 0
	if n > 0:
		while n > 0:
			if n & 2 == 1:
				sum += 1
			n -=1

	if n < 0:
		while n < 0:
			if n & 2 == 1:
				sum += 1
			n += 1
	return sum


def grid(w, h):
	out = ""
	x = 0
	while x < w:
		out += "." * w
		x += 1
	return out

def main():
	print grid(6, 2)
	countFromZ(7, 2)
	addOdds(19)

main()
