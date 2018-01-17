import webbrowser
import math

def ll(n, sd, chi1):
	return round(((n-1) * (sd ** 2) /(chi1 ** 2)), 4)

def ul(n, sd, chi2):
	return round(((n-1) * (sd ** 2) /(chi2 ** 2)), 4)
def limit2(sd1, sd2, F1):
	return round(((sd1 ** 2)/(sd2 ** 2)) * F1, 4)

option = int(input("Choose 1 to find C.I. of variance, 2 for finding C.I. of ratio of the variances: "))

if option == 1:
	n = int(input("Sample size (n) = "))
	sd = float(input("Standard deviation (s) = "))
	ci = int(input("Confidence interval(in %) = "))
	print ("We have to find confidence interval for variance of the sample")
	webbrowser.open('https://www.danielsoper.com/statcalc/calculator.aspx?id=12')
	chi1 = float(input("\\\\\chi_{\\alpha/2, n-1}^2 = "))
	chi2 = float(input("\\\\\chi_{1-\\alpha/2, n-1}^2 = "))
	print ("Since we know that")
	print ("\\\\Confidence\; interval = \\frac{(n-1)S^2}{\chi_{\\alpha/2, n-1}^2}, \\frac{(n-1)S^2}{\chi_{1-\\alpha/2, n-1}^2}")
	lol = ll(n, sd, chi1)
	upl = ul(n, sd, chi2)
	print ("\\\\Required confidence interval = \left(\\frac{(" + str(n) + "-1)" + str(sd) + "^2}{" + str(chi1) + "}, \\frac{(" + str(n) + "-1)" + str(sd) + "^2}{" + str(chi2) + "}\\right)")
	print ("Required confidence interval = (" + str(lol) + ", " + str(upl) + ")")
else:
	n1 = int(input("Sample size1 (n1) = "))
	sd1 = float(input("Standard deviation1 (s1) = "))
	n2 = int(input("Sample size2 (n2) = "))
	sd2 = float(input("Standard deviation2 (s2) = "))
	ci = int(input("Confidence interval(in %) = "))
	print ("We have to find confidence interval for the ration of variances of two normal distribution")
	webbrowser.open('https://www.danielsoper.com/statcalc/calculator.aspx?id=4')
	F1 = float(input("\\\\F_{1-\\alpha/2, n_1-1, n_2-1}^2 = "))
	F2 = float(input("\\\\F_{\\alpha/2, n_1-1, n_2-1}^2 = "))
	print ("Since we know that")
	print ("\\\\Confidence\; interval = \\frac{S_1^2}{S_2^2}F_{1-\\alpha/2, n_1-1, n_2-1}, \\frac{S_1^2}{S_2^2}F_{\\alpha/2, n_1-1, n_2-2}")
	lol = limit2(sd1, sd2, F1)
	upl = limit2(sd1, sd2, F2)
	print ("\\\\Required confidence interval = \left(\\frac{" + str(sd1) + "^2}{" + str(sd2) + "^2}" + str(F1) + "}, \\frac{" + str(sd1) + "^2}{" + str(sd2) + "^2}" + str(F2) + "}\\right)")
	print ("Required confidence interval = (" + str(lol) + ", " + str(upl) + ")")
