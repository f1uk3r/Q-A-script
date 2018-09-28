import math
import webbrowser
def stdError1(p, N, n):
	return round(math.sqrt((p * (1 - p)) / n) * math.sqrt((N-n)/(N-1)), 4)
def stdError2(p, n):
	return round(math.sqrt((p * (1 - p)) / n), 4)
def error(z, sd):
	return round((z * sd), 4)
def stdErrorTwoProportion(p1,p2,n1,n2):
	return round(math.sqrt(((p1*(1-p1))/n1)+((p2*(1-p2))/n2)),4)
zs = dict([(70, 1.04), (75, 1.15), (80, 1.282), (85, 1.44), (90, 1.645), (92, 1.75), (95, 1.96), (96, 2.05), (98, 2.33), (99, 2.576), (99.5, 2.807), (99.9, 3.291)])
option = int(input("Choose 1 for Confidence interval, 2 for margin of error and 3 for both: "))
typ = int(input("Choose 1 if you have to find confidence interval on the difference between two proportion: "))
pop = int(input("Population size given? 1. for yes"))
if option == 1 and typ != 1:
	p = float(input("Sample proportion (\\hat{p}) = "))
	if pop == 1:
		N = int(input("Population size (N) = "))
	n = int(input("Sample size (n) = "))
	if pop == 1:
		sd = stdError1(p, N, n)
	else:
		sd = stdError2(p, n)
	ci = int(input("Confidence interval(in %) = "))
	
	z = zs.get(ci, 0)
	if z == 0:
		z = float(input("z = "))
	print ("z @ " + str(ci) + "% = " + str(z))
	E = error(z, sd)
	print ("Since we know that")
	print ("\\\\Confidence\; interval = \\hat{p} \pm z_{\\alpha}\sqrt{\\frac{\hat{p}(1-\hat{p})}{n}}")
	ll = round(p - E, 4)
	ul = round(p + E, 4)
	print ("\\\\Required\; confidence\; interval = (" + str(p) + "-" + str(z) + "\sqrt{\\frac{" + str(p) +"(1-" + str(p) + ")}{" + str(n) + "}}, "+ str(p) + "+" + str(z) + "\sqrt{\\frac{" + str(p) +"(1-" + str(p) + ")}{" + str(n) + "}})")
	print ("Required confidence interval = (" + str(p) + "-" + str(E) + ", "+ str(p) + "+" + str(E) + ")")
	print ("Required confidence interval = (" + str(ll) + ", " + str(ul) + ")")
elif option == 2 and typ != 1:
	p = float(input("Sample proportion (\\hat{p}) = "))
	if pop == 1:
		N = int(input("Population size (N) = "))
	n = int(input("Sample size (n) = "))
	if pop == 1:
		sd = stdError1(p, N, n)
	else:
		sd = stdError2(p, n)
	ci = int(input("Confidence interval(in %) = "))
	
	z = zs.get(ci, 0)
	if z == 0:
		z = float(input("z = "))
	print ("z @ " + str(ci) + "% = " + str(z))
	print ("Since we know that")
	print ("\\\\Margin\; of\; error =z_{\\alpha}\sqrt{\\frac{\hat{p}(1-\hat{p})}{n}}")
	E = error(z, sd)
	
	print ("\\\\Margin\; of\; error = " + str(z) + "\sqrt{\\frac{" + str(p) +"(1-" + str(p) + ")}{" + str(n) + "}}")
	print ("\\\\Margin\;of\;error = " + str(E))
elif option == 3 and typ != 1:
	p = float(input("Sample proportion (\\hat{p}) = "))
	if pop == 1:
		N = int(input("Population size (N) = "))
	n = int(input("Sample size (n) = "))
	if pop == 1:
		sd = stdError1(p, N, n)
	else:
		sd = stdError2(p, n)
	ci = int(input("Confidence interval(in %) = "))
	z = zs.get(ci, 0)
	if z == 0:
		z = float(input("z = "))
	print ("z @ " + str(ci) + "% = " + str(z))
	E = error(z, sd)
	print ("Since we know that")
	print ("\\\\Confidence\; interval = \\hat{p} \pm z_{\\alpha}\sqrt{\\frac{\hat{p}(1-\hat{p})}{n}}")
	print ("\\\\And")
	print ("\\\\Margin\; of\; error =z_{\\alpha}\sqrt{\\frac{\hat{p}(1-\hat{p})}{n}}")
	ll = round(p - E, 4)
	ul = round(p + E, 4)
	print ("\\\\Margin\; of\; error = " + str(z) + "\sqrt{\\frac{" + str(p) +"(1-" + str(p) + ")}{" + str(n) + "}}")
	print ("\\\\Margin\;of\;error = " + str(E))
	print ("\\\\Required\; confidence\; interval = (" + str(p) + "-" + str(z) + "\sqrt{\\frac{" + str(p) +"(1-" + str(p) + ")}{" + str(n) + "}}, "+ str(p) + "+" + str(z) + "\sqrt{\\frac{" + str(p) +"(1-" + str(p) + ")}{" + str(n) + "}})")
	print ("Required confidence interval = (" + str(p) + "-" + str(E) + ", "+ str(p) + "+" + str(E) + ")")
	print ("Required confidence interval = (" + str(ll) + ", " + str(ul) + ")")
elif option == 1 and typ == 1:
	p1 = float(input("Sample proportion1 (\\hat{p1}) = "))
	p2 = float(input("Sample proportion2 (\\hat{p2}) = "))
	n1 = int(input("Sample size1 (n1) = "))
	n2 = int(input("Sample size2 (n2) = "))
	p = p1-p2
	sd = stdErrorTwoProportion(p1,p2,n1,n2)
	ci = int(input("Confidence interval(in %) = "))
	
	z = zs.get(ci, 0)
	if z == 0:
		z = float(input("z = "))
	print ("z @ " + str(ci) + "% = " + str(z))
	E = error(z, sd)
	print ("Since we know that")
	print ("\\\\Confidence\; interval = \\hat{p_1}-\\hat{p_2} \pm z_{\\alpha/2}\sqrt{\\frac{\hat{p_1}(1-\hat{p1})}{n1}+\\frac{\hat{p_1}(1-\hat{p1})}{n1}}")
	ll = round(p - E, 4)
	ul = round(p + E, 4)
	print ("\\\\Required\; confidence\; interval = (" + str(p1) + "-" + str(p2) + "-" + str(z) + "\sqrt{\\frac{" + str(p1) +"(1-" + str(p1) + ")}{" + str(n1) + "} + \\frac{" + str(p2) +"(1-" + str(p2) + ")}{" + str(n2) + "}}, "+ str(p1) + "-" + str(p2) + "+" + str(z) + "\sqrt{\\frac{" + str(p1) +"(1-" + str(p1) + ")}{" + str(n1) + "} + \\frac{" + str(p2) +"(1-" + str(p2) + ")}{" + str(n2) + "}})")
	print ("Required confidence interval = (" + str(p) + "-" + str(E) + ", "+ str(p) + "+" + str(E) + ")")
	print ("Required confidence interval = (" + str(ll) + ", " + str(ul) + ")")
print ("Please hit thumps up if the answer helped you.")