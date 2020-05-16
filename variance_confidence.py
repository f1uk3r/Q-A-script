import scipy.stats as st
import webbrowser
import math

def test_statistic(n, sd, chi):
	return round(((n-1) * (sd ** 2) /(chi)), 4)

def limit2(sd1, sd2, F1):
	return round(((sd1 ** 2)/(sd2 ** 2)) * F1, 4)

option = int(input("Choose 1 to find C.I. of variance, 2 for lower confidence bound, 3 for upper confidence bound, 4 finding C.I. of ratio of the variances: "))
var_or_sd = int(input("Confidence interval for 1. variance or 2. standard deviation: "))
given_var_or_sd = int(input("Given value of 1. variance or 2. standard deviation: "))
if option < 4 :
	n = int(input("Sample size (n) = "))
	if (given_var_or_sd == 2):
		sd = float(input("Standard deviation (s) = "))
	elif (given_var_or_sd == 1):
		var = float(input("\\\\Variance (s^2) = "))
		sd = round(var**0.5, 4)
		print(f"Standard deviation (s) = {sd}")
	ci = int(input("Confidence interval(in %) = "))
	if option == 1:
		if (var_or_sd == 2):
			print (f"We have to find {ci} confidence interval for standard deviation")
			print("First we find the confidence interval for variance")
		elif (var_or_sd == 1):
			print (f"We have to find {ci} confidence interval for variance")
		chi1 = round(st.chi2.ppf(1-((1-(ci/100))/2), n-1), 4)
		chi2 = round(st.chi2.ppf((1-(ci/100))/2, n-1), 4)
		print(f"\\\\\\chi_{{\\alpha/2, n-1}}^2 = \\chi_{{{round((1-(ci/100))/2, 4)}, {n-1}}}^2 = {chi1}")
		print(f"\\\\\\chi_{{1-\\alpha/2, n-1}}^2 = \\chi_{{{round(1-((1-(ci/100))/2), 4)}, {n-1}}}^2 = {chi2}")
		print ("\\\\\\text{Confidence interval =} \\frac{(n-1)s^2}{\\chi_{\\alpha/2, n-1}^2}, \\frac{(n-1)s^2}{\chi_{1-\\alpha/2, n-1}^2}")
		lol = test_statistic(n, sd, chi1)
		upl = test_statistic(n, sd, chi2)
		print (f"\\\\\\text{{Required confidence interval = }}\\left(\\frac{{({n}-1){sd}^2}}{{{chi1}}}, \\frac{{({n}-1){sd}^2}}{{{chi2}}}\\right)")
		print (f"\\\\\\text{{Required confidence interval = }}\\left(\\frac{{({n-1}){round(sd**2, 4)}}}{{{chi1}}}, \\frac{{({n-1}){round(sd**2, 4)}}}{{{chi2}}}\\right)")
		print ("\\\\\\text{Required confidence interval = (" + str(lol) + ", " + str(upl) + ")}")
		if (var_or_sd == 2):
			print(f"\\\\\\text{{Taking the square root of the endpoints of this interval we obtain,}}")
			print(f"\\\\\\text{{Required confidence interval = (\\sqrt{{{lol}}}, \\sqrt{{{upl}}})}}")
			print(f"\\\\\\text{{Required confidence interval = ({round(lol**0.5, 4)}, {round(upl**0.5, 4)})}}")
			print(f"\\\\{round(lol**0.5, 4)} < \\sigma < {round(upl**0.5, 4)}")
		elif (var_or_sd ==1):
			print(f"\\\\{lol} \\le \\sigma \\le {upl}")
	elif option == 2:
		if (var_or_sd == 2):
			print (f"We have to find {ci} lower confidence bound for standard deviation")
			print("First we find the lower confidence bound for variance")
		elif (var_or_sd == 1):
			print (f"We have to find {ci} lower confidence bound for variance")
		chi = round(st.chi2.ppf(ci/100, n-1), 4)
		print(f"\\\\\\chi_{{\\alpha, n-1}}^2 = \\chi_{{{round(1-(ci/100), 4)}, {n-1}}}^2 = {chi}")
		print ("\\\\\\frac{(n-1)s^2}{\\chi_{\\alpha, n-1}^2} < \\sigma^2")
		print (f"\\\\\\frac{{({n}-1){sd}^2}}{{{chi}}} < \\sigma^2")
		print (f"\\\\\\frac{{({n-1}){round(sd**2, 4)}}}{{{chi}}} < \\sigma^2")
		lower_bound = test_statistic(n, sd, chi)
		print(f"\\\\{lower_bound} < \\sigma^2")
		if (var_or_sd == 2):
			print(f"\\\\\\text{{Taking the square root of the endpoints of this interval we obtain,}}")
			print(f"\\\\\\sqrt{{{lower_bound}}} < \\sigma")
			print(f"\\\\{round(lower_bound**0.5, 4)} < \\sigma")
	elif option == 3:
		if (var_or_sd == 2):
			print (f"We have to find {ci} upper confidence bound for standard deviation")
			print("First we find the upper confidence bound for variance")
		elif (var_or_sd == 1):
			print (f"We have to find {ci} upper confidence bound for variance")
		chi = round(st.chi2.ppf(1-(ci/100), n-1), 4)
		print(f"\\\\\\chi_{{1-\\alpha, n-1}}^2 = \\chi_{{{round(ci/100, 4)}, {n-1}}}^2 = {chi}")
		print ("\\\\\\sigma^2 < \\frac{(n-1)s^2}{\\chi_{1-\\alpha, n-1}^2}")
		print (f"\\\\\\sigma^2 < \\frac{{({n}-1){sd}^2}}{{{chi}}}")
		print (f"\\\\\\sigma^2 < \\frac{{({n-1}){round(sd**2, 4)}}}{{{chi}}}")
		upper_bound = test_statistic(n, sd, chi)
		print(f"\\\\\\sigma^2 < {upper_bound}")
		if (var_or_sd == 2):
			print(f"\\\\\\text{{Taking the square root of the endpoints of this interval we obtain,}}")
			print(f"\\\\\\sigma < \\sqrt{{{upper_bound}}}")
			print(f"\\\\\\sigma < {round(upper_bound**0.5, 4)}")
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
		
print("Please hit thumbs up if the answer helped you.")
