import math, webbrowser

def calChi(s, sd, n):
	return round(((n-1) * s** 2) / (sd ** 2), 4)

def calF(s1, s2):
	return round(s1/s2, 4)
print("1. Alternative hypothesis \\neq\n2. Alternative hypothesis <\n3. Alternative hypothesis >")
print("4. For 2 distributions alternative hypothesis \\neq\n5. For 2 distributions alternative hypothesis <\n6. For 2 distributions alternative hypothesis >")
type1 = int(input("Mention the type as legend: "))
if type1 < 4:
	n = int(input("Sample Size (n) = "))
	sd = float(input("Variance \sigma_0^2 = "))
	s = float(input("Sample variance (S^2) = "))
	alpha = round(float(input("\\alpha = ")) / 2, 4)
elif type1>3 and type1<7:
	var1 = float(input("\\\\Variance1(S_1^2) = "))
	var2 = float(input("\\\\Variance1(S_2^2) = "))
	n1 = int(input("\\\\Sample\;Size(n_1) = "))
	n2 = int(input("\\\\Sample\;Size(n_2) = "))
	alpha = round(float(input("\\alpha = ")) / 2, 4)

if type1 == 1:
	print("We are interested in testing the hypothesis")
	print("\\\\Null\;Hypothesis --> H_0: \sigma^2 = \sigma_0^2")
	print("\\\\Alternate\;Hypothesis --> H_1: \sigma^2 \\ne \sigma_0^2")
	print("Now, the value of test static can be found out by following formula: ")
	print("\chi_0^2 = \\frac{(n-1)S^2}{\sigma_0^2}")
	print("\chi_0^2 = \\frac{(" + str(n) + "-1)" + str(s) + "^2}{" + str(sd) + "^2}")
	cFinal = calChi(s, sd, n)
	print("\chi_0^2 = " + str(cFinal))
	webbrowser.open('https://www.danielsoper.com/statcalc/calculator.aspx?id=12')
	critRight = float(input("\chi_{\\alpha/2, n-1}^2 = "))
	critLeft = float(input("\chi_{1-\\alpha/2, n-1}^2 = "))
	if cFinal > critRight or cFinal < critLeft:
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are \chi_{" + str(alpha) + ", " + str(n-1) + "}^2 = " + str(critRight) + " and \chi_{1-" + str(alpha) + ", " + str(n-1) + "}^2 = " + str(critLeft) + " and we note that \chi_0^2 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the variance is not equal to " + str(variance))
	else:
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are \chi_{" + str(alpha) + ", " + str(n-1) + "}^2 = " + str(critRight) + " and \chi_{1-" + str(alpha) + ", " + str(n-1) + "}^2 = " + str(critLeft) + " and we note that \chi_0^2 does not falls in the critical region. Therefore, we are failed to reject H_0.")

elif type1 == 2:
	type2 = int(input("1. Null Hypothesis =\n2. Null Hypophesis \le"))
	print("We are interested in testing the hypothesis")
	if type2 == 1:
		print("\\\\Null\;Hypothesis --> H_0: \sigma^2 = \sigma_0^2")
	else:
		print("\\\\Null\;Hypothesis --> H_0: \sigma^2 \le \sigma_0^2")
	print("\\\\Alternate\;Hypothesis --> H_1: \sigma^2 > \sigma_0^2")
	print("Now, the value of test static can be found out by following formula: ")
	print("\chi_0^2 = \\frac{(n-1)S^2}{\sigma_0^2}")
	print("\chi_0^2 = \\frac{(" + str(n) + "-1)" + str(s) + "^2}{" + str(sd) + "^2}")
	cFinal = calChi(s, sd, n)
	print("\chi_0^2 = " + str(cFinal))
	webbrowser.open('https://www.danielsoper.com/statcalc/calculator.aspx?id=12')
	crit = float(input("\chi_{\\alpha, n-1}^2 = "))
	if cFinal > crit:
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are \chi_{" + str(alpha*2) + ", " + str(n-1) + "}^2 = " + str(crit) + " and we note that \chi_0^2 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the variance is not equal to " + str(variance))
	else:
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are \chi_{" + str(alpha*2) + ", " + str(n-1) + "}^2 = " + str(crit) + " and we note that \chi_0^2 does not falls in the critical region. Therefore, we are failed to reject H_0.")

elif type1 == 3:
	type2 = int(input("1. Null Hypothesis =\n2. Null Hypophesis \ge"))
	print("We are interested in testing the hypothesis")
	if type2 == 1:
		print("\\\\Null\;Hypothesis --> H_0: \sigma^2 = \sigma_0^2")
	else:
		print("\\\\Null\;Hypothesis --> H_0: \sigma^2 /ge \sigma_0^2")
	print("\\\\Alternate\;Hypothesis --> H_1: \sigma^2 < \sigma_0^2")
	print("Now, the value of test static can be found out by following formula: ")
	print("\chi_0^2 = \\frac{(n-1)S^2}{\sigma_0^2}")
	print("\chi_0^2 = \\frac{(" + str(n) + "-1)" + str(s) + "^2}{" + str(sd) + "^2}")
	cFinal = calChi(s, sd, n)
	print("\chi_0^2 = " + str(cFinal))
	webbrowser.open('https://www.danielsoper.com/statcalc/calculator.aspx?id=12')
	crit = float(input("\chi_{1-\\alpha/2, n-1}^2 = "))
	if cFinal < crit:
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are \chi_{1-" + str(alpha*2) + ", " + str(n-1) + "}^2 = " + str(crit) + " and we note that \chi_0^2 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the variance is not equal to " + str(variance))
	else:
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are \chi_{1-" + str(alpha*2) + ", " + str(n-1) + "}^2 = " + str(crit) + " and we note that \chi_0^2 does not falls in the critical region. Therefore, we are failed to reject H_0.")

if type1 == 4:
	print("We are interested in testing the hypothesis")
	print("\\\\Null\;Hypothesis --> H_0: \sigma_1^2 = \sigma_2^2")
	print("\\\\Alternate\;Hypothesis --> H_1: \sigma_1^2 \\ne \sigma_2^2")
	print("Now, the value of test static can be found out by following formula: ")
	print("F_0 = \\frac{S_1^2}{S_2^2}")
	print("F_0 = \\frac{"  + str(var1) + "}{" + str(var2) + "}")
	fFinal = calF(var1, var2)
	print("F_0 = " + str(fFinal))
	webbrowser.open('https://www.danielsoper.com/statcalc/calculator.aspx?id=4')
	critRight = float(input("F_{\\alpha/2, n_1-1, n_2-1} = "))
	critLeft = float(input("F_{1-\\alpha/2, n_1-1, n_2-1} = "))
	if fFinal > critRight or fFinal < critLeft:
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are F_{" + str(alpha) + ", " + str(n1-1) + ", " + str(n2-1) + "} = " + str(critRight) + " and F_{1-" + str(alpha) + ", " + str(n1-1) + ", " + str(n2-1) + "} = " + str(critLeft) + " and we note that F_0 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the variance is not equal to " + str(variance))
	else:
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are F_{" + str(alpha) + ", " + str(n1-1) + ", " + str(n2-1) + "} = " + str(critRight) + " and F_{1-" + str(alpha) + ", " + str(n1-1) + ", " + str(n2-1) + "} = " + str(critLeft) + " and we note that F_0 does not falls in the critical region. Therefore, we are failed to reject H_0.")

elif type1 == 2:
	type2 = int(input("1. Null Hypothesis =\n2. Null Hypophesis \le"))
	print("We are interested in testing the hypothesis")
	if type2 == 1:
		print("\\\\Null\;Hypothesis --> H_0: \sigma_1^2 = \sigma_2^2")
	else:
		print("\\\\Null\;Hypothesis --> H_0: \sigma_1^2 \le \sigma_2^2")
	print("\\\\Alternate\;Hypothesis --> H_1: \sigma_1^2 > \sigma_2^2")
	print("Now, the value of test static can be found out by following formula: ")
	print("F_0 = \\frac{S_1^2}{S_2^2}")
	print("F_0 = \\frac{"  + str(var1) + "}{" + str(var2) + "}")
	fFinal = calF(var1, var2)
	print("F_0 = " + str(fFinal))
	webbrowser.open('https://www.danielsoper.com/statcalc/calculator.aspx?id=4')
	crit = float(input("F_{\\alpha/2, n_1-1, n_2-1} = "))
	if fFinal > crit:
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are F_{" + str(alpha*2) + ", " + str(n1-1) + ", " + str(n2-1) + "} = " + str(crit) + " and we note that F_0 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the variance is not equal to " + str(variance))
	else:
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are \chi_{" + str(alpha*2) + ", " + str(n1-1) + ", " + str(n2-1) + "} = " + str(crit) + " and we note that F_0 does not falls in the critical region. Therefore, we are failed to reject H_0.")

elif type1 == 3:
	type2 = int(input("1. Null Hypothesis =\n2. Null Hypophesis \ge"))
	print("We are interested in testing the hypothesis")
	if type2 == 1:
		print("\\\\Null\;Hypothesis --> H_0: \sigma^2 = \sigma_0^2")
	else:
		print("\\\\Null\;Hypothesis --> H_0: \sigma^2 /ge \sigma_0^2")
	print("\\\\Alternate\;Hypothesis --> H_1: \sigma^2 < \sigma_0^2")
	print("Now, the value of test static can be found out by following formula: ")
	print("F_0 = \\frac{S_1^2}{S_2^2}")
	print("F_0 = \\frac{"  + str(var1) + "}{" + str(var2) + "}")
	fFinal = calF(var1, var2)
	print("F_0 = " + str(fFinal))
	webbrowser.open('https://www.danielsoper.com/statcalc/calculator.aspx?id=4')
	crit = float(input("F_{1-\\alpha/2, n_1-1, n_2-1} = "))
	if fFinal < crit:
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are F_{1-" + str(alpha*2) + ", " + str(n1-1) + ", " + str(n2-1) + "} = " + str(crit) + " and we note that F_0 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the variance is not equal to " + str(variance))
	else:
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are F_{1-" + str(alpha*2) + ", " + str(n1-1) + ", " + str(n2-1) + "} = " + str(crit) + " and we note that F_0 does not falls in the critical region. Therefore, we are failed to reject H_0.")


