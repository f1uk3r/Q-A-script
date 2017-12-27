import math
import matplotlib.pyplot as plt


def a(x, y, xy, xx, n):
	return round(((y * xx) - (x * xy)) / ((n * xx) - (x*x)), 4)

def b(x, y, xy, xx, n):
	return round(((n * xy) - (x * y)) / ((n * xx) - (x*x)), 4)

def r(x, y, xy, xx, yy, n):
	return round(((n * xy) - (x * y)) / math.sqrt(((n * xx) - (x*x)) * ((n * yy) - (y*y))), 4)

def square(list):
	neo = []
	sq = 0
	for i in range(len(list)):
		neo.append(round(list[i] ** 2, 4))
	return neo

def mul(list1, list2):
	neo = []
	multi = 0
	for i in range(len(list1)):
		neo.append(round(list1[i] * list2[i], 4))
	return neo

def yforline(list, a, b):
	neo = []
	for i in range(len(list)):
		neo.append(round(a + b * list[i], 4))
	return neo

option = int(input("Choose 1. for regression\n 2. for correlation \n 3. Scatter plot \n 4. Line Graph: "))
xs = list(map(float, input("Input all the values of x: ").split()))
ys = list(map(float, input("Input all the values of y: ").split()))

xys = mul(xs, ys)
xxs = square(xs)
yys = square(ys)

print ("X         Y          XY          XX          YY")
for row in zip(xs, ys, xys, xxs, yys):
	print ('   |    '.join(str(v) for v in row))

n = len(xs)
x = round(sum(xs), 4)
y = round(sum(ys), 4)
xy = round(sum(xys), 4)
xx = round(sum(xxs), 4)
yy = round(sum(yys), 4)
sec = 97
a1 = a(x, y, xy, xx, n)
b1 = b(x, y, xy, xx, n)
r1 = r(x, y, xy, xx, yy, n)
somex = list(range(10))
somey = yforline(somex, a1, b1)
print ("\\\\ \sum X =" + str(x) + ", \sum Y =" + str(y) + "\\\\ \sum XY =" + str(xy) + ", \sum XX =" + str(xx) + ", \sum YY =" + str(yy))
if option == 1:
	print (chr(sec) + ")\\\\ \hat y = a + bx")
	sec += 1
	print ("\\\\ a = \\frac{\sum Y * \sum XX-\sum X*\sum XY}{n\sum X^2 -(\sum X)^2}")
	print ("\\\\ a = \\frac{" + str(y) + "*" + str(xx) + " - " + str(x) + "*" + str(xy) + "}{" + str(n) + "*" + str(xx) + " - " + str(x) + "*" + str(x) + "} \\approx " + str(a1))
	print ("\\\\ b = \\frac{n\sum XY -\sum X*\sum Y}{n\sum X^2 -(\sum X)^2}")
	print ("\\\\ b = \\frac{" + str(n) + "*" + str(xy) + " - " + str(x) + "*" + str(y) + "}{" + str(n) + "*" + str(xx) + " - " + str(x) + "*" + str(x) + "} \\approx " + str(b1))
	print ("\\\\ \hat y = " + str(a1) + "+" + str(b1) + "x")
	est = int(input("Press 0 if no estimation part, press number of parts if there are any estimation parts: "))
	for i in range(est):
		xhat = float(input(chr(sec) + ")x = "))
		sec += 1
		print ("\\\\ \hat y = " + str(a1) + "+" + str(b1) + "(" + str(xhat) + ")")
		yhat = round(a1 + (b1 * xhat), 4)
		print ("\\\\ \hat y = " + str(yhat))

elif option == 2:
	print (chr(sec) + ")\\\\ r = \\frac{n\sum XY -\sum X*\sum Y}{\sqrt{\left(n\sum X^2 -(\sum X)^2\\right)\left(n\sum Y^2 -(\sum Y)^2\\right)}}")
	sec += 1
	print ("\\\\ r = \\frac{" + str(n) + "*" + str(xy) + " - " + str(x) + "*" + str(y) + "}{ \sqrt{(" + str(n) + "*" + str(xx) + " - " + str(x) + "^2)(" + str(n) + "*" + str(yy) + " - " + str(y) + "^2)}} \\approx " + str(r1))

elif option == 3:
	print(chr(sec) + ")")
	sec += 1
	plt.scatter(xs, ys)
	plt.savefig('chegg.png', bbox_inches='tight')

elif option == 4:
	print(chr(sec) + ")")
	sec += 1
	plt.plot(somex, somey)
	plt.savefig('chegg2.png', bbox_inches='tight')

print ("Please hit thumps up if the answer helped you")
