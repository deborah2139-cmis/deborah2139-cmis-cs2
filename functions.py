def add (a, b):
	return a + b

def sub (d, e):
	return d - e

def mul (g, h):
	return g * h

def div (j, k):
	return (j / k)

import math

def hours_from_seconds (a):
	return a / 3600
print hours_from_seconds (86400)

def circle_area (a):
	return math.pi * (a**2)
print circle_area (5)

def sphere_volume (a):
	return 1.33333333333 * math.pi * (a**3)
print sphere_volume (5)

def avg_volume (a, b):
	 return ((1.0/6 * math.pi * a**3) + (1.0/6 * math.pi * b**3)) /2
print avg_volume(10, 20)

def area (a, b, c):
	return math.sqrt (2.75*(2.75-a)*(2.75-b)*(2.75-c))
print area (1.0, 2.0, 2.5)

def right_align (word):
	return (80-len(word))*(" ")+word
print right_align ("Hello")

def center (word):
	return (40-len(word))*(" ")+word
print center ("Hello")

def msg_box (word):
    return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word) +4)*"-") + "+"
print msg_box ("Hello")

def msg_box (word):
    return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word) +4)*"-") + "+"
print msg_box ("I eat cats!")
a= add (3, 4)
print a
a= add (3,4)
print a
b= sub (5, 3)
print b
b= sub (5,3)
print b
c= mul (4, 4)
print c
c= mul (4, 4)
d= div (2.0, 3.0)
print d
d= div (2.0, 3.0)
print d 
e= hours_from_seconds (86400)
print e
e= hours_from_seconds (86400)
print e
f= circle_area (5)
print f
f= circle_area (5)
print f
g= sphere_volume (5)
print g
g = sphere_volume (5)
print g
h= avg_volume (10, 20)
print h
h= avg_volume (10, 20)
print h
i= area (1.0, 2.0, 2.5)
print i
i= area (1.0, 2.0, 2.5)
print i
j= right_align ("Hello")
print j
j= right_align ("Hello")
print j
k= center ("Hello")
print k
k= center ("Hello")
print k
l= msg_box ("Hello")
print l
l= msg_box ("Hello")
print l
m= msg_box ("I eat cats!")
print m
m= msg_box ("I eat cats!")
print m

