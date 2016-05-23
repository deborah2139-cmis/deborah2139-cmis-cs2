def function1(x, n):
	if n <= 0:
		return x
	else:
		return 1 + function1(x, n - 1)

def function2(a, b):
	if a <= 0:
		return 1 + function2(a + 1, b ** a)
	else:
		return b

def function3(a, b):
	if b <=0:
		return a
	else:
		return a + b + function3(a, b - 1)

def function4(a, b, c):
	if a > b and a > c:
		return 1 + function4(b + 1 , c, a)
	elif b > a or b > c:
		return 1 - function4(b-1, c, a)
	else:
		return a+b+c

a = function1(2,6)
b = function1(6,2)
c= function1(-1,-1)

d = function2(2,2)
z = function2(0,0)
e = function2(-2,-2)

f = function3(-2,3)
g = function3(4,-2)
h = function3(5,5)

i = function4(1,2,3)
j = function4(3,2,1)
k = function4(1,3,2)

print a
print b
print c
print d
print z
print e
print f
print g
print h
print i
print j
print k
