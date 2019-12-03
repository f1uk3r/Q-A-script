from operator import mul
from functools import reduce
import math
from tabulate import tabulate
import matplotlib.pyplot as plt

def ncr(n, x):
	x1 = min(x, n-x)
	if x1 == 0: return 1
	numer = reduce(mul, range(n, n-x, -1))
	denom = reduce(mul, range(1, x+1))
	return numer / denom

def binom1(n, x, p, q):
	return ncr(n, x) * p**x * q**(n-x)

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
	return sum

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

def printBinomMarkup1(n, x, p, q):
	print(f"\\binom{{{n}}}{{{x}}} {p}^{{{x}}} {q}^{{{n}-{x}}}", end=" ")

def printBinomMarkup2(n, x, p, q):
	print(f"{round(ncr(n, x), 4)} ({p}^{{{x}}}) ({q}^{{{n-x}}})", end=" ")

def printBinomMarkup3(n, x, p, q):
	print(f"{round(ncr(n, x), 4)} ({round(p**x, 4)}) ({round(q**(n-x), 4)})", end=" ")

def printBinomMarkup4(n, x, p, q):
	print(f"\\textbf{{{round(ncr(n, x) * p**x * q**(n-x), 10)}}}", end=" ")

def printFullMarkup(n, x, p, q):
	print(f"\\\\ \\binom{{{n}}}{{{x}}} {p}^{{{x}}} {q}^{{{n}-{x}}} = {round(ncr(n, x), 4)} ({p}^{{{x}}}) ({q}^{{{n-x}}}) = {round(ncr(n, x), 4)} ({round(p**x, 4)}) ({round(q**(n-x), 4)}) = \\textbf{{{round(ncr(n, x) * p**x * q**(n-x), 4)}}}")

print ("""Legend for type
1 for =
2 and 3 for less than equal to and <
4 and 5 for \\ge and >
6 and 7 (between) for both inclusive and both exclusive
8 and 9 (between) for only second inclusive and only first inclusive
10 and 11 (outside) for both inclusive and both exclusive
12 and 13 (outside) for only second inclusive and only first inclusive
14 for mean, variance and standard deviation
15 Probability Distribution Table
16 Probability Histogram""")
parts = int(input("How many parts: "))
print ("This is a binomial distribution question with ")
n = int(input("n = "))
p = float(input("p = "))
q = round(1-p, 4)
print ("q = 1 - p = " + str(q))
print ("where")
print ("P(X = x) = \\binom{n}{x} p^x q^{n-x}")
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
		print (f"""\\\\ Mean (\\mu or E(X)) = np
\\\\ Mean (\\mu or E(X)) = {n}({p})
\\\\ Mean (\\mu or E(X)) = {mean}""")
		print (f"""\\\\ Variance (\\sigma^2 or V(x)) = npq
\\\\ Variance (\\sigma^2 or V(x)) = {n}({p})({q})
\\\\ Variance (\\sigma^2 or V(x)) = {variance}""")
		print (f"""\\\\ Standard\\; deviation (\\sigma or sd) = \\sqrt{{npq}}
\\\\ Standard\\; deviation (\\sigma or sd) = \\sqrt{{V(x)}}
\\\\ Standard\\; deviation (\\sigma or sd) = \\sqrt{variance}
\\\\ Standard\\; deviation (\\sigma or sd) = {sd}
\\\\ \\par\\noindent\\rule{{\\textwidth}}{{0.4pt}}""")

	elif ty == 1:
		x = int(input(chr(sec) + ") " + "x = "))
		ans = binom1(n, x, p, q)
		print(
			f"""\\\\ {chr(sec)}) P(X = {x}), n = {n}, p = {p}
\\\\ X \\sim Binomial(n = {n}, p = {p}, X = {x})
\\\\ P(X = {x}) = \\binom{{{n}}}{{{x}}} {p}^{{{x}}} {q}^{{{n}-{x}}}
\\\\ P(X = {x}) = {round(ncr(n, x), 4)} {p}^{{{x}}} {q}^{{{n-x}}} = {round(ncr(n, x), 4)} {round(p**x, 4)} {round(q**(n-x), 4)}
\\\\ P(X = {x}) = {ans} \\approx \\textbf{{{round(ans, 4)}}}"""
		)
		print(f"\\\\ \\par\\noindent\\rule{{\\textwidth}}{{0.4pt}}")
		sec += 1 

	elif ty == 2:
		x = int(input(chr(sec) + ") " + "x = "))
		ans = binom2(n, x, p, q)
		print(f"""\\\\ {chr(sec)})P(X \\le {x}), n = {n}, p = {p}
\\\\ P(X \\le {x}) = P(0 \\le X \\le {x})
\\\\ P(X \\le {x}) = P(X = 0)""", end=" ")
		for j in range(1, x+1):
			print(" + P(X = " + str(j) + ")", end=" ")
		print(" ")
		print(f"\\\\ P(X \\le {x}) = ", end=" ")
		for each_x in range(x):
			printBinomMarkup1(n, each_x, p, q)
			print("+", end=" ")
		printBinomMarkup1(n, x, p, q)
		print(" ")
		print(f"\\\\ P(X \\le {x}) = ", end=" ")
		for each_x in range(x):
			printBinomMarkup2(n, each_x, p, q)
			print("+", end=" ")
		printBinomMarkup2(n, x, p, q)
		print(" ")
		print(f"\\\\ P(X \\le {x}) = ", end=" ")
		for each_x in range(x):
			printBinomMarkup3(n, each_x, p, q)
			print("+", end=" ")
		printBinomMarkup3(n, x, p, q)
		print(" ")
		print(f"\\\\ P(X \\le {x}) = ", end=" ")
		for each_x in range(x):
			printBinomMarkup4(n, each_x, p, q)
			print("+", end=" ")
		printBinomMarkup4(n, x, p, q)
		print(" ")
		print("\\\\ P(X \\le " + str(x) + ") = " + str(ans))
		print(f"\\\\ \\par\\noindent\\rule{{\\textwidth}}{{0.4pt}}")
		sec += 1

	elif ty == 3:
		x = int(input(chr(sec) + ") " + "x = "))
		ans = binom3(n, x, p, q)
		print(f"""\\\\ {chr(sec)}) P(X < {x}), n = {n}, p = {p}
\\\\ P(X < {x}) = P(0 \\le X < {x})
\\\\ P(X < {x}) = P(X = 0)""", end=" ")
		for j in range(1, x):
			print(" + P(X = " + str(j) + ")", end=" ")
		print(" ")
		print(f"\\\\ P(X < {x}) = ", end=" ")
		for each_x in range(x-1):
			printBinomMarkup1(n, each_x, p, q)
			print("+", end=" ")
		printBinomMarkup1(n, x-1, p, q)
		print(" ")
		print(f"\\\\ P(X < {x}) = ", end=" ")
		for each_x in range(x-1):
			printBinomMarkup2(n, each_x, p, q)
			print("+", end=" ")
		printBinomMarkup2(n, x-1, p, q)
		print(" ")
		print(f"\\\\ P(X < {x}) = ", end=" ")
		for each_x in range(x-1):
			printBinomMarkup3(n, each_x, p, q)
			print("+", end=" ")
		printBinomMarkup3(n, x-1, p, q)
		print(" ")
		print(f"\\\\ P(X < {x}) = ", end=" ")
		for each_x in range(x-1):
			printBinomMarkup4(n, each_x, p, q)
			print("+", end=" ")
		printBinomMarkup4(n, x-1, p, q)
		print(" ")
		print("\\\\ P(X < " + str(x) + ") = \\textbf{" + str(ans) + "}")
		print(f"\\\\ \\par\\noindent\\rule{{\\textwidth}}{{0.4pt}}")
		sec += 1

	elif ty == 4:
		x = int(input(chr(sec) + ") " + "x = "))
		ans = binom4(n, x, p, q)
		print(f"""\\\\ {chr(sec)})P(X \\ge {x}), n = {n}, p = {p}
\\\\ P(X \\ge {x}) = P({x} \\le X \\le {n})""")
		if x > n / 2 :
			print ("\\\\ P(X \\ge " + str(x) + ") = ", end=" ")
			for j in range(x, n):
				print("P(X = " + str(j) + ") + ", end=" ")
			print("P(X = " + str(n) + ")")
			print(f"\\\\ P(X \\ge {x}) = ", end=" ")
			for each_x in range(x, n):
				printBinomMarkup1(n, each_x, p, q)
				print("+", end=" ")
			printBinomMarkup1(n, n, p, q)
			print(" ")
			print(f"\\\\ P(X \\ge {x}) = ", end=" ")
			for each_x in range(x, n):
				printBinomMarkup2(n, each_x, p, q)
				print("+", end=" ")
			printBinomMarkup2(n, n, p, q)
			print(" ")
			print(f"\\\\ P(X \\ge {x}) = ", end=" ")
			for each_x in range(x, n):
				printBinomMarkup3(n, each_x, p, q)
				print("+", end=" ")
			printBinomMarkup3(n, n, p, q)
			print(" ")
			print(f"\\\\ P(X \\ge {x}) = ", end=" ")
			for each_x in range(x, n):
				printBinomMarkup4(n, each_x, p, q)
				print("+", end=" ")
			printBinomMarkup4(n, n, p, q)
			print(" ")
		else:
			print ("\\\\ P(X \\ge " + str(x) + ") = 1 ", end=" ")
			for j in range(x-1):
				print("- P(X = " + str(j) + ") ", end=" ")
			print ("- P(X = " + str(x-1) + ")")
			print(f"\\\\ P(X \\ge {x}) = 1 - (", end=" ")
			for each_x in range(x-1):
				printBinomMarkup1(n, each_x, p, q)
				print("+", end=" ")
			printBinomMarkup1(n, x-1, p, q)
			print(")")
			print(f"\\\\ P(X \\ge {x}) = 1 - (", end=" ")
			for each_x in range(x-1):
				printBinomMarkup2(n, each_x, p, q)
				print("+", end=" ")
			printBinomMarkup2(n, x-1, p, q)
			print(")")
			print(f"\\\\ P(X \\ge {x}) = 1 - (", end=" ")
			for each_x in range(x-1):
				printBinomMarkup3(n, each_x, p, q)
				print("+", end=" ")
			printBinomMarkup3(n, x-1, p, q)
			print(")")
			print(f"\\\\ P(X \\ge {x}) = 1 - (", end=" ")
			for each_x in range(x-1):
				printBinomMarkup4(n, each_x, p, q)
				print("+", end=" ")
			printBinomMarkup4(n, x-1, p, q)
			print(")")
		print ("\\\\ P(X \\ge " + str(x) + ") = \\textbf{" + str(round(ans, 4)) + "}")
		print ("\\\\ P(X \\ge " + str(x) + ") = \\textbf{" + str(ans) + "}")
		print(f"\\\\ \\par\\noindent\\rule{{\\textwidth}}{{0.4pt}}")
		sec += 1 

	elif ty == 5:
		x = int(input(chr(sec) + ") " + "x = "))
		ans = round(binom5(n, x, p, q), 4)
		print(f"""\\\\ {chr(sec)})P(X > {x}), n = {n}, p = {p}
\\\\ P(X > {x}) = P({x} < X \\le {n})""")
		if x > n / 2 :
			print ("\\\\ P(X > " + str(x) + ") = ", end=" ")
			for j in range(x+1, n):
				print("P(X = " + str(j) + ") + ", end=" ")
			print("P(X = " + str(n) + ")")
			print(f"\\\\ P(X > {x}) = ", end=" ")
			for each_x in range(x+1, n):
				printBinomMarkup1(n, each_x, p, q)
				print("+", end=" ")
			printBinomMarkup1(n, n, p, q)
			print(" ")
			print(f"\\\\ P(X > {x}) = ", end=" ")
			for each_x in range(x+1, n):
				printBinomMarkup2(n, each_x, p, q)
				print("+", end=" ")
			printBinomMarkup2(n, n, p, q)
			print(" ")
			print(f"\\\\ P(X > {x}) = ", end=" ")
			for each_x in range(x+1, n):
				printBinomMarkup3(n, each_x, p, q)
				print("+", end=" ")
			printBinomMarkup3(n, n, p, q)
			print(" ")
			print(f"\\\\ P(X > {x}) = ", end=" ")
			for each_x in range(x+1, n):
				printBinomMarkup4(n, each_x, p, q)
				print("+", end=" ")
			printBinomMarkup4(n, n, p, q)
			print(" ")
		else:
			print ("\\\\ P(X > " + str(x) + ") = 1 ", end=" ")
			for j in range(x):
				print("- P(X = " + str(j) + ") ", end=" ")
			print ("- P(X = " + str(x) + ")")
			print(f"\\\\ P(X > {x}) = 1 - (", end=" ")
			for each_x in range(x):
				printBinomMarkup1(n, each_x, p, q)
				print("+", end=" ")
			printBinomMarkup1(n, x, p, q)
			print(")")
			print(f"\\\\ P(X > {x}) = 1 - (", end=" ")
			for each_x in range(x):
				printBinomMarkup2(n, each_x, p, q)
				print("+", end=" ")
			printBinomMarkup2(n, x, p, q)
			print(")")
			print(f"\\\\ P(X > {x}) = 1 - (", end=" ")
			for each_x in range(x):
				printBinomMarkup3(n, each_x, p, q)
				print("+", end=" ")
			printBinomMarkup3(n, x, p, q)
			print(")")
			print(f"\\\\ P(X > {x}) = 1 - (", end=" ")
			for each_x in range(x):
				printBinomMarkup4(n, each_x, p, q)
				print("+", end=" ")
			printBinomMarkup4(n, x, p, q)
			print(")")
		print ("\\\\ P(X > " + str(x) + ") = " + str(ans))
		print(f"\\\\ \\par\\noindent\\rule{{\\textwidth}}{{0.4pt}}")
		sec += 1 
	
	if ty == 6:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		x2 = int(input("x2 = "))
		ans = round(binom6(n, x1, x2, p, q), 4)
		print ("\\\\ P(" + str(x1) + "\\le X \\le" + str(x2) + ") = ", end=" ")
		for j in range(x1, x2):
			print("P(X = " + str(j) + ") + ", end=" ")
		print("P(X = " + str(x2) + ")")
		print(f"\\\\ P({x1} \\le X \\le {x2}) = ", end=" ")
		for each_x in range(x1, x2 + 1):
			printBinomMarkup1(n, each_x, p, q)
			print("+", end=" ")
		print(" ")
		print(f"\\\\ P({x1} \\le X \\le {x2}) = ", end=" ")
		for each_x in range(x1, x2 + 1):
			printBinomMarkup2(n, each_x, p, q)
			print("+", end=" ")
		print(" ")
		print(f"\\\\ P({x1} \\le X \\le {x2}) = ", end=" ")
		for each_x in range(x1, x2 + 1):
			printBinomMarkup3(n, each_x, p, q)
			print("+", end=" ")
		print(" ")
		print(f"\\\\ P({x1} \\le X \\le {x2}) = ", end=" ")
		for each_x in range(x1, x2 + 1):
			printBinomMarkup4(n, each_x, p, q)
			print("+", end=" ")
		print(" ")
		print ("\\\\ P(" + str(x1) + "\\le X \\le" + str(x2) + ") = " + str(ans))
		print(f"\\\\ \\par\\noindent\\rule{{\\textwidth}}{{0.4pt}}")
		sec += 1 

	if ty == 7:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		sec += 1 
		x2 = int(input("x2 = "))
		ans = round(binom7(n, x1, x2, p, q), 4)
		print ("P(" + str(x1) + "< X <" + str(x2) + ") = ", end=" ")
		for j in range(x1 + 1, x2 - 1):
			print("P(X = " + str(j) + ") + ", end=" ")
		print("P(X = " + str(x2 - 1) + ")")
		print(f"\\\\ P({x1} < X < {x2}) = ", end=" ")
		for each_x in range(x1+1, x2):
			printBinomMarkup1(n, each_x, p, q)
			print("+", end=" ")
		print(" ")
		print(f"\\\\ P({x1} < X < {x2}) = ", end=" ")
		for each_x in range(x1, x2 + 1):
			printBinomMarkup2(n, each_x, p, q)
			print("+", end=" ")
		print(" ")
		print(f"\\\\ P({x1} < X < {x2}) = ", end=" ")
		for each_x in range(x1, x2 + 1):
			printBinomMarkup3(n, each_x, p, q)
			print("+", end=" ")
		print(" ")
		print(f"\\\\ P({x1} < X < {x2}) = ", end=" ")
		for each_x in range(x1, x2 + 1):
			printBinomMarkup4(n, each_x, p, q)
			print("+", end=" ")
		print(" ")
		print ("P(" + str(x1) + "< X <" + str(x2) + ") = " + str(ans))
		print(f"\\\\ \\par\\noindent\\rule{{\\textwidth}}{{0.4pt}}")

	if ty == 8:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		sec += 1 
		x2 = int(input("x2 = "))
		ans = round(binom8(n, x1, x2, p, q), 4)
		print ("P(" + str(x1) + "< X \\le" + str(x2) + ") = ", end=" ")
		for j in range(x1 + 1, x2):
			print("P(X = " + str(j) + ") + ", end=" ")
		print("P(X = " + str(x2) + ")")
		print(f"\\\\ P({x1} < X \\le {x2}) = ", end=" ")
		for each_x in range(x1 + 1, x2 + 1):
			printBinomMarkup1(n, each_x, p, q)
			print("+", end=" ")
		print(" ")
		print(f"\\\\ P({x1} < X \\le {x2}) = ", end=" ")
		for each_x in range(x1 + 1, x2 + 1):
			printBinomMarkup2(n, each_x, p, q)
			print("+", end=" ")
		print(" ")
		print(f"\\\\ P({x1} < X \\le {x2}) = ", end=" ")
		for each_x in range(x1 + 1, x2 + 1):
			printBinomMarkup3(n, each_x, p, q)
			print("+", end=" ")
		print(" ")
		print(f"\\\\ P({x1} < X \\le {x2}) = ", end=" ")
		for each_x in range(x1 + 1, x2 + 1):
			printBinomMarkup4(n, each_x, p, q)
			print("+", end=" ")
		print(" ")
		print ("P(" + str(x1) + "< X \\le" + str(x2) + ") = " + str(ans))
		print(f"\\\\ \\par\\noindent\\rule{{\\textwidth}}{{0.4pt}}")

	if ty == 9:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		sec += 1 
		x2 = int(input("x2 = "))
		ans = round(binom9(n, x1, x2, p, q), 4)
		print ("P(" + str(x1) + "\\le X <" + str(x2) + ") = ", end=" ")
		for j in range(x1, x2 - 1):
			print("P(X = " + str(j) + ") + ", end=" ")
		print("P(X = " + str(x2 - 1) + ")")
		print(f"\\\\ P({x1} < X < {x2}) = ", end=" ")
		for each_x in range(x1, x2):
			printBinomMarkup1(n, each_x, p, q)
			print("+", end=" ")
		print(" ")
		print(f"\\\\ P({x1} < X < {x2}) = ", end=" ")
		for each_x in range(x1, x2):
			printBinomMarkup2(n, each_x, p, q)
			print("+", end=" ")
		print(" ")
		print(f"\\\\ P({x1} < X < {x2}) = ", end=" ")
		for each_x in range(x1, x2):
			printBinomMarkup3(n, each_x, p, q)
			print("+", end=" ")
		print(" ")
		print(f"\\\\ P({x1} < X < {x2}) = ", end=" ")
		for each_x in range(x1, x2):
			printBinomMarkup4(n, each_x, p, q)
			print("+", end=" ")
		print(" ")
		print ("P(" + str(x1) + "\\le X <" + str(x2) + ") = " + str(ans))
		print(f"\\\\ \\par\\noindent\\rule{{\\textwidth}}{{0.4pt}}")

	if ty == 10:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		sec += 1 
		x2 = int(input("x2 = "))
		ans = round(1 - binom7(n, x1, x2, p, q), 4)
		print ("P(" + str(x1) + "\\ge X or X \\ge" + str(x2) + ") = " + str(ans))
		print(f"\\\\ \\par\\noindent\\rule{{\\textwidth}}{{0.4pt}}")

	if ty == 11:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		sec += 1 
		x2 = int(input("x2 = "))
		ans = round(1 - binom6(n, x1, x2, p, q), 4)
		print ("P(" + str(x1) + "> X or X >" + str(x2) + ") = " + str(ans))
		print(f"\\\\ \\par\\noindent\\rule{{\\textwidth}}{{0.4pt}}")

	if ty == 12:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		sec += 1 
		x2 = int(input("x2 = "))
		ans = round(1 - binom9(n, x1, x2, p, q), 4)
		print ("P(" + str(x1) + "> X or X \\ge" + str(x2) + ") = " + str(ans))
		print(f"\\\\ \\par\\noindent\\rule{{\\textwidth}}{{0.4pt}}")

	if ty == 13:
		x1 = int(input(chr(sec) + ") " + "x1 = "))
		x2 = int(input("x2 = "))
		ans = round(1 - binom8(n, x1, x2, p, q), 4)
		print ("P(" + str(x1) + "\\ge X or X >" + str(x2) + ") = " + str(ans))
		print(f"\\\\ \\par\\noindent\\rule{{\\textwidth}}{{0.4pt}}")
		sec += 1 

	if ty == 15:
		xs = range(0, n+1)
		px, cpx = pdt(n, p, q)
		print (f"\\\\ {chr(sec)})\\; Since \\;we\\; know\\; that")
		print (f"\\\\ P(X = x) = \\binom{{n}}{{x}} p^x q^{{n-x}}")
		for each_x in range(n+1):
			printFullMarkup(n, each_x, p, q)
		header = ["X", "P(X = x)", "cumm P(X = x)"]
		table = zip(xs, px, cpx)
		print(tabulate((table), header, tablefmt="latex"))
		print(f"\\\\ \\par\\noindent\\rule{{\\textwidth}}{{0.4pt}}")
		sec += 1 

	if ty == 16:
		xs = range(0, n+1)
		px, cpx = pdt(n, p, q)
		plt.bar(xs, px)
		plt.xlabel("X")
		plt.ylabel("P(X=x)")
		plt.title("Histogram")
		plt.savefig('binom_hist.png', bbox_inches='tight')
		plt.close()


print ("Please hit thumps up if the answer helped you")	