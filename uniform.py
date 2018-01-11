# python 3
# uniform.py - solves probability for uniform distribution

import math
def findP(alp, bet, x):
	return round((x-alp) / (bet-alp), 4)
parts = int(input("How many parts are there for these questions: "))
print("This is a uniform distribution with")
a = int(input("\\\\ \\alpha = "))
b = int(input("\\\\ \\beta = "))
print("Since we know that")
print("Probability density function of a uniform distribution is")
print("f(x) = \\frac{1}{\\beta - \\alpha}, \\alpha \le x \le \\beta")
print("This implies that")
print("Cummulative density function of a uniform distribution is")
print("F(x) = \\frac{x_1 - \\alpha}{\\beta - \\alpha}")
sec = 97
for i in range(parts):
	opt = int(input("Enter a number according to legend: "))
	if opt == 1:
		print(chr(sec) + ") Pr(X<x) = F(x)")
		sec += 1
		x = int(input("Where x = "))
		if x <= a:
			print("Pr(X<" + str(x) + ") = 0")
		elif x >= b:
			print("Pr(X<" + str(x) + ") = 1")
		else:
			ans = findP(a, b, x)
			print("Pr(X<" + str(x) + ") = \\frac{" + str(x) + "-" + str(a) + "}{" + str(b) + "-" + str(a) + "}")
			print("Pr(X<" + str(x) + ") = " + str(ans))
	elif opt == 2:
		print(chr(sec) + ") Pr(X>x) = 1- F(x)")
		sec += 1
		x = int(input("Where x = "))
		if x <= a:
			print("Pr(X>" + str(x) + ") = 1")
		elif x >= b:
			print("Pr(X>" + str(x) + ") = 0")
		else:
			ans = round(1 - findP(a, b, x), 4)
			print("Pr(X>" + str(x) + ") = \\frac{" + str(b) + "-" + str(x) + "}{" + str(b) + "-" + str(a) + "}")
			print("Pr(X>" + str(x) + ") = " + str(ans))
	elif opt == 3:
		print(chr(sec) + ") Pr(x1<X<x2) = F(x2) - F(x1)")
		sec += 1
		x1 = int(input("Where x1 = "))
		x2 = int(input("x2 = "))
		if (x1 <= a and x2 <= a) or (x1 >= b and x2 >= b):
			print("Since, both x's doesn't lie in the interval")
			print("Pr(" + str(x1) + "<X<" + str(x2) + ") = 0")
		elif x1 <= a and x2 >= b :
			print("Pr(" + str(x1) + "<X<" + str(x2) + ") = F(\\beta) - F(\\alpha)")
			print("Pr(" + str(x1) + "<X<" + str(x2) + ") = \\frac{" + str(b) + "-" + str(a) + "}{" + str(b) + "-" + str(a) + "}")
			print("Pr(" + str(x1) + "<X<" + str(x2) + ") = 1")
		elif x1 <= a:
			ans = findP(a, b, x2)
			print("Pr(" + str(x1) + "<X<" + str(x2) + ") = F(x2) - F(\\alpha)")
			print("Pr(" + str(x1) + "<X<" + str(x2) + ") = \\frac{" + str(x2) + "-" + str(a) + "}{" + str(b) + "-" + str(a) + "}")
			print("Pr(" + str(x1) + "<X<" + str(x2) + ") = " + str(ans))
		elif x2 >= b:
			ans = round(1 - findP(a, b, x1), 4)
			print("Pr(" + str(x1) + "<X<" + str(x2) + ") = F(\\beta) - F(x1)")
			print("Pr(" + str(x1) + "<X<" + str(x2) + ") = \\frac{" + str(b) + "-" + str(x1) + "}{" + str(b) + "-" + str(a) + "}")
			print("Pr(" + str(x1) + "<X<" + str(x2) + ") = " + str(ans))
		else:
			ans = round(findP(a, b, x2) - findP(a, b, x1), 4)
			print("Pr(" + str(x1) + "<X<" + str(x2) + ") = \\frac{" + str(x2) + "-" + str(x1) + "}{" + str(b) + "-" + str(a) + "}")
			print("Pr(" + str(x1) + "<X<" + str(x2) + ") = " + str(ans))
	elif opt == 4:
		print(chr(sec) + ")Since we also know that")
		sec += 1
		print("Mean of a uniform distribution is the average of its interval i.e.")
		print("\\\\Mean = \\frac{\\alpha + \\beta}{2}" )
		print("\\\\Mean = \\frac{" + str(a) + "+" + str(b) + "}{2}")
		print("Mean = " + str(round((a + b )/ 2, 4)))
	elif opt == 5:
		print(chr(sec) + ") Also")
		sec += 1
		print("Variance = \\frac{(\\beta-\\alpha)^2}{12}")
		print("Variance = \\frac{(" + str(b) + "-" + str(a) + ")^2}{12}")
		variance = round(((b-a) ** 2) / 12, 4)
		print("Variance = " + str(variance))
		print("Standard/;Deviation = \sqrt{Variance}")
		print("Standard Deviation = " + str(round(math.sqrt(variance), 4)))