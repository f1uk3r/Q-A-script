import math
import webbrowser
import scipy.stats as st
def stdError2(p, n):
	return round(math.sqrt((p * (1 - p)) / n), 4)
def error(z, sd):
	return round((z * sd), 4)
def stdErrorTwoProportion(p1,p2,n1,n2):
	return round(math.sqrt(((p1*(1-p1))/n1)+((p2*(1-p2))/n2)),4)
option = int(input("Choose 1 for Confidence interval, 2 for margin of error, 3 for both: , 4. Choice of sample size when margin of error is given"))
typ = int(input("Choose 1 if you have to find confidence interval on the difference between two proportion: "))
#pop = int(input("Population size given? 1. for yes"))
if option != 4:
	proportionOrNumber = int(input("Give 1. proportion or 2. number of event"))
if typ != 1:
	if option < 4:
		if proportionOrNumber == 1:
			p = float(input("\\hat p = "))
			n = int(input("Total number of sample (n) = "))
		elif proportionOrNumber == 2:
			n = int(input("Total number of sample (n) = "))
			x = int(input("number of favourable events (X) = "))
			p = round(x/n,4)
			print(f"\\hat p = X/n = {x}/{n} = {p}")
		#if pop == 1:
		#	N = int(input("Population size (N) = "))
		#	sd = stdError1(p, N, n)
		else:
			sd = stdError2(p, n)
		ci = int(input("Confidence interval(in %) = "))
		
		z = round(st.norm.ppf(1-((1-(ci/100))/2)), 4)
		print (f"\\\\z_{{\\alpha/2}} = z_{{{round((1-(ci/100))/2, 4)}}} = {z}")
		print ("\\\\\\text{Since we know that}")
		E = error(z, sd)
		ll = round(p - E, 4)
		ul = round(p + E, 4)
		if option == 2 or option == 3:
			print ("\\\\\\text{Margin of error = }z_{\\alpha/2}\\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n}}")
			print (f"\\\\\\text{{Margin of error = }}{z}\\sqrt{{\\frac{{{p}(1-\\hat{p})}}{{{n}}}}}")
			print (f"\\\\\\text{{Margin of error = }}{z}\\sqrt{{{round((p*(1 - p))/n, 4)}}}")
			print (f"\\\\\\text{{Margin of error = }}{E}")
		if option == 1 or option == 3:
			print ("\\\\\\text{Confidence interval = }\\hat{p} \\pm z_{\\alpha/2}\\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n}}")
			print (f"\\\\\\text{{Required confidence interval = }}({p}-{z}\\sqrt{{\\frac{{{p}(1-{p})}}{{{n}}}}}, {p}+{z}\\sqrt{{\\frac{{{p}(1-{p})}}{{{n}}}}})")
			print (f"\\\\\\text{{Required confidence interval = }}({p}-{z}\\sqrt{{\\frac{{{p}({1-p})}}{{{n}}}}}, {p}+{z}\\sqrt{{\\frac{{{p}({1-p})}}{{{n}}}}})")
			print (f"\\\\\\text{{Required confidence interval = }}({p}-{z}\\sqrt{{{round((p*(1-p))/n, 4)}}}, {p}+{z}\\sqrt{{{round((p*(1-p))/n, 4)}}})")
			print (f"Required confidence interval = ({p}-{z}({sd}), {p}+{z}({sd}))")
			print (f"Required confidence interval = ({p}-{E}, {p}+{E})")
			print (f"Required confidence interval = ({ll}, {ul})")
	if option == 4:
		p = float(input("p = "))
		ci = int(input("Confidence interval(in %) = "))
		E = float(input("Margin of error (E) = "))
		print("Since we know that")
		print("\\\\\\text{Margin of error = }z_{\\alpha/2}\\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n}}")
		print("\\\\n = \\left(\\frac{z_{\\alpha/2}}{E}\\right)^2 p(1-p)")
		print(f"\\\\n = \\left(\\frac{{{z}}}{{{E}}}\\right)^2 {p}(1-{p})")
		print(f"\\\\n = ({round(z/E, 4)})^2 {p}({1-p})")
		print(f"\\\\n = ({round((z/E)**2, 4)})({round(p*(1-p), 4)})")
		print(f"\\\\n = {round(((z/E)**2)*p*(1-p), 4)}")
		print(f"\\\\n \\approx {round(((z/E)**2)*p*(1-p))}")
elif option == 1 and typ == 1:
	n1 = int(input("Total number of sample 1 (n1) = "))
	n2 = int(input("Total number of sample 2 (n2) = "))
	if proportionOrNumber == 1:
		p1 = float(input("\\\\\\hat p_1 = "))
		p2 = float(input("\\\\\\hat p_2 = "))
	elif proportionOrNumber == 2:
		x1 = int(input("number of favourable events (X1) = "))
		x2 = int(input("number of favourable events (X2) = "))
		p1 = round(x1/n1, 4)
		p2 = round(x2/n2, 4)
		print(f"\\\\\\hat p_1 = \\frac{{X_1}}{{n_1}} = \\frac{{{x1}}}{{{n1}}} = {p1}")
		print(f"\\\\\\hat p_2 = \\frac{{X_2}}{{n_2}} = \\frac{{{x2}}}{{{n2}}} = {p2}")

	p = round(p1-p2, 4)
	sd = stdErrorTwoProportion(p1,p2,n1,n2)
	ci = int(input("Confidence interval(in %) = "))

	z = round(st.norm.ppf(1-((1-(ci/100))/2)), 4)
	print (f"\\\\z_{{\\alpha/2}} = z_{{{round((1-(ci/100))/2, 4)}}} = {z}")
	print ("\\\\\\text{Since we know that}")
	print ("\\\\\\text{Confidence interval = }\\hat{p_1}-\\hat{p_2} \\pm z_{\\alpha/2}\\sqrt{\\frac{\\hat{p_1}(1-\\hat{p_1})}{n_1}+\\frac{\\hat{p_2}(1-\\hat{p_2})}{n_2}}")
	E = error(z, sd)
	ll = round(p - E, 4)
	ul = round(p + E, 4)
	print (f"\\\\\\text{{Confidence interval = }}({p1} - {p2} - {z}\\sqrt{{\\frac{{{p1}(1-{p1})}}{{{n1}}}+\\frac{{{p2}(1-{p2})}}{{{n2}}}}}, {p1} - {p2} + {z}\\sqrt{{\\frac{{{p1}(1-{p1})}}{{{n1}}}+\\frac{{{p2}(1-{p2})}}{{{n2}}}}})")
	print (f"\\\\\\text{{Confidence interval = }}({p} - {z}\\sqrt{{\\frac{{{p1}({1-p1})}}{{{n1}}}+\\frac{{{p2}({1-p2})}}{{{n2}}}}}, {p} + {z}\\sqrt{{\\frac{{{p1}({1-p1})}}{{{n1}}}+\\frac{{{p2}({1-p2})}}{{{n2}}}}})")
	print (f"\\\\\\text{{Confidence interval = }}({p} - {z}\\sqrt{{{round((p1*(1-p1))/n1, 4)}+{round((p2*(1-p2))/n2, 4)}}}, {p} + {z}\\sqrt{{{round((p1*(1-p1))/n1, 4)}+{round((p2*(1-p2))/n2, 4)}}})")
	print (f"\\\\\\text{{Confidence interval = }}({p} - {z}\\sqrt{{{round((p1*(1-p1))/n1, 4)+round((p2*(1-p2))/n2, 4)}}}, {p} + {z}\\sqrt{{{round((p1*(1-p1))/n1, 4)+round((p2*(1-p2))/n2, 4)}}})")
	print (f"Required Confidence interval = ({p} - {z}({round(math.sqrt(((p1*(1-p1))/n1)+((p2*(1-p2))/n2)), 4)}), {p} + {z}({round(math.sqrt(((p1*(1-p1))/n1)+((p2*(1-p2))/n2)), 4)}))")
	print (f"Required Confidence interval = ({p} - {E}, {p} + {E})")
	print (f"Required Confidence interval = ({ll}, {ul})")
print ("Please hit thumps up if the answer helped you.")