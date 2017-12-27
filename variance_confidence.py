import webbrowser
import math

def ll(n, sd, chi1):
	return round(((n-1) * (sd ** 2) /(chi1 ** 2)), 4)

def ul(n, sd, chi2):
	return round(((n-1) * (sd ** 2) /(chi2 ** 2)), 4)

n = int(input("Sample size (n) = "))
sd = float(input("Standard deviation (s) = "))
ci = int(input("Confidence interval(in %) = "))
print ("We have to find confidence interval for variance of the sample")
webbrowser.open('https://www.danielsoper.com/statcalc/calculator.aspx?id=12')
chi1 = float(input("\chi_{\\alpha/2, n-1}^2 = "))
chi2 = float(input("\chi_{1-\\alpha/2, n-1}^2 = "))
print ("Since we know that")
print ("Confidence\; interval = \\frac{(n-1)S^2}{\chi_{\\alpha/2, n-1}^2}, \\frac{(n-1)S^2}{\chi_{1-\\alpha/2, n-1}^2}")
lol = ll(n, sd, chi1)
upl = ul(n, sd, chi2)
print ("Required confidence interval = \left(\\frac{(" + str(n) + "-1)" + str(sd) + "^2}{" + str(chi1) + "}, \\frac{(" + str(n) + "-1)" + str(sd) + "^2}{" + str(chi2) + "}\\right)")
print ("Required confidence interval = (" + str(lol) + ", " + str(upl) + ")")
