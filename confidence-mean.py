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
if typ != 1:
	varknown = int(input("Is population variance/standard deviation known? Press 1 for yes: "))
	if option == 1 or option == 3: 
		mean = float(input(f"\\\\\\text{{Mean (}}\\bar{{x}}\\text{{) = }}"))
	n = int(input(f"\\\\\\text{{Sample size (n) = }}"))
	if varknown != 1:
		sd = float(input(f"\\\\\\text{{Standard deviation (s) = }}"))
	else:
		sd = float(input(f"\\\\\\text{{Standard deviation }} (\\sigma) = "))
	ci = float(input(f"\\\\\\text{{Confidence interval (in }}%\\text{{) = }}"))
	if option < 4:
		if (varknown != 1 and n < 30):
			z = round(st.t.ppf(1-((1-(ci/100))/2), n-1), 4)
			print (f"\\\\t_{{\\alpha/2, n-1}} = t_{{{round((1-(ci/100))/2, 4)}, {n-1}}} = {z}" )
			print ("\\\\\\text{Since we know that}")
			
		else:
			z = round(st.norm.ppf(1-((1-(ci/100))/2)), 4)
			print ("z @ " + str(ci) + "% = " + str(z))
			print ("\\\\\\text{Since we know that}")
		E = error(z, sd, n)
		ll = round(mean - E, 4)
		ul = round(mean + E, 4)
		if option == 2 or option == 3:
			if (varknown != 1 and n < 30):
				print ("\\\\\\text{Margin of error = }t_{\\alpha/2, n-1}\\frac{s}{\\sqrt{n}}")
			elif (varknown != 1 and n > 29):
				print ("\\\\\\text{Margin of error = }z\\frac{s}{\\sqrt{n}}")
			else:
				print ("\\\\\\text{Margin of error = }z\\frac{\\sigma}{\\sqrt{n}}")
			print (f"\\\\\\text{{Margin of error = }}{z}\\frac{{{sd}}}{{\\sqrt{{{n}}}}}")
			print (f"\\\\\\text{{Margin of error = }}{E}")
		if option == 1 or option == 3:
			if (varknown != 1 and n < 30):
				print ("\\\\\\\\\\\\\\text{Confidence interval = }\\bar{x} \\pm t_{\\alpha/2, n-1}\\frac{s}{\\sqrt{n}}")
			elif (varknown != 1 and n > 29):
				print ("\\\\\\\\\\\\\\text{Confidence interval = }\\bar{x} \\pm z\\frac{s}{\\sqrt{n}}")
			else:
				print ("\\\\\\\\\\\\\\text{Confidence interval = }\\bar{x} \\pm z\\frac{\\sigma}{\\sqrt{n}}")
			print (f"\\\\\\text{{Required confidence interval = }}({mean}-{z}\\frac{{{sd}}}{{\\sqrt{{{n}}}}}, {mean}+{z}\\frac{{{sd}}}{{\\sqrt{{{n}}}}})")
			print (f"Required confidence interval = ({mean}-{z}({round(sd/(n**0.5), 4)}), {mean}+{z}({round(sd/(n**0.5), 4)}))")
			print (f"Required confidence interval = ({mean} - {E}, {mean} + {E})")
			print (f"Required confidence interval = ({ll}, {ul})")
			print(f"Interpretion: We are {ci}% confident that the true mean of the population lie between the interval {ll} and {ul}.")

elif option == 4 and typ != 1:
	e = float(input("Margin of error (e) = "))
	sd = float(input("Standard deviation (s) = "))
	ci = float(input("Confidence interval(in %) = "))
	z = round(st.norm.ppf(1-((1-(ci/100))/2)), 4)
	print (f"z @ {ci}% = {z}")
	print ("Since we know that")
	print ("\\\\\\text{Margin of error = }z\\frac{s}{\\sqrt{n}}")
	print (f"\\\\{e} = {z}\\frac{{{sd}}}{{\\sqrt{{n}}}}")
	print (f"\\\\\\sqrt{{n}} = {z}\\frac{{{sd}}}{{{e}}}")
	print (f"\\\\\\sqrt{{n}} = {round((z*sd)/e, 4)}")
	print (f"\\\\n = {round(((z*sd)/e)**2, 4)}")
if typ == 1:
	varknown = int(input("Is population variance/standard deviation known? Press 1 for yes: "))
	if option == 1 or option == 3:
		mean1 = float(input(f"\\\\\\text{{Mean 1 }}(\\bar{{X_1}}) = "))
	if option < 4:
		n1 = int(input(f"\\\\\\text{{Sample size 1 }}(n_1) = "))
	if varknown != 1:
		sd1 = float(input(f"\\\\\\text{{Standard deviation 1 }}(s_1) = "))
	else:
		sd1 = float(input(f"\\\\\\text{{Standard deviation 1 }}(\\sigma_1) = "))
	if option == 1 or option == 3:
		mean2 = float(input(f"\\\\\\text{{Mean 2 }}(\\bar{{X_2}}) = "))
	if option < 4:
		n2 = int(input(f"\\\\\\text{{Sample size 2 }}(n_2) = "))
	if varknown != 1:
		sd2 = float(input(f"\\\\\\text{{Standard deviation 2 }}(s_2) = "))
	else:
		sd2 = float(input(f"\\\\\\text{{Standard deviation 2 }}(\\sigma_2) = "))
	ci = float(input("Confidence interval(in %) = "))
	if option < 4:
		if varknown != 1:
			variance_equality = int(input("1. If population variance are equal(If nothing is written about equality of population variance, most of the time they are equal)"))
			if variance_equality == 1:
				t = round(st.t.ppf(1-((1-(ci/100))/2), n1 + n2 - 2), 4)
				print(f"\\\\t_{{\\alpha/2, n_1 + n_2 -2}} = {t}")
				print ("\\\\\\text{Since we know that}")
				print ("\\\\S_P = \\sqrt{\\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}}")
				print (f"\\\\S_P = \\sqrt{{\\frac{{({n1}-1){sd1}^2 + ({n2}-1){sd2}^2}}{{{n1} + {n2} - 2}}}}")
				print (f"\\\\S_P = \\sqrt{{\\frac{{({n1-1}){sd1**2} + ({n2-1}){sd2**2}}}{{{n1 + n2 - 2}}}}}")
				E = errort2(t, sd1, sd2, n1, n2)
				sP = sp(sd1, sd2, n1, n2)
				ll = round(mean1 - mean2 - E, 4)
				ul = round(mean1 - mean2 + E, 4)
				mean = round(mean1 - mean2, 4)
				print(f"\\\\S_P = {sP}")
				if option == 2 or option == 3:
					print("\\\\\\text{Margin of error = } t_{\\alpha/2, n-1}S_P\\sqrt{\\frac{1}{n_1}+\\frac{1}{n_2}}")
					print(f"\\\\\\text{{Margin of error = }}({t}) ({sP})\\sqrt{{\\frac{{1}}{{{n1}}}+\\frac{{1}}{{{n2}}}}}")
					print(f"\\\\\\text{{Margin of error = }}({round(t*sP, 4)})\\sqrt{{{round((1/n1)+(1/n2), 4)}}}")
					print(f"\\\\\\text{{Margin of error = }}{E}")
				if option == 1 or option == 3:
					print ("\\\\\\text{Confidence interval = }\\bar{X_1}-\\bar{X_2} \\pm t_{\\alpha/2, n-1}S_P\\sqrt{\\frac{1}{n_1}+\\frac{1}{n_2}}")
					print (f"\\\\\\text{{Required confidence interval = }}({mean1} - {mean2} - ({t}) ({sP})\\sqrt{{\\frac{{1}}{{{n1}}}+\\frac{{1}}{{{n2}}}}}, {mean1} - {mean2} + ({t})  ({sP})\\sqrt{{\\frac{{1}}{{{n1}}}+\\frac{{1}}{{{n2}}}}})")
					print (f"\\\\\\text{{Required confidence interval = }}({mean1} - {mean2} - ({round(t*sP, 4)})\\sqrt{{{round((1/n1)+(1/n2), 4)}}}, {mean1} - {mean2} + ({round(t*sP, 4)})\\sqrt{{{round((1/n1)+(1/n2), 4)}}})")
					print (f"Required confidence interval = ({mean} - {E}, {mean} + {E})")
					print (f"Required confidence interval = ({ll}, {ul})")
			else:
				print("First we calculate degree of freedom")
				print("\\\\\\nu = \\frac{\\left(\\frac{S_1^2}{n_1} + \\frac{S_2^2}{n_2}\\right)^2}{\\frac{(S_1^2/n_1)^2}{n_1-1}+\\frac{(S_2^2/n_2)^2}{n_2-1}}")
				print(f"\\\\\\nu = \\frac{{\\left(\\frac{{{sd1}^2}}{{{n1}}} + \\frac{{{sd2}^2}}{{{n2}}}\\right)^2}}{{\\frac{{({sd1}^2/{n1})^2}}{{{n1}-1}}+\\frac{{({sd2}^2/{n2})^2}}{{{n2}-1}}}}")
				print(f"\\\\\\nu = \\frac{{\\left(\\frac{{{sd1**2}}}{{{n1}}} + \\frac{{{sd2**2}}}{{{n2}}}\\right)^2}}{{\\frac{{({sd1**2}/{n1})^2}}{{{n1-1}}}+\\frac{{({sd2**2}/{n2})^2}}{{{n2-1}}}}}")
				print(f"\\\\\\nu = \\frac{{({round((sd1**2)/n1, 4)} + {round((sd2**2)/n2, 4)})^2}}{{\\frac{{({round((sd1**2)/n1, 4)})^2}}{{{n1-1}}}+\\frac{{({round((sd2**2)/n2, 4)})^2}}{{{n2-1}}}}}")
				print(f"\\\\\\nu = \\frac{{({round((sd1**2)/n1, 4) + round((sd2**2)/n2, 4)})^2}}{{\\frac{{({round(((sd1**2)/n1)**2, 4)})}}{{{n1-1}}}+\\frac{{({round(((sd2**2)/n2)**2, 4)})}}{{{n2-1}}}}}")
				print(f"\\\\\\nu = \\frac{{{round((round((sd1**2)/n1, 4) + round((sd2**2)/n2, 4))**2, 4)}}}{{{round((((sd1**2)/n1)**2)/(n1-1), 4)}+{round((((sd2**2)/n2)**2)/(n2-1), 4)}}}")
				print(f"\\\\\\nu = \\frac{{{round((round((sd1**2)/n1, 4) + round((sd2**2)/n2, 4))**2, 4)}}}{{{round((((sd1**2)/n1)**2)/(n1-1), 4)+round((((sd2**2)/n2)**2)/(n2-1), 4)}}}")
				df = round(((((sd1**2)/n1) + ((sd2**2)/n2))**2)/(((((sd1**2)/n1)**2)/(n1-1)) + ((((sd2**2)/n2)**2)/(n2-1))))
				print(f"\\\\\\nu = {round(round((round((sd1**2)/n1, 4) + round((sd2**2)/n2, 4))**2, 4)/(round((((sd1**2)/n1)**2)/(n1-1), 4)+round((((sd2**2)/n2)**2)/(n2-1), 4)), 4)}")
				print(f"\\\\\\nu \\approx {df}")
				t = round(st.t.ppf(1-((1-(ci/100))/2), df), 4)
				print(f"\\\\t_{{\\alpha/2, \\nu}} = {t}")
				print ("\\\\\\text{Since we know that}")
				E = errort2(t, sd1, sd2, n1, n2)
				ll = round(mean1 - mean2 - E, 4)
				ul = round(mean1 - mean2 + E, 4)
				mean = round(mean1 - mean2, 4)
				if option == 2 or option == 3:
					print("\\\\\\text{Margin of error = } t_{\\alpha/2, \\nu}\\sqrt{\\frac{s_1^2}{n_1} + \\frac{s_2^2}{n_2}}")
					print(f"\\\\\\text{{Margin of error = }}{t}\\sqrt{{\\frac{{{sd1}^2}}{{{n1}}} + \\frac{{{sd2}^2}}{{{n2}}}}}")
					print(f"\\\\\\text{{Margin of error = }}{t}\\sqrt{{{round((sd1**2)/n1, 4) + round((sd2**2)/n2, 4)}}}")
					print(f"\\\\\\text{{Margin of error = }}{t}({round((((sd1**2)/n1)+((sd2**2)/n2))**0.5, 4)})")
					print(f"\\\\\\text{{Margin of error = }}{E}")
				if option == 1 or option == 3:
					print ("\\\\\\text{Confidence interval = }\\bar{X_1}-\\bar{X_2} \\pm t_{\\alpha/2, \\nu}\\sqrt{\\frac{s_1^2}{n_1} + \\frac{s_2^2}{n_2}}")
					print (f"\\\\\\text{{Confidence interval = }}({mean1}-{mean2} - {t}\\sqrt{{\\frac{{{sd1}^2}}{{{n1}}} + \\frac{{{sd2}^2}}{{{n2}}}}}, {mean1}-{mean2} + {t}\\sqrt{{\\frac{{{sd1}^2}}{{{n1}}} + \\frac{{{sd2}^2}}{{{n2}}}}})")
					print (f"\\\\\\text{{Confidence interval = }}({mean} - {t}\\sqrt{{{round((sd1**2)/n1, 4)} + {round((sd2**2)/n2, 4)}}}, {mean} + {t}\\sqrt{{{round((sd1**2)/n1, 4)} + {round((sd2**2)/n2, 4)}}})")
					print (f"\\\\\\text{{Confidence interval = }}({mean} - {t}\\sqrt{{{round((sd1**2)/n1, 4) + round((sd2**2)/n2, 4)}}}, {mean} + {t}\\sqrt{{{round((sd1**2)/n1, 4) + round((sd2**2)/n2, 4)}}})")
					print (f"\\\\\\text{{Confidence interval = }}({mean} - {t}({round((((sd1**2)/n1)+((sd2**2)/n2))**0.5, 4)}), {mean} + {t}({round((((sd1**2)/n1)+((sd2**2)/n2))**0.5, 4)}))")
					print (f"Required confidence interval = ({mean} - {E}, {mean} + {E})")
					print (f"Required confidence interval = ({ll}, {ul})")
		else:
			z = round(st.norm.ppf(1-((1-(ci/100))/2)), 4)
			print (f"z @ {ci}% = {z}")
			print ("Since we know that")
			E = error2(z, sd1, sd2, n1, n2)
			ll = round(mean1 - mean2 - E, 4)
			ul = round(mean1 - mean2 + E, 4)
			mean = round(mean1 - mean2, 4)
			if option == 2 or option == 3:
				print("\\\\\\text{Margin of error = } z_{\\alpha/2}\\sqrt{\\frac{\\sigma_1^2}{n_1} + \\frac{\\sigma_2^2}{n_2}}")
				print(f"\\\\\\text{{Margin of error = }}{z}\\sqrt{{\\frac{{{sd1}}}^2}}{{{n1}}} + \\frac{{{sd2}^2}}{{{n2}}}}}")
				print(f"\\\\\\text{{Margin of error = }}{z}\\sqrt{{{round((sd1**2)/n1, 4) + round((sd2**2)/n2, 4)}}}")
				print(f"\\\\\\text{{Margin of error = }}{z}({round((((sd1**2)/n1)+((sd2**2)/n2))**0.5, 4)})")
				print(f"\\\\\\text{{Margin of error = }}{E}")
			if option == 1 or option == 3:
				print ("\\\\\\text{Confidence interval = }\\bar{X_1}-\\bar{X_2} \\pm z_{\\alpha/2}\\sqrt{\\frac{\\sigma_1^2}{n_1} + \\frac{\\sigma_2^2}{n_2}}")
				print (f"\\\\\\text{{Required confidence interval = }}({mean1}-{mean2}-{z}\\sqrt{{\\frac{{{sd1}^2}}{{{n1}}} + \\frac{{{sd2}^2}}{{{n2}}}}}, {mean1}-{mean2}+{z}\\sqrt{{\\frac{{{sd1}^2}}{{{n1}}} + \\frac{{{sd2}^2}}{{{n2}}}}})")
				print (f"\\\\\\text{{Required confidence interval = }}({mean} - {z}\\sqrt{{{round((sd1**2)/n1, 4)} + {round((sd2**2)/n2, 4)}}}, {mean} + {z}\\sqrt{{{round((sd1**2)/n1, 4)} + {round((sd2**2)/n2, 4)}}})")
				print (f"\\\\\\text{{Required confidence interval = }}({mean} - {z}\\sqrt{{{round((sd1**2)/n1, 4) + round((sd2**2)/n2, 4)}}}, {mean} + {z}\\sqrt{{{round((sd1**2)/n1, 4) + round((sd2**2)/n2, 4)}}})")
				print (f"\\\\\\text{{Required confidence interval = }}({mean} - {z}({round((((sd1**2)/n1)+((sd2**2)/n2))**0.5, 4)}), {mean} + {z}({round((((sd1**2)/n1)+((sd2**2)/n2))**0.5, 4)}))")
				print (f"Required confidence interval = ({mean}-{E}, {mean}+{E})")
				print (f"Required confidence interval = ({ll}, {ul})")
	if option == 4:
		E = float(input("Margin of error (E) = "))
		z = round(st.norm.ppf(1-((1-(ci/100))/2)), 4)
		print (f"z @ {ci}% = {z}")
		print ("Let n1 = n2 = n")
		print("Since we know that")
		print("\\\\\\text{Margin of error (E)= } z_{\\alpha/2}\\sqrt{\\frac{\\sigma_1^2}{n} + \\frac{\\sigma_2^2}{n}}")
		print("\\\\n = \\left(\\frac{z_{\\alpha/2}}{E}\\right)^2(\\sigma_1^2+\\sigma_2^2)")
		print(f"\\\\n = \\left(\\frac{{{z}}}{{{E}}}\\right)^2({sd1}^2+{sd2}^2)")
		print(f"\\\\n = ({round(z/E, 4)})^2({round(sd1**2, 4)}+{round(sd2**2, 4)})")
		print(f"\\\\n = {round((z/E)**2, 4)}({round(sd1**2+sd2**2, 4)})")
		print(f"\\\\n = {round(((z/E)**2)*(sd1**2+sd2**2), 4)}")
		print(f"\\\\n \\approx {round(((z/E)**2)*(sd1**2+sd2**2))}")
print ("Please hit thumbs up if the answer helped you.")
