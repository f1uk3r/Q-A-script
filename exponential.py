import math

def lam(mean):
	return round(1 / mean, 4)

def prob(lamb, x):
	return round(1 - (math.exp(-1 * lamb * x)), 4)
print ("Choose 1. equals \n 2. for less than \n 3. for more than \n 4. for between \n 5. outside")
parts = int(input("How many parts: "))
MorL = int(input("Would you like to enter 1. mean or 2. lambda: "))

if MorL == 1:
	mean = float(input("\\\\Given,\\; mean(\\mu) = "))
	lamb = lam(mean)
	print ("\\\\Since,\\; \\lambda = \\frac{1}{\\mu} = " + str(lamb))
elif MorL == 2:
	lamb = float(input("\\\\Rate(\lambda) = "))
print ("For an exponential random variable X, the probability distribution function is")
print ("\\\\f(x) = \lambda e^{-\lambda x},\\; for x\\ge 0")
print ("\\\\So,\\; cummulative \\;distribution \\;function \\;of \\;X\\;is")
print ("\\\\F(x) = \int_0^x \lambda e^{-\lambda x}dx")
print ("\\\\F(x) = 1-e^{-\lambda x}")
print ("\\\\P(X < x) = F(x)")
sec = 97
for i in range(parts):
	ty = int(input("Mention type as legend: "))
	
	if ty == 1:
		x = float(input(chr(sec) + ") x = "))
		sec += 1
		print ("P(X = " + str(x) + ") = ?")
		print ("For a continous the probability is the integration of probability density function in an given interval. Since if we give a particular point as an interval the integration comes out as 0.")
		print ("P(X = " + str(x) + ") = 0")
	if ty == 2:
		x = float(input(chr(sec) +  ") x = "))
		sec += 1
		print ("P(X < " + str(x) + ") = ?")
		ans = prob(lamb, x)
		print ("P(X < " + str(x) + ") = 1-e^{-" + str(lamb)+ "*"  + str(x) + "}"  )
		print ("P(X < " + str(x) + ") = " + str(ans))
	if ty == 3:
		x = float(input(chr(sec) + ") x = "))
		sec += 1
		print ("P(X > " + str(x) + ") = ?")
		ans = round(1 - prob(lamb, x), 4)
		print ("P(X > " + str(x) + ") = 1-(1-e^{-" + str(lamb)+ "*" + str(x) + "})"  )
		print ("P(X > " + str(x) + ") = " + str(ans))
	if ty == 4:
		x1 = float(input("\\\\" + chr(sec) +  ") x_1 = "))
		sec += 1
		x2 = float(input("\\\\ x_2 = "))
		print ("P(" + str(x1) + " < X < " + str(x2) + " ) = ?")
		print ("P(" + str(x1) + " < X < " + str(x2) + " ) = P(X < " + str(x2) + ") - P(X < " + str(x1) + ")")
		print ("P(" + str(x1) + " < X < " + str(x2) + " ) = (1-e^{-" + str(lamb)+ "*" + str(x2) + "}) - (1-e^{-" + str(lamb)+ "*" + str(x1) + "})")
		ans = round(prob(lamb, x2) - prob(lamb, x1), 4)
		print ("P(" + str(x1) + " < X < " + str(x2) + " ) = " + str(ans))
	if ty == 5:
		x1 = float(input("\\\\" + chr(sec) +  ") x_1 = "))
		sec += 1
		x2 = float(input("\\\\ x_2 = "))
		print ("P(" + str(x1) + " > X or X > " + str(x2) + " ) = ?")
		print ("P(" + str(x1) + " > X or X > " + str(x2) + " ) = 1 - (P(X < " + str(x2) + ") - P(X < " + str(x1) + "))")
		print ("P(" + str(x1) + " > X or X > " + str(x2) + " ) =1 - ((1-e^{-" + str(lamb)+ "*" + str(x2) + "}) - (1-e^{-" + str(lamb)+ "*" + str(x1) + "}))")
		ans = round(1 - (prob(lamb, x2) - prob(lamb, x1)), 4)
		print ("P(" + str(x1) + " > X or X > " + str(x2) + " ) = " + str(ans))

print ("Please hit thumbs up if the answer helped you.")