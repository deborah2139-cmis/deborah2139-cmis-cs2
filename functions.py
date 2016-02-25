import math

def add(a, b):
	return a + b
a = add(3, 4)
a2 = add(2, 5)
#Adds 3 and 4

def sub(d, e):
	return d - e
b = sub(5, 3)
b2 = sub(6, 4)
#Subtracts 5 and 3

def mul(g, h):
	return g * h
c= mul(4, 4)
c2 = mul(2, 8)
#Multiplies 4 and 4

def div(j, k):
	return (j / k)
d = div(2.0, 3.0)
d2 = div(3.0, 5.0)
#Divides 2.0 and 3.0

def hours_from_seconds(a):
	return a / 3600
print hours_from_seconds(86400)
h = hours_from_seconds(86400)
h2 = hours_from_seconds(42200)
#Finds the hours in 86400 seconds

def circle_area(a):
	return math.pi * (a**2)
print circle_area(5)
r= circle_area(5)
r2 = circle_area(7)
#It calculates the area of the circle

def sphere_volume(a):
	return 1.33333333333 * math.pi * (a**3)
print sphere_volume(5)
v = sphere_volume(5)
v2 = sphere_volume(7)
#It calculates the volume of the sphere

def avg_volume(a, b):
	 return ((1.0/6 * math.pi * a**3) + (1.0/6 * math.pi * b**3)) /2
print avg_volume(10, 20)
g = avg_volume(10, 20)
g2 = avg_volume(20, 30)
#It calculates the average volume

def area(a, b, c):
	return math.sqrt (2.75*(2.75-a)*(2.75-b)*(2.75-c))
print area(1.0, 2.0, 2.5)
e = area(1.0, 2.0, 2.5)
e2 = area(2.0, 3.0, 3.5)
#It calculates area of a triangle

def right_align(word):
	return (80-len(word))*(" ")+word
print right_align("Hello")
j= right_align("Hello")
j2 = right_align("Hello")
#It returns you "Hello" with 80 spaces in the front

def center(word):
	return (40-len(word))*(" ")+word
print center("Hello")
k= center("Hello")
k2 = center("Hello")
#It returns you "Hello", in the middle of 80 spaces

def msg_box(word):
    return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word) +4)*"-") + "+"
print msg_box("Hello")
m = msg_box("Hello")
m2 = msg_box("Hello")
#It returns you "Hello" in a box

def msg_box(word):
    return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word) +4)*"-") + "+"
print msg_box("I eat cats!")
n = msg_box("I eat cats!")
n2 = msg_box("I eat cats!")
#It returns you "I eat cats!" in a box

print msg_box(str(a))
print msg_box(str(a2))
print msg_box(str(b))
print msg_box(str(b2))
print msg_box(str(c))
print msg_box(str(c2))
print msg_box(str(d))
print msg_box(str(d2))
print msg_box(str(h))
print msg_box(str(h2))
print msg_box(str(r))
print msg_box(str(r2))
print msg_box(str(v))
print msg_box(str(v2))
print msg_box(str(g))
print msg_box(str(g2))
print msg_box(str(e))
print msg_box(str(e2))
print msg_box(j)
print msg_box(j2)
print msg_box(k)
print msg_box(k2)
print m
print m2
