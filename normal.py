import math
import webbrowser
import scipy.stats as st
print ("""Legend for type
1 for less than <
2 for greater than >
3 for between
4 for outside
5 for finding x from z value
6 for equal to
7 Unusual data""")
sample = int(input("Do you wish to convert population tendencies to sample ones? Press 1 YES: "))
xOrZ = int(input("Would you like to enter values of 1. x or 2. z: "))
parts = int(input("How many parts: "))
print ("This is a normal distribution question with")
mean = float(input("\\\\Mean (\\mu)= "))
sd = float(input("\\\\Standard\\;Deviation (\\sigma)= "))

def z(x, mean, sd):
	return round((x - mean) / sd, 4)

def xi(z, mean, sd):
	return round(mean + (z * sd), 4)

def s(sd, n):
	return round(sd / math.sqrt(n), 4)

zscores = dict([(-3, 0.0013), (-2.5, 0.0062), (-2, 0.0228), (-1.75, 0.0401), (-1.5, 0.0668), (-1.25, 0.1056), (-1.2, 0.1151), (-1, 0.1587), (-0.9, 0.1841), (-0.8, 0.2119), (-0.75, 0.2266), (-0.7, 0.2420), (-0.6, 0.2743), (-0.5, 0.3085), (-0.4, 0.3446), (-0.3, 0.3821), (-0.25, 0.4013), (-0.2, 0.4207), (-0.1, 0.4602), (0.0, 0.5), (3, 0.9987), (2.5, 0.9938), (2, 0.9772), (1.75, 0.9599), (1.5, 0.9332), (1.25, 0.8944), (1.2, 0.8849), (1, 0.8413), (0.9, 0.8159), (0.8, 0.7881), (0.75, 0.7434), (0.7, 0.7580), (0.6, 0.7257), (0.5, 0.6915), (0.4, 0.6554), (0.3, 0.6179), (0.25, 0.5987), (0.2, 0.5793), (0.1, 0.5398)])
zinv = dict([(0.05, -1.645), (0.1, -1.282), (0.15, -1.036), (0.2, -0.8416), (0.25, -0.6745), (0.3, -0.525), (0.35, -0.385), (0.40, -0.253), (0.45, -0.1257), (0.5, 0), (0.95, 1.645), (0.9, 1.282), (0.85, 1.036), (0.8, 0.8416), (0.75, 0.6745), (0.7, 0.525), (0.65, 0.385), (0.6, 0.253), (0.55, 0.1257), (0.98, 2.054), (0.96, 1.751), (0.99, 2.326)])
sec = 97

if sample == 1:
	n = int(input("Sample size (n) = "))
	sd = s(sd, n)
	print ("Since we know that")
	print ("\\\\Sample \\; mean (\\bar{x}) = \\mu = " + str(mean))
	print ("\\\\Sample \\;standard\\;deviation(s) = \\frac{\\sigma}{\\sqrt{n}} = " + str(sd))
	print ("\\\\ z_{ score } = \\frac{x-\\bar{x}}{s}")
else: 
	print ("\\\\Since\\; we\\; know\\; that")
	print ("\\\\z_{ score } = \\frac{x-\\mu}{\\sigma}")

if xOrZ == 1:
	for i in range(parts):
		ty = int(input("Type of this part: "))

		if ty == 1:
			x1 = float(input(chr(sec) + ") " + "x = "))
			sec += 1 
			print ("P(x < " + str(x1) + ")=?")
			print(f"The z-score at x = {x1} is, ")
			print (f"z = \\frac{{{x1}-{mean}}}{{{sd}}}")
			z1 = z(x1, mean, sd)
			ans = st.norm.cdf(z1)
			print ("z = " + str(z1))
			print ("This implies that")
			print (f"P(x < {x1}) = P(z < {z1}) = \\textbf{{{ans}}}")
	
		if ty == 2:
			x1 = float(input(chr(sec) + ") " + "x = "))
			sec += 1 
			print ("P(x > " + str(x1) + ")=?")
			print(f"The z-score at x = {x1} is, ")
			print (f"z = \\frac{{{x1}-{mean}}}{{{sd}}}")
			z1 = z(x1, mean, sd)
			ans = round(1 - st.norm.cdf(z1), 4)
			print ("z = " + str(z1))
			print ("This implies that")
			print (f"P(x > {x1}) = P(z > {z1}) = 1 - {st.norm.cdf(z1)}")
			print (f"P(x > {x1}) = \\textbf{{{ans}}}")
	
		elif ty == 3:
			x1 = float(input(chr(sec) + ") " + "x1 = "))
			sec += 1 
			x2 = float(input("x2 = "))
			print ("P(" + str(x1) + " < x < " + str(x2) + ")=?")
			print(f"\\\\ The\\; z-score\\; at\\; x = {x1} is, ")
			print (f"\\\\ z = \\frac{{{x1}-{mean}}}{{{sd}}}")
			z1 = z(x1, mean, sd)
			print ("\\\\ z_1 = " + (str(z1)))
			print(f"\\\\ The\\; z-score\\; at\\; x = {x1} is, ")
			print (f"\\\\ z = \\frac{{{x2}-{mean}}}{{{sd}}}")
			z2 = z(x2, mean, sd)
			print ("\\\\ z_2 = " + str(z2))
			ans = round(st.norm.cdf(z2) - st.norm.cdf(z1), 4)
			print ("This implies that")
			print (f"P({x1} < x < {x2}) = P({z1} < z < {z2}) = P(Z < {z2}) - P(Z < {z1})")
			print (f"P({x1} < x < {x2}) = {st.norm.cdf(z2)} - {st.norm.cdf(z1)}")
			print (f"P({x1} < x < {x2}) = \\textbf{{{ans}}}")	
		elif ty == 4:
			x1 = float(input(chr(sec) + ") " + "x1 = "))
			sec += 1 
			x2 = float(input("x2 = "))
			print ("P(X < " + str(x1) + " or X > " + str(x2) + ")=?")
			print(f"\\\\ The\\; z-score\\; at\\; x = {x1} is, ")
			print (f"\\\\ z = \\frac{{{x1}-{mean}}}{{{sd}}}")
			z1 = z(x1, mean, sd)
			print ("\\\\ z_1 = " + (str(z1)))
			print(f"\\\\ The\\; z-score\\; at\\; x = {x1} is, ")
			print (f"\\\\ z = \\frac{{{x2}-{mean}}}{{{sd}}}")
			z2 = z(x2, mean, sd)
			print ("\\\\ z_2 = " + str(z2))
			ans = round(1 - zscores.get(z2, 0) + zscores.get(z1, 0), 4)
			print ("This implies that")
			print ("P(X < " + str(x1) + " or X > " + str(x2) + ") = P(z < " + str(z1) + " or z > " + str(z2) + ") = " +str(ans))

		elif ty == 5:
			pn = float(input("p = "))
			zn = st.norm.ppf(pn)
			xn = xi(zn, mean, sd)
			print (chr(sec) + ") Given in the question ")
			sec += 1
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

		elif ty ==7:
			print("Data beyond two standard deviations away from the mean i.e. data which have z-scores beyond -2 or 2 is known as unusual data.")
			print("So this data is not unusual value")

elif xOrZ == 2:
	for i in range(parts):

		ty = int(input("Type of this part: "))
		if ty == 1:
			z1 = float(input(chr(sec) + ") " + "z = "))
			sec += 1
			ans = zscores.get(z1, 0)
			print ("This implies that")
			print ("P(z < " + str(z1) + ") = " + str(ans))
	
		if ty == 2:
			z1 = float(input(chr(sec) + ") " + "z = "))
			sec += 1 
			ans = 1 - zscores.get(z1, 0)
			print ("This implies that")
			print ("P(z > " + str(z1) + ") = " + str(ans))
	
		elif ty == 3:
			z1 = float(input(chr(sec) + ") " + "z1 = "))
			sec += 1 
			z2 = float(input("z2 = "))
			ans = round(zscores.get(z2, 0) - zscores.get(z1, 0), 4)
			print ("This implies that")
			print ("P(" + str(z1) + " < z < " + str(z2) + ") = " + str(ans))
	
		elif ty == 4:
			z1 = float(input(chr(sec) + ") " + "z1 = "))
			sec += 1 
			z2 = float(input("z2 = "))
			ans = round(1 - zscores.get(z2, 0) + zscores.get(z1, 0), 4)
			print ("This implies that")
			print ("P(z < " + str(z1) + " or z > " + str(z2) + ") = " +str(ans))

		elif ty == 5:
			pn = float(input("p = "))
			zn = zinv.get(pn, 0)
			if zn == 0:
				webbrowser.open('http://measuringu.com/zcalcp/')
				zn = float(input("z = "))
			xn = xi(zn, mean, sd)
			print (chr(sec) + ") Given in the question ")
			sec += 1
			print ("P(X < x) = " + str(pn))
			print ("This implies that")
			print ("P(Z < " + str(zn) + ") = " + str(pn))
			print ("With the help of formula for z, we can say that")
			print ("\\\\ x = \mu + z\sigma")
			print ("\\\\\implies x = " + str(mean) + " + (" + str(zn) + ")" + str(sd)) 
			print ("x = " + str(xn))
		
		elif ty == 6:
			z = float(input(chr(sec) + ") z = "))
			sec += 1
			print ("P(X = " + str(z) + ") = ?")
			print ("For a continous the probability is the integration of probability density function in an given interval. Since if we give a particular point as an interval the integration comes out as 0.")
			print ("P(X = " + str(z) + ") = 0")
		
		elif ty ==7:
			print("Data beyond two standard deviations away from the mean i.e. data which have z-scores beyond -2 or 2 is known as unusual data.")
			print("So this data is not unusual value")

print ("PS: you have to refer z score table to find the final probabilities.")
print ("Please hit thumps up if the answer helped you")
