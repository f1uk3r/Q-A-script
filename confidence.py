# python3
# confidence.py - Calculates confidence interval for a single or difference of the mean of a normal distributions
import scipy.stats as st
import math
import webbrowser
def error(z, sd, n):
	return round((z * sd) / math.sqrt(n), 4)
def sp(s1, s2, n1, n2):
	return round((math.sqrt((((n1 - 1) * (s1 ** 2)) + ((n2 - 1) * (s2 ** 2))) / (n1 + n2 - 2))), 4)
def errort2(t, s1, s2, n1, n2):
	return round(t * sp(s1, s2, n1, n2) * (math.sqrt((1/n1) + (1/n2))), 4)
def error2(z, s1, s2, n1, n2):
	return round(z * math.sqrt(((s1 ** 2) / n1) + ((s2 ** 2) / n2)), 4)

option = int(input("Choose 1 for Confidence interval, 2 for margin of error, 3 for both, 4 for finding n from margin of error: "))
typ = int(input("Press 1 to calculate ci of difference in means of two normal distribution: "))
if option == 1 and typ != 1:
	mean = float(input("\\\\Mean (\\bar{x}) = "))
	n = int(input("\\\\Sample\\ size (n) = "))
	sd = float(input("\\\\Standard\\ deviation (s) = "))
	ci = float(input("\\\\Confidence\\ interval\\ (in \\%) = "))
	if n < 30:
		t = round(st.t.ppf(1-((1-(ci/100))/2), n-1), 4)
		print ("\\\\t_{\\alpha/2, n-1} = " + str(t))
		print ("\\\\\\text{Since we know that}")
		print ("\\\\\\text{Confidence interval = }\\bar{x} \\pm t_{\\alpha/2, n-1}\\frac{s}{\\sqrt{n}}")
		E = error(t, sd, n)
		ll = round(mean - E, 4)
		ul = round(mean + E, 4)
		print ("\\\\\\text{Required confidence interval = }(" + str(mean) + "-" + str(t) + "\\frac{" + str(sd) + "}{\\sqrt{" + str(n) + "}}, "+ str(mean) + "+" + str(t) + "\\frac{" + str(sd) + "}{\\sqrt{" + str(n) + "}})")
		print ("Required confidence interval = (" + str(mean) + "-" + str(E) + ", "+ str(mean) + "+" + str(E) + ")")
		print ("Required confidence interval = (" + str(ll) + ", " + str(ul) + ")")
	else:
		z = round(st.norm.ppf(1-((1-(ci/100))/2)), 4)
		print ("z @ " + str(ci) + "% = " + str(z))
		print ("\\\\\\text{Since we know that}")
		print ("\\\\\\text{Confidence interval = }\\bar{x} \\pm z\\frac{s}{\\sqrt{n}}")
		E = error(z, sd, n)
		ll = round(mean - E, 4)
		ul = round(mean + E, 4)
		print ("\\\\\\text{Required confidence interval = }(" + str(mean) + "-" + str(z) + "\\frac{" + str(sd) + "}{\\sqrt{" + str(n) + "}}, "+ str(mean) + "+" + str(z) + "\\frac{" + str(sd) + "}{\\sqrt{" + str(n) + "}})")
		print ("Required confidence interval = (" + str(mean) + "-" + str(E) + ", "+ str(mean) + "+" + str(E) + ")")
		print ("Required confidence interval = (" + str(ll) + ", " + str(ul) + ")")
	print(f"Interpretion: We are {ci}% confident that the true mean of the population lie between the interval {ll} and {ul}.")
elif option == 2 and typ != 1:
	n = int(input("Sample size (n) = "))
	sd = float(input("Standard deviation (s) = "))
	ci = float(input("Confidence interval (in %) = "))
	if n < 30:
		t = round(st.t.ppf(1-((1-(ci/100))/2), n-1), 4)
		print ("\\\\t_{\\alpha/2, n-1} = " + str(t))
		E = error(t, sd, n)
		print ("\\\\t_{\\alpha/2, n-1} = " + str(t))
		print ("\\\\\\text{Since we know that}")
		print ("\\\\\\text{Margin of error = }t_{\\alpha/2, n-1}\\frac{s}{\\sqrt{n}}")
		print ("\\\\\\text{Margin of error = }" + str(t) + "\\frac{" + str(sd) + "}{\\sqrt{" + str(n) + "}}")
		print ("\\\\\\text{Margin of error = }" + str(E))
	else:
		z = round(st.norm.ppf(1-((1-(ci/100))/2)), 4)
		E = error(z, sd, n)
		print ("z @ " + str(ci) + "% = " + str(z))
		print ("\\\\\\text{Since we know that}")
		print ("\\\\\\text{Margin of error = }z\\frac{s}{\\sqrt{n}}")
		print ("\\\\\\text{Margin of error = }" + str(z) + "\\frac{" + str(sd) + "}{\\sqrt{" + str(n) + "}}")
		print ("\\\\\\text{Margin of error = }" + str(E))
elif option == 3 and typ != 1:
	mean = float(input("Mean (\\bar{x}) = "))
	n = int(input("Sample size (n) = "))
	sd = float(input("Standard deviation (s) = "))
	ci = float(input("Confidence interval (in %) = "))
	if n < 30:
		t = round(st.t.ppf(1-((1-(ci/100))/2), n-1), 4)
		print ("\\\\t_{\\alpha/2, n-1} = " + str(t))
		print ("\\\\\\text{Since we know that}")
		print ("\\\\\\text{Margin of error = }t_{\\alpha/2, n-1}\\frac{s}{\\sqrt{n}}")
		E = error(t, sd, n)
		ll = round(mean - E, 4)
		ul = round(mean + E, 4)
		print ("\\\\\\text{Margin of error = }" + str(t) + "\\frac{" + str(sd) + "}{\\sqrt{" + str(n) + "}}")
		print ("\\\\\\text{Margin of error = }" + str(E))
		print ("\\\\\\text{Confidence interval = }\\bar{x} \\pm t_{\\alpha/2, n-1}\\frac{s}{\\sqrt{n}}")
		print ("\\\\\\text{Required confidence interval = }(" + str(mean) + "-" + str(t) + "\\frac{" + str(sd) + "}{\\sqrt{" + str(n) + "}}, "+ str(mean) + "+" + str(t) + "\\frac{" + str(sd) + "}{\\sqrt{" + str(n) + "}})")
		print ("Required confidence interval = (" + str(mean) + "-" + str(E) + ", "+ str(mean) + "+" + str(E) + ")")
		print ("Required confidence interval = (" + str(ll) + ", " + str(ul) + ")")
	else:
		z = round(st.norm.ppf(1-((1-(ci/100))/2)), 4)
		print ("z @ " + str(ci) + "% = " + str(z))
		print ("\\\\\\text{Since we know that}")
		print ("\\\\\\text{Confidence interval = }\\bar{x} \\pm z\\frac{s}{\\sqrt{n}}")
		print ("\\\\And")
		print ("\\\\\\text{Margin of error(e) = }z\\frac{s}{\\sqrt{n}}")
		E = error(z, sd, n)
		ll = round(mean - E, 4)
		ul = round(mean + E, 4)
		print ("\\\\\\text{Margin of error = }" + str(z) + "\\frac{" + str(sd) + "}{\\sqrt{" + str(n) + "}}")
		print ("\\\\\\text{Margin of error = }" + str(E))
		print ("\\\\Required\\; confidence\\; interval = (" + str(mean) + "-" + str(z) + "\\frac{" + str(sd) + "}{\\sqrt{" + str(n) + "}}, "+ str(mean) + "+" + str(z) + "\\frac{" + str(sd) + "}{\\sqrt{" + str(n) + "}})")
		print ("Required confidence interval = (" + str(mean) + "-" + str(E) + ", "+ str(mean) + "+" + str(E) + ")")
		print ("Required confidence interval = (" + str(ll) + ", " + str(ul) + ")")
elif option == 4 and typ != 1:
	e = float(input("Margin of error (e) = "))
	sd = float(input("Standard deviation (s) = "))
	ci = float(input("Confidence interval(in %) = "))
	z = round(st.norm.ppf(1-((1-(ci/100))/2)), 4)
	print ("z @ " + str(ci) + "% = " + str(z))
	print ("\\\\\\text{Since we know that}")
	print ("\\\\\\text{Margin of error = }z\\frac{s}{\\sqrt{n}}")
	print (f"\\\\{e} = {z}\\frac{{{sd}}}{{\\sqrt{{n}}}}")
	print (f"\\\\\\sqrt{{n}} = {z}\\frac{{{sd}}}{{{e}}}")
	print (f"\\\\\\sqrt{{n}} = {round((z*sd)/e, 4)}")
	print (f"\\\\n = {round(((z*sd)/e)**2, 4)}")
if option == 1 and typ == 1:
	varknown = int(input("Is population variance/standart deviation known? Press 1 for yes: "))
	mean1 = float(input("\\\\Mean\\ 1 (\\bar{X_1}) = "))
	n1 = int(input("\\\\Sample\\ size\\ 1 (n_1) = "))
	sd1 = float(input("\\\\Standard\\ deviation\\ 1 (s_1) = "))
	mean2 = float(input("\\\\Mean\\ 2 (\\bar{X_2}) = "))
	n2 = int(input("\\\\Sample\\ size\\ 2 (n_2) = "))
	sd2 = float(input("\\\\Standard\\ deviation\\ 2 (s_2) = "))
	ci = float(input("Confidence interval(in %) = "))
	if varknown != 1:
		if n1 + n2 - 2 < 30:
			t = round(st.t.ppf(1-((1-(ci/100))/2), n1 + n2 - 1), 4)
			print("\\\\t_{\\alpha/2, n_1 + n_2 -2} = " + str(t))
			print ("\\\\\\text{Since we know that}")
			print ("\\\\S_P = \sqrt{\\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}}")
			print (f"\\\\S_P = \\sqrt{{\\frac{{({n1}-1){sd1}^2 + ({n2}-1){sd2}^2}}{{{n1} + {n2} - 2}}}}")
			print (f"\\\\S_P = \\sqrt{{\\frac{{({n1-1}){sd1**2} + ({n2-1}){sd2**2}}}{{{n1 + n2 - 2}}}}}")
			E = errort2(t, sd1, sd2, n1, n2)
			sP = sp(sd1, sd2, n1, n2)
			ll = round(mean1 - mean2 - E, 4)
			ul = round(mean1 - mean2 + E, 4)
			mean = round(mean1 - mean2, 4)
			print(f"\\\\S_P = {sP}")
			print ("\\\\\\text{Confidence interval = }\\bar{X_1}-\\bar{X_2} \\pm t_{\\alpha/2, n-1}S_P\\sqrt{\\frac{1}{n_1}+\\frac{1}{n_2}}")
			print (f"\\\\\\text{{Required confidence interval = }}({mean1} - {mean2} - ({t}) ({sP})\\sqrt{{\\frac{{1}}{{{n1}}}+\\frac{{1}}{{{n2}}}}}, {mean1} - {mean2} + ({t})  ({sP})\\sqrt{{\\frac{{1}}{{{n1}}}+\\frac{{1}}{{{n2}}}}})")
			print ("Required confidence interval = (" + str(mean) + "-" + str(E) + ", "+ str(mean) + "+" + str(E) + ")")
			print ("Required confidence interval = (" + str(ll) + ", " + str(ul) + ")")
		else:
			z = round(st.norm.ppf(1-((1-(ci/100))/2)), 4)
			print ("z @ " + str(ci) + "% = " + str(z))
			print ("\\\\\\text{Since we know that}")
			print ("\\\\\\text{Confidence interval = }\\bar{X_1}-\\bar{X_2} \\pm z_{\\alpha/2}\\sqrt{\\frac{\\sigma_1^2}{n_1} + \\frac{\\sigma_2^2}{n_2}}")
			E = error2(z, sd1, sd2, n1, n2)
			ll = round(mean1 - mean2 - E, 4)
			ul = round(mean1 - mean2 + E, 4)
			print ("\\\\\\text{Required confidence interval = }(" + str(mean1) + "-" + str(mean2) + "-" + str(z) + "\\sqrt{\\frac{" + str(sd1) + "^2}{" + str(n1) + "} + \\frac{" + str(sd2) + "^2}{" + str(n2) + "}}, " + str(mean1) + "-" + str(mean2) + "+" + str(z) + "\\sqrt{\\frac{" + str(sd1) + "^2}{" + str(n1) + "} + \\frac{" + str(sd2) + "^2}{" + str(n2) + "}})")
			print ("Required confidence interval = (" + str(mean1) + "-" + str(mean2) + "-" + str(E) + ", "+ str(mean1) + "-" + str(mean2) + "+" + str(E) + ")")
			print ("Required confidence interval = (" + str(ll) + ", " + str(ul) + ")")
print ("Please hit thumbs up if the answer helped you.")
