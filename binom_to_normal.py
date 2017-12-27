import math
def prob(mean, x):
	return (math.exp(-mean) * (mean ** x)) / math.factorial(x)
print ("Legend for type \n 1 for less than \n 2 for greater than \n 3 for between \n 4 for outside \n 5 for finding x from z value \n 6 for equal to =")
normalOrPoisson = int(input("Would you like to do a 1. Normal Approximation or 2. Poisson Approximation"))
parts = int(input("How many parts: "))

print ("This is a binomial distribution question with ")
n = int(input("n = "))
p = float(input("p = "))
q = 1-p
print ("q = 1 - p = " + str(q))
if normalOrPoisson == 1:

	print ("This binomial distribution can be approximated as Normal distribution since")
	print ("np > 5 and nq > 5")
	mean = round(n * p, 4)
	sd = round(math.sqrt(n * p * q), 4)
	print ("Since we know that")
	print ("\\\\Mean (\mu) = np = " + str(mean))
	print ("\\\\Standard\; deviation (\sigma) = \sqrt{npq} = " + str(sd))

	def z(x, mean, sd):
		return round((x - mean) / sd, 4)

	def xi(z, mean, sd):
		return round(mean + (z * sd), 4)
	zscores = dict([(-3, 0.0013), (-2.5, 0.0062), (-2, 0.0228), (-1.75, 0.0401), (-1.5, 0.0668), (-1.25, 0.1056), (-1.2, 0.1151), (-1, 0.1587), (-0.9, 0.1841), (-0.8, 0.2119), (-0.75, 0.2266), (-0.7, 0.2420), (-0.6, 0.2743), (-0.5, 0.3085), (-0.4, 0.3446), (-0.3, 0.3821), (-0.25, 0.4013), (-0.2, 0.4207), (0.1, 0.4602), (0.0, 0.5), (3, 0.9987), (2.5, 0.9938), (2, 0.9772), (1.75, 0.9599), (1.5, 0.9332), (1.25, 0.8944), (1.2, 0.8849), (1, 0.8413), (0.9, 0.8159), (0.8, 0.7881), (0.75, 0.7434), (0.7, 0.7580), (0.6, 0.7257), (0.5, 0.6915), (0.4, 0.6554), (0.3, 0.6179), (0.25, 0.5987), (0.2, 0.5793), (0.1, 0.5398)])

	print ("Also")
	print ("z_{ score } = \\frac{x-\mu}{\sigma}")

	sec = 97
	for i in range(parts):
		ty = int(input("Type of this part: "))
		if ty == 1:
			x1 = float(input(chr(sec) + ") " + "x = "))
			sec += 1 
			print ("P(x < " + str(x1) + ")=?")
			print ("z = \\frac {" + str(x1) + "-" +  str(mean) +  "}{" + str(sd) + "}")
			z1 = z(x1, mean, sd)
			ans = zscores.get(z1, 0)
			print ("z = " + str(z1))
			print ("This implies that")
			print ("P(x < " + str(x1) + ") = P(z < " + str(z1) + ") = " + str(ans))
	
		if ty == 2:
			x1 = float(input(chr(sec) + ") " + "x = "))
			sec += 1 
			print ("P(x > " + str(x1) + ")=?")
			print ("z = \\frac {" + str(x1) + "-" +  str(mean) +  "}{" + str(sd) + "}")
			z1 = z(x1, mean, sd)
			ans = 1 - zscores.get(z1, 0)
			print ("z = " + str(z1))
			print ("This implies that")
			print ("P(x > " + str(x1) + ") = P(z > " + str(z1) + ") = " + str(ans))

		elif ty == 4:
			x1 = float(input(chr(sec) + ") " + "x1 = "))
			sec += 1 
			x2 = float(input("x2 = "))
			print ("P(" + str(x1) + " < x < " + str(x2) + ")=?")
			print ("\\\\ z_1 = \\frac {" + str(x1) + "-" +  str(mean) +  "}{" + str(sd) + "}")
			z1 = z(x1, mean, sd)
			print ("\\\\ z_1 = " + (str(z1)))
			print ("\\\\ z_2 = \\frac {" + str(x2) + "-" +  str(mean) +  "}{" + str(sd) + "}")
			z2 = z(x2, mean, sd)
			ans = round(zscores.get(z2, 0) - zscores.get(z1, 0), 4)
			print ("\\\\ z_2 = " + str(z2))
			print ("This implies that")
			print ("P(" + str(x1) + " < x < " + str(x2) + ") = P(" + str(z1) + " < z < " + str(z2) + ") = " + str(ans))

		elif ty == 3:
			x1 = float(input(chr(sec) + ") " + "x1 = "))
			sec += 1 
			x2 = float(input("x2 = "))
			print ("P(X < " + str(x1) + " or X > " + str(x2) + ")=?")
			print ("\\\\ z_1 = \\frac {" + str(x1) + "-" +  str(mean) +  "}{" + str(sd) + "}")
			z1 = z(x1, mean, sd)
			print ("\\\\ z_1 = " + (str(z1)))
			print ("\\\\ z_2 = \\frac {" + str(x2) + "-" +  str(mean) +  "}{" + str(sd) + "}")
			z2 = z(x2, mean, sd)
			ans = round(1 - zscores.get(z2, 0) + zscores.get(z1, 0), 4)
			print ("\\\\ z_2 = " + str(z2))
			print ("This implies that")
			print ("P(X < " + str(x1) + " or X > " + str(x2) + ") = P(z < " + str(z1) + " or z > " + str(z2) + ") = " + str(ans))
	
		elif ty == 5:
			pn = float(input("p = "))
			zn = float(input("z = "))
			xn = xi(zn, mean, sd)
			print ("Given in the question ")
			print ("P(X < x) = " + str(pn))
			print ("This implies that")
			print ("P(Z < " + str(zn) + ") = " + str(pn))
			print ("With the help of formula for z, we can say that")
			print ("\\\\ x = \mu + z\sigma")
			print ("\\\\\implies x = " + str(mean) + " + (" + str(zn) + ")" + str(sd)) 
			print ("x = " + str(xn))
		elif ty == 6:
			x = float(input(chr(sec) + ") x = "))
			sec += 1
			print ("P(X = " + str(x) + ") = ?")
			print ("For a continous the probability is the integration of probability density function in an given interval. Since if we give a particular point as an interval the integration comes out as 0.")
			print ("P(X = " + str(x) + ") = 0")
	

elif normalOrPoisson == 2:
	print ("This binomial distribution can be approximated as Poisson Distribution since")
	print ("n > 20 and p < 0.05")
	mean = round(n * p, 4)
	print ("Since we know that")
	print ("\\\\Mean (\mu) = np = " + str(mean))
	print ("For a Poisson Distribution")
	print ("P(X=x) = \\frac{e^{-\mu} \mu^{x}}{x!}")
	sec = 97
	for i in range(parts):
		ty = int(input("Mention type as in legend: "))
		if ty == 6:
			x = int(input(chr(sec) + ") " + "x = "))
			sec += 1 
			ans = round(prob(mean, x), 4)
			print ("P(X = " + str(x) + ") = \\frac{e^{-" + str(mean) + "} " + str(mean) + "^{" + str(x) + "}}{" + str(x) + "!}")
			print ("P(X = " + str(x) + ") = " + str(ans))
		if ty == 1:
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
			print ("P(X = " + str(x-1) + ")")
			print ("P(X \ge " + str(x) + ") = " + str(ans))
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


print ("Please hit thumps up if the answer helped you")	
