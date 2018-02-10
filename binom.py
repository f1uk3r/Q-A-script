from operator import mul
from functools import reduce
import math
from tabulate import tabulate

print ("Legend for type \n 1 for = \n 2 and 3 for less than equal to and < \n 4 and 5 for \ge and > \n 6 and 7 (between) for both inclusive and both exclusive \n 8 and 9 (between) for only second inclusive and only first inclusive \n 10 and 11 (outside) for both inclusive and both exclusive \n 12 and 13 (outside) for only second inclusive and only first inclusive \n 14 for mean, variance and standard deviation \n 15 Probability Distribution Table")
parts = int(input("How many parts: "))
print ("This is a binomial distribution question with ")
n = int(input("n = "))
p = float(input("p = "))
q = round(1-p, 4)
print ("q = 1 - p = " + str(q))
print ("where")
print ("P(X = x) = \\binom{n}{x} p^x q^{n-x}")

def ncr(n, x):
	x1 = min(x, n-x)
	if x1 == 0: return 1
	numer = reduce(mul, range(n, n-x, -1))
	denom = reduce(mul, range(1, x+1))
	return numer / denom

def binom1(n, x, p, q):
	return round(ncr(n, x) * p**x * q**(n-x), 4)

def binom2(n, x, p, q):
	sum = 0
	while x > -1:
		sum += binom1(n, x, p, q)
		x -= 1
	return round(sum, 4)

def binom3(n, x, p, q):
	sum = 0
	x -= 1
	while x > -1:
		sum += binom1(n, x, p, q)
		x -= 1
	return round(sum, 4)

def binom4(n, x, p, q):
	sum = 0
	while x < n+1:
		sum += binom1(n, x, p, q)
		x += 1
	return round(sum, 4)

def binom5(n, x, p, q):
	sum = 0
	x += 1
	while x < n+1:
		sum += binom1(n, x, p, q)
		x += 1
	return round(sum, 4)

def binom6(n, x1, x2, p, q):
	sum = 0
	while x1 < x2 + 1:
		sum += binom1(n, x1, p, q)
		x1 += 1
	return round(sum, 4)

def binom7(n, x1, x2, p, q):
	sum = 0
	x1 += 1
	while x1 < x2:
		sum += binom1(n, x1, p, q)
		x1 += 1
	return round(sum, 4)

def binom8(n, x1, x2, p, q):
	sum = 0
	x1 += 1
	while x1 < x2 + 1:
		sum += binom1(n, x1, p, q)
		x1 += 1
	return round(sum, 4)

def binom9(n, x1, x2, p, q):
	sum = 0
	while x1 < x2:
		sum += binom1(n, x1, p, q)
		x1 += 1
	return round(sum, 4)

def pdt(n, p, q):
	neo = []
	neo2 = []
	sum = 0
	for i in range(0, n+1):
		neo.append(round(binom1(n, i, p, q), 4))
		sum += round(binom1(n, i, p, q), 4)
		neo2.append(sum)
	return neo, neo2

sec = 97
#if __name__ = __main__:
for i in range(parts):
	ty = int(input("Type of x: "))

	if ty == 14:
		mean = round(n * p, 4)
		variance = round(n * p * q, 4)
		sd = round(math.sqrt(n * p * q), 4)
		print (chr(sec) + ") Since we know that")
		sec += 1
		print ("\\\\Mean (\mu) = np = " + str(mean))
		print ("\\\\Variance (\sigma^2) = npq = " + str(variance))
		print ("\\\\Standard\; deviation (\sigma) = \sqrt{npq} = " + str(sd))

	elif ty == 1:
		x = int(input(chr(sec) + ") " + "x = "))
		sec += 1 
		ans = round(binom1(n, x, p, q), 4)
		print ("P(X = " + str(x) + ") = \\binom{" + str(n) + "}{" + str(x) + "} " + str(p) + "^{" + str(x) + "} "+ str(q) + "^{" + str(n) + "-" + str(x) + "}")
		print ("P(X = " + str(x) + ") = " + str(ans))

	elif ty == 2:
		x = int(input(chr(sec) + ") " + "x = "))
		sec += 1 
		ans = round(binom2(n, x, p, q), 4)
		print ("P(X \le " + str(x) + ") = ", end=" ")
		for j in range(x):
			print("P(X = " + str(j) + ") + ", end=" ")
		print("P(X = " + str(x) + ")")
		print ("P(X \le " + str(x) + ") = " + str(ans))

	elif ty == 3:
		x = int(input(chr(sec) + ") " + "x = "))
		sec += 1 
		ans = round(binom3(n, x, p, q), 4)
		print ("P(X < " + str(x) + ") = ", end=" ")
		for j in range(x-1):
			print("P(X = " + str(j) + ") + ", end=" ")
		print("P(X = " + str(x-1) + ")")
		print ("P(X < " + str(x) + ") = " + str(ans))

	elif ty == 4:
		x = int(input(chr(sec) + ") " + "x = "))
		sec += 1 
		ans = round(binom4(n, x, p, q), 4)
		if x > n / 2 :
			print ("P(X \ge " + str(x) + ") = ", end=" ")
			for j in range(x, n):
				print("P(X = " + str(j) + ") + ", end=" ")
			print("P(X = " + str(n) + ")")
		else:
			print ("\\\\P(X \ge " + str(x) + ") = 1 ", end=" ")
			for j in range(x-1):
				print("- P(X = " + str(j) + ") ", end=" ")
			print ("P(X = " + str(x-1) + ")")
		print ("P(X \ge " + str(x) + ") = " + str(ans))

	elif ty == 5:
		x = int(input(chr(sec) + ") " + "x = "))
		sec += 1 
		ans = round(binom5(n, x, p, q), 4)
		if x > n / 2 :
			print ("P(X > " + str(x) + ") = ", end=" ")
			for j in range(x+1, n):
				print("P(X = " + str(j) + ") + ", end=" ")
			print("P(X = " + str(n) + ")")
		else:
			print ("\\\\P(X > " + str(x) + ") = 1 ", end=" ")
			for j in range(x):
				print("- P(X = " + str(j) + ") ", end=" ")
			print ("P(X = " + str(x) + ")")
		print ("P(X > " + str(x) + ") = " + str(ans))
	
	if ty == 6:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		sec += 1 
		x2 = int(input("x2 = "))
		ans = round(binom6(n, x1, x2, p, q), 4)
		print ("P(" + str(x1) + "\le X \le" + str(x2) + ") = ", end=" ")
		for j in range(x1, x2):
			print("P(X = " + str(j) + ") + ", end=" ")
		print("P(X = " + str(x2) + ")")
		print ("P(" + str(x1) + "\le X \le" + str(x2) + ") = " + str(ans))

	if ty == 7:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		sec += 1 
		x2 = int(input("x2 = "))
		ans = round(binom7(n, x1, x2, p, q), 4)
		print ("P(" + str(x1) + "< X <" + str(x2) + ") = ", end=" ")
		for j in range(x1 + 1, x2 - 1):
			print("P(X = " + str(j) + ") + ", end=" ")
		print("P(X = " + str(x2 - 1) + ")")
		print ("P(" + str(x1) + "< X <" + str(x2) + ") = " + str(ans))

	if ty == 8:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		sec += 1 
		x2 = int(input("x2 = "))
		ans = round(binom8(n, x1, x2, p, q), 4)
		print ("P(" + str(x1) + "< X \le" + str(x2) + ") = ", end=" ")
		for j in range(x1 + 1, x2):
			print("P(X = " + str(j) + ") + ", end=" ")
		print("P(X = " + str(x2) + ")")
		print ("P(" + str(x1) + "< X \le" + str(x2) + ") = " + str(ans))

	if ty == 9:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		sec += 1 
		x2 = int(input("x2 = "))
		ans = round(binom9(n, x1, x2, p, q), 4)
		print ("P(" + str(x1) + "\le X <" + str(x2) + ") = ", end=" ")
		for j in range(x1, x2 - 1):
			print("P(X = " + str(j) + ") + ", end=" ")
		print("P(X = " + str(x2 - 1) + ")")
		print ("P(" + str(x1) + "\le X <" + str(x2) + ") = " + str(ans))

	if ty == 10:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		sec += 1 
		x2 = int(input("x2 = "))
		ans = round(1 - binom7(n, x1, x2, p, q), 4)
		print ("P(" + str(x1) + "\ge X or X \ge" + str(x2) + ") = " + str(ans))

	if ty == 11:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		sec += 1 
		x2 = int(input("x2 = "))
		ans = round(1 - binom6(n, x1, x2, p, q), 4)
		print ("P(" + str(x1) + "> X or X >" + str(x2) + ") = " + str(ans))

	if ty == 12:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		sec += 1 
		x2 = int(input("x2 = "))
		ans = round(1 - binom9(n, x1, x2, p, q), 4)
		print ("P(" + str(x1) + "> X or X \ge" + str(x2) + ") = " + str(ans))

	if ty == 13:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		sec += 1 
		x2 = int(input("x2 = "))
		ans = round(1 - binom8(n, x1, x2, p, q), 4)
		print ("P(" + str(x1) + "\ge X or X >" + str(x2) + ") = " + str(ans))
	if ty == 15:
		xs = range(0, n+1)
		px, cpx = pdt(n, p, q)
		header = ["X", "p(x)", "cumm P(x)"]
		table = zip(xs, px, cpx)
		print(tabulate((table), header, tablefmt="latex"))

print ("Please hit thumps up if the answer helped you")	