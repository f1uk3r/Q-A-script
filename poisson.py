import math
def prob(mean, x):
	return (math.exp(-mean) * (mean ** x)) / math.factorial(x)

print ("Legend for type \n 1 for = \n 2 and 3 for < and less than equal to \n 4 and 5 for \ge and > \n 6 and 7 for both inclusive and both exclusive \n 8 and 9 for only second inclusive and only first inclusive \n 10 for variance and standard deviation")
parts = int(input("How many parts: "))
MorL = int(input("Would you like to enter 1. mean or 2. lambda: "))
print ("This is a question of poisson distribution with")
if MorL == 1:
	mean = float(input("Mean (\mu) = "))
elif MorL == 2:
	lamb = float(input("Rate (\lambda) = "))
	t = float(input("time (t) = "))
	print ("Since we know that for poisson distribution")
	mean = round(lamb * t, 4)	
	print ("Mean (\mu) = \lambda t = " + str(lamb) + "*" + str(t) + " = " + str(mean))

print ("For a Poisson Distribution")
print ("P(X=x) = \\frac{e^{-\mu} \mu^{x}}{x!}")
sec = 97
for i in range(parts):
	ty = int(input("Mention type as in legend: "))
	if ty == 1:
		x = int(input(chr(sec) + ") " + "x = "))
		sec += 1 
		ans = round(prob(mean, x), 4)
		print ("P(X = " + str(x) + ") = \\frac{e^{-" + str(mean) + "} " + str(mean) + "^{" + str(x) + "}}{" + str(x) + "!}")
		print ("P(X = " + str(x) + ") = " + str(ans))
	if ty == 2:
		x = int(input(chr(sec) + ") " + "x = "))
		sec += 1 
		ans = 0
		for i in range(x):
			ans = ans + prob(mean, i)
		ans = round(ans, 4)
		print ("P(X < " + str(x) + ") = ", end=" ")
		for j in range(x-1):
			print("P(X = " + str(j) + ") + ", end=" ")
		print("P(X = " + str(x-1) + ")")
		print ("\\\\P(X < " + str(x) + ") = " + str(ans))
	if ty == 3:
		x = int(input(chr(sec) + ") " + "x = "))
		sec += 1 
		ans = 0
		for i in range(x+1):
			ans = ans + prob(mean, i)
		ans = round(ans, 4)
		print ("P(X \le " + str(x) + ") = ", end=" ")
		for j in range(x):
			print("P(X = " + str(j) + ") + ", end=" ")
		print("P(X = " + str(x) + ")")
		print ("\\\\ P(X \le " + str(x) + ") = " + str(ans))
	if ty == 4:
		x = int(input(chr(sec) + ") " + "x = "))
		sec += 1 
		ans = 1
		for i in range(x+1):
			ans = ans - prob(mean, i)
		ans = round(ans, 4)
		print ("\\\\P(X \ge " + str(x) + ") = 1 - P(X < " + str(x) + ")")
		print ("\\\\P(X \ge " + str(x) + ") = 1 ", end=" ")
		for j in range(x-1):
			print("- P(X = " + str(j) + ") ", end=" ")
		print ("- P(X = " + str(x-1) + ")")
		print ("\\\\P(X \ge " + str(x) + ") = " + str(ans))
	if ty == 5:
		x = int(input(chr(sec) + ") " + "x = "))
		sec += 1 
		ans = 1
		for i in range(x):
			ans = ans - prob(mean, i)
		ans = round(ans, 4)
		print ("P(X > " + str(x) + ") = 1 - P(X \le " + str(x) + ")")
		print ("P(X > " + str(x) + ") = 1 ", end=" ")
		for j in range(x):
			print("- P(X = " + str(j) + ") ", end=" ")
		print ("P(X = " + str(x) + ")")
		print ("\\\\P(X > " + str(x) + ") = " + str(ans))
	if ty == 6:
		x1 = int(input("x1 = "))
		x2 = int(input("x2 = "))
		ans = 0
		for i in range(x1, x2 + 1):
			ans = ans + prob(mean, i)
		ans = round(ans, 4)
		print ("\\\\P(" + str(x1) + "\le X \le" + str(x2) + ") = P(X\le " + str(x2) + ") - P(X\le " + str(x1) + ")")
		print ("\\\\P(" + str(x1) + "\le X \le" + str(x2) + ") = ", end=" ")
		for i in range(x1, x2):
			print ("P(X= " + str(i) + ") + ", end=" ")
		print ("P(X=" + str(x2) + ")")
		print("\\\\P(" + str(x1) + "\le X \le" + str(x2) + ") = " + str(ans))
	if ty == 7:
		x1 = int(input("x1 = "))
		x2 = int(input("x2 = "))
		ans = 0
		for i in range(x1+1, x2):
			ans = ans + prob(mean, i)
		ans = round(ans, 4)
		print ("\\\\P(" + str(x1) + "< X <" + str(x2) + ") = P(X< " + str(x2) + ") - P(X< " + str(x1) + ")")
		print ("\\\\P(" + str(x1) + "< X <" + str(x2) + ") = ", end=" ")
		for i in range(x1+1, x2-1):
			print ("P(X= " + str(i) + ") + ", end=" ")
		print ("P(X=" + str(x2-1) + ")")
		print("\\\\P(" + str(x1) + "< X <" + str(x2) + ") = " + str(ans))
	if ty == 8:
		x1 = int(input("x1 = "))
		x2 = int(input("x2 = "))
		ans = 0
		for i in range(x1+1, x2 + 1):
			ans = ans + prob(mean, i)
		ans = round(ans, 4)
		print ("\\\\P(" + str(x1) + "< X \le" + str(x2) + ") = P(X\le " + str(x2) + ") - P(X< " + str(x1) + ")")
		print ("\\\\P(" + str(x1) + "< X \le" + str(x2) + ") = ", end=" ")
		for i in range(x1+1, x2):
			print ("P(X= " + str(i) + ") + ", end=" ")
		print ("P(X=" + str(x2) + ")")
		print("\\\\P(" + str(x1) + "< X \le" + str(x2) + ") = " + str(ans))
	if ty == 9:
		x1 = int(input("x1 = "))
		x2 = int(input("x2 = "))
		ans = 0
		for i in range(x1, x2):
			ans = ans + prob(mean, i)
		ans = round(ans, 4)
		print ("\\\\P(" + str(x1) + "\le X <" + str(x2) + ") = P(X< " + str(x2) + ") - P(X< " + str(x1) + ")")
		print ("\\\\P(" + str(x1) + "\le X <" + str(x2) + ") = ", end=" ")
		for i in range(x1, x2-1):
			print ("P(X= " + str(i) + ") + ", end=" ")
		print ("P(X=" + str(x2-1) + ")")
		print("\\\\P(" + str(x1) + "\le X <" + str(x2) + ") = " + str(ans))
	if ty == 10:
		print("Since, we know that variance of poisson distribution is equal to the rate of the distribution")
		print("i.e. Variance = \lambda")
		print("or variance is equal to the mean of the distribution")
		print("This implies that")
		print("Variance = mean")
		print("Variance = " + str(mean))
		print("Also, Standard deviation is equal to the square root of the variance.")
		print("\\\\Standard\; deviation = variance^{\\frac{1}{2}}")
		print("\\\\standard\; deviation = " + round(math.sqrt(mean)), 4)
print ("Please hit thumps up if the answer helped you")
