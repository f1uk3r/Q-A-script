import webbrowser, pyperclip, time, math
def zvalue(xbar, mean, sd, n):
	return round((xbar - mean)/(sd/math.sqrt(n)), 4)
	
def zfor2(x1, x2, s1, s2, n1, n2):
	return round((x1 - x2) / math.sqrt((s1/n1) + (s2/n2)), 4)

def varSq(s1, s2, n1, n2):
	return round((((n1 - 1) * s1) + ((n2 - 1) * s2)) / (n1 + n2 -2), 4)

def tvalue2(x1, x2, sp, n1, n2):
	return round((x1 - x2) / math.sqrt(sp * ((1/n1) + (1/n2))), 4)

zs = dict([(0.15, 1.04), (0.125, 1.15), (0.1, 1.282), (0.075, 1.44), (0.05, 1.645), (0.04, 1.75), (0.025, 1.96), (0.02, 2.05), (0.01, 2.33), (0.005, 2.576), (0.0025, 2.807), (0.0005, 3.291)])
print("1. Alternative hypothesis \\neq\n2. Alternative hypothesis <\n3. Alternative hypothesis >")
print("4. For two distributions Alternative hypothesis \\neq\n5. For two distributions Alternative hypothesis <\n6. For two distributions Alternative hypothesis >")
pval = int(input("Need to calculate P value also? Press 1 for yes: "))
type1 = int(input("Mention the type as legend: "))
sample = int(input("Means of how many Distributions: "))


if sample == 1:
	mean = float(input("\mu_0 = "))
	n = int(input("n = "))
	if n < 30:
		sd = float(input("S = "))
	elif n > 30:
		sd = float(input("\\\\\sigma = "))
	barx = float(input("\\\\\\bar{X} = "))
	alpha = round(float(input("\\\\\\alpha = ")) / 2, 4)
elif sample == 2:
	barx1 = float(input("\\\\\\bar{X_1} = "))
	barx2 = float(input("\\\\\\bar{X_2} = "))
	var1 = float(input("\\\\\sigma_1^2 = "))
	var2 = float(input("\\\\\sigma_2^2 = "))
	n1 = int(input("\\\\n_1 = "))
	n2 = int(input("\\\\n_2 = "))
	alpha = round(float(input("\\\\\\alpha = ")) / 2, 4)

if type1 == 1:
	print("We are interested in testing the hypothesis")
	print("\\\\Null\;Hypothesis --> H_0: \mu = \mu_0")
	print("\\\\Alternate\;Hypothesis --> H_1: \mu \\ne \mu_0")
	print("Now, the value of test static can be found out by following formula: ")
	if n > 30:
		print("Z_0 = \\frac{\\bar{X} - \mu_0}{\sigma/\sqrt{n}}")
		print("Z_0 = \\frac{" + str(barx) + "-" + str(mean) + "}{" + str(sd) + "/\sqrt{" + str(n) + "}}")
		zfinal = zvalue(barx, mean, sd, n)
		print("Z_0 = " + str(zfinal))
		if pval == 1:
			print("Since P-value of a two tailed test is equal to 2(1 - \phi(|Z_0|)")
			print("P = 2(1 - \phi(" + str(zfinal) + ")) ")
			pyperclip.copy(str(zfinal))
			webbrowser.open("https://www.easycalculation.com/statistics/p-value-for-z-score.php")
			forP = float(input())
			print("P = 2(1 - " + str(forP) + ") ")
			print("P = " + str(round(2 * (1 - forP), 4)))
		crit = zs.get(alpha, 0)
		if crit == 0:
			crit = float(input("critical value = "))
		if zfinal > crit or zfinal < (-crit):
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are Z_" + str(alpha) + " = " + str(crit) + " and -Z_" + str(alpha) + " = -" + str(crit) + " and we note that Z_0 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the mean is not equal to " + str(mean))
		else:
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are Z_" + str(alpha) + " = " + str(crit) + " and -Z_" + str(alpha) + " = -" + str(crit) + " and we note that Z_0 does not falls in the critical region. Therefore, we fail to reject H_0.")
	else:
		print("t_0 = \\frac{\\bar{X} - \mu_0}{S/\sqrt{n}}")
		print("t_0 = \\frac{" + str(barx) + "- " + str(mean) + "}{" + str(sd) + "/\sqrt{" + str(n) + "}}")
		zfinal = zvalue(barx, mean, sd, n)
		print("t_0 = " + str(zfinal))
		pyperclip.copy(str(alpha))
		webbrowser.open('https://www.danielsoper.com/statcalc/calculator.aspx?id=10')
		crit = float(input("critical value(t_{\\alpha/2, n-1}) = "))
		if zfinal > crit or zfinal < (-crit):
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are t_{" + str(alpha) + ", " + str(n-1) + "} = " + str(crit) + " and -t_{" + str(alpha) + ", " + str(n-1) + " = -" + str(crit) + " and we note that Z_0 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the mean is not equal to " + str(mean))
		else:
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are t_{" + str(alpha) + ", " + str(n-1) + " = " + str(crit) + " and -t_{" + str(alpha) + ", " + str(n-1) + " = -" + str(crit) + " and we note that Z_0 does not falls in the critical region. Therefore, we fail to reject H_0.")
	
elif type1 == 2:
	type2 = int(input("1. Null Hypothesis =\n2. Null Hypophesis \ge"))
	print("We are interested in testing the hypothesis")
	if type2 == 1:
		print("\\\\Null\;Hypothesis --> H_0: \mu = \mu_0")
	elif type2 ==2:
		print("\\\\Null\;Hypothesis --> H_0: \mu \ge \mu_0")
	print("\\\\Alternate\;Hypothesis --> H_1: \mu < \mu_0")
	print("Now, the value of test static can be found out by following formula: ")
	if n > 30:
		print("Z_0 = \\frac{\\bar{X} - \mu_0}{\sigma/\sqrt{n}}")
		print("Z_0 = \\frac{" + str(barx) + "-" + str(mean) + "}{" + str(sd) + "/" + str(n) + "}")
		zfinal = zvalue(barx, mean, sd, n)
		print("Z_0 = " + str(zfinal))
		if pval == 1:
			print("Since P-value of a upper tailed test is equal to \phi(|Z_0|)")
			print("P = \phi(" + str(zfinal) + ") ")
			pyperclip.copy(str(zfinal))
			webbrowser.open("https://www.easycalculation.com/statistics/p-value-for-z-score.php")
			forP = float(input())
			print("P = " + str(forP))
		crit = zs.get((alpha*2), 0)
		if crit == 0:
			crit = float(input("critical value = "))
		if zfinal < (-crit):
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are -Z_" + str(alpha*2) + " = -" + str(crit) + " and we note that Z_0 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the mean is not equal to " + str(mean))
		else:
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are -Z_" + str(alpha*2) + " = -" + str(crit) + " and we note that Z_0 does not falls in the critical region. Therefore, we fail to reject H_0.")
	else:
		print("t_0 = \\frac{\\bar{X} - \mu_0}{S/\sqrt{n}}")
		print("t_0 = \\frac{" + str(barx) + "- " + str(mean) + "}{" + str(sd) + "/\sqrt{" + str(n) + "}}")
		zfinal = zvalue(barx, mean, sd, n)
		print("t_0 = " + str(zfinal))
		pyperclip.copy(str(alpha))
		webbrowser.open('https://www.danielsoper.com/statcalc/calculator.aspx?id=10')
		crit = float(input("critical value(t_{\\alpha, n-1}) = "))
		if zfinal < (-crit):
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are -t_{" + str(alpha*2) + ", " + str(n-1) + " = -" + str(crit) + " and we note that Z_0 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the mean is not equal to " + str(mean))
		else:
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are -t_{" + str(alpha*2) + ", " + str(n-1) + " = -" + str(crit) + " and we note that Z_0 does not falls in the critical region. Therefore, we fail to reject H_0.")
elif type1 == 3:
	type2 = int(input("1. Null Hypothesis =\n2. Null Hypophesis \le"))
	print("We are interested in testing the hypothesis")
	if type2 == 1:
		print("\\\\Null\;Hypothesis --> H_0: \mu = \mu_0")
	elif type2 ==2:
		print("\\\\Null\;Hypothesis --> H_0: \mu \le \mu_0")
	print("\\\\Alternate\;Hypothesis --> H_1: \mu > \mu_0")
	print("Now, the value of test static can be found out by following formula: ")
	if n > 30:
		print("Z_0 = \\frac{\\bar{X} - \mu_0}{\sigma/\sqrt{n}}")
		print("Z_0 = \\frac{" + str(barx) + "-" + str(mean) + "}{" + str(sd) + "/" + str(n) + "}")
		zfinal = zvalue(barx, mean, sd, n)
		print("Z_0 = " + str(zfinal))
		if pval == 1:
			print("Since P-value of a upper tailed test is equal to (1 - \phi(|Z_0|)")
			print("P = 1 - \phi(" + str(zfinal) + ") ")
			pyperclip.copy(str(zfinal))
			webbrowser.open("https://www.easycalculation.com/statistics/p-value-for-z-score.php")
			forP = float(input())
			print("P = 1 - " + str(forP))
			print("P = " + str(round(1 - forP, 4)))
		crit = zs.get(alpha*2, 0)
		if crit == 0:
			crit = float(input("critical value = "))
		if zfinal > crit :
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are Z_" + str(alpha*2) + " = -" + str(crit) + " and we note that Z_0 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the mean is not equal to " + str(mean))
		else:
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are Z_" + str(alpha*2) + " = -" + str(crit) + " and we note that Z_0 does not falls in the critical region. Therefore, we fail to reject H_0.")
	else:
		print("t_0 = \\frac{\\bar{X} - \mu_0}{S/\sqrt{n}}")
		print("t_0 = \\frac{" + str(barx) + "- " + str(mean) + "}{" + str(sd) + "/\sqrt{" + str(n) + "}}")
		zfinal = zvalue(barx, mean, sd, n)
		print("t_0 = " + str(zfinal))
		pyperclip.copy(str(alpha))
		webbrowser.open('https://www.danielsoper.com/statcalc/calculator.aspx?id=10')
		crit = float(input("critical value(t_{\\alpha, n-1}) = "))
		if zfinal > (crit):
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are t_{" + str(alpha*2) + ", " + str(n-1) + " = -" + str(crit) + " and we note that Z_0 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the mean is not equal to " + str(mean))
		else:
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are t_{" + str(alpha*2) + ", " + str(n-1) + " = -" + str(crit) + " and we note that Z_0 does not falls in the critical region. Therefore, we fail to reject H_0.")
elif type1 == 4:
	print("We are interested in testing the hypothesis")
	print("\\\\Null\;Hypothesis --> H_0: \mu_1 = \mu_2")
	print("\\\\Alternate\;Hypothesis --> H_1: \mu_1 \\ne \mu_2")
	print("Now, the value of test static can be found out by following formula: ")
	print("\\\\Z_0 = \\frac{\\bar{X_1} - \\bar{X_2}}{\sqrt{\\frac{\sigma_1^2}{n_1} + \\frac{\sigma_2^2}{n_2}}}")
	print("\\\\Z_0 = \\frac{" + str(barx1) + "-" + str(barx2) + "}{\sqrt{\\frac{" + str(var1) + "^2}{" + str(n1) + "}}} + \\frac{" + str(var2) + "^2}{" + str(n2) +"}")
	zfinal = zfor2(barx1, barx2, var1, var2, n1, n2)
	print("Z_0 = " + str(zfinal))
	if pval == 1:
		print("Since P-value of a two tailed test is equal to 2(1 - \phi(|Z_0|)")
		print("P = 2(1 - \phi(" + str(zfinal) + ")) ")
		pyperclip.copy(str(zfinal))
		webbrowser.open("https://www.easycalculation.com/statistics/p-value-for-z-score.php")
		forP = float(input())
		print("P = 2(1 - " + str(forP) + ") ")
		print("P = " + str(round(2 * (1 - forP), 4)))
	crit = zs.get(alpha, 0)
	if crit == 0:
		crit = float(input("critical value = "))
	if zfinal > crit or zfinal < (-crit):
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are Z_" + str(alpha) + " = " + str(crit) + " and -Z_" + str(alpha) + " = -" + str(crit) + " and we note that Z_0 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the means are not equal")
	else:
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are Z_" + str(alpha) + " = " + str(crit) + " and -Z_" + str(alpha) + " = -" + str(crit) + " and we note that Z_0 does not falls in the critical region. Therefore, we fail to reject H_0.")
'''	else:
		print("t_0 = \\frac{\\bar{X_1} - \\bar{X_2}}{S_p\sqrt{\\frac{1}{n_1} + \\frac{1}{n_2}}}")
		print("Where")
		print("S_p^2 = \\frac{(n_1-1)s_1^2}{n_1 + n_2 - 2}")
		print("t_0 = \\frac{" + str(barx) + "- " + str(mean) + "}{" + str(sd) + "/\sqrt{" + str(n) + "}}")
		zfinal = zvalue(barx, mean, sd, n)
		print("t_0 = " + str(zfinal))
		pyperclip.copy(str(alpha))
		webbrowser.open('https://www.danielsoper.com/statcalc/calculator.aspx?id=10')
		crit = float(input("critical value(t_{\\alpha/2, n-1}) = "))
		if zfinal > crit or zfinal < (-crit):
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are t_{" + str(alpha) + ", " + str(n-1) + "} = " + str(crit) + " and -t_{" + str(alpha) + ", " + str(n-1) " = -" + str(crit) + " and we note that Z_0 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the mean is not equal to " + str(mean))
		else:
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are t_{" + str(alpha) + ", " + str(n-1) + " = " + str(crit) + " and -t_{" + str(alpha) + ", " + str(n-1) " = -" + str(crit) + " and we note that Z_0 does not falls in the critical region. Therefore, we fail to reject H_0.")

elif type1 == 5:
	type2 = int(input("1. Null Hypothesis =\n2. Null Hypophesis \ge"))
	print("We are interested in testing the hypothesis")
	if type2 == 1:
		print("\\\\Null\;Hypothesis --> H_0: \mu_1 = \mu_2")
	elif type2 ==2:
		print("\\\\Null\;Hypothesis --> H_0: \mu_1 \ge \mu_2")
	print("\\\\Alternate\;Hypothesis --> H_1: \mu_1 < \mu_2")
	print("Now, the value of test static can be found out by following formula: ")
	print("Z_0 = \\frac{\\bar{X_1} - \\bar{X_2}}{\sqrt{\\frac{\sigma_1^2}{n_1} + \\frac{\sigma_2^2}{n_2}}}")
	print("Z_0 = \\frac{" + str(barx1) + "-" + str(barx2) + "}{\sqrt{\\frac{" + str(var1) + "^2}{" + str(n1) + "} + \\frac{" + str(var2) + "^2}{" + str(n2) +"}")
	zfinal = zfor2(barx1, barx2, var1, var2, n1, n2)
	print("Z_0 = " + str(zfinal))
	if pval == 1:
		print("Since P-value of a upper tailed test is equal to \phi(|Z_0|)")
		print("P = \phi(" + str(zfinal) + ") ")
		pyperclip.copy(str(zfinal))
		webbrowser.open("https://www.easycalculation.com/statistics/p-value-for-z-score.php")
		forP = float(input())
		print("P = " + str(forP))
	crit = zs.get((alpha*2), 0)
	if crit == 0:
		crit = float(input("critical value = "))
	if zfinal < (-crit):
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are -Z_" + str(alpha*2) + " = -" + str(crit) + " and we note that Z_0 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the mean is not equal to " + str(mean))
	else:
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are -Z_" + str(alpha*2) + " = -" + str(crit) + " and we note that Z_0 does not falls in the critical region. Therefore, we fail to reject H_0.")
elif type1 == 6:
	type2 = int(input("1. Null Hypothesis =\n2. Null Hypophesis \le"))
	print("We are interested in testing the hypothesis")
	if type2 == 1:
		print("\\\\Null\;Hypothesis --> H_0: \mu_1 = \mu_2")
	elif type2 ==2:
		print("\\\\Null\;Hypothesis --> H_0: \mu_1 \le \mu_2")
	print("\\\\Alternate\;Hypothesis --> H_1: \mu_1 > \mu_2")
	print("Now, the value of test static can be found out by following formula: ")
	print("Z_0 = \\frac{\\bar{X_1} - \\bar{X_2}}{\sqrt{\\frac{\sigma_1^2}{n_1} + \\frac{\sigma_2^2}{n_2}}}")
	print("Z_0 = \\frac{" + str(barx1) + "-" + str(barx2) + "}{\sqrt{\\frac{" + str(var1) + "^2}{" + str(n1) + "} + \\frac{" + str(var2) + "^2}{" + str(n2) +"}")
	zfinal = zfor2(barx1, barx2, var1, var2, n1, n2)
	print("Z_0 = " + str(zfinal))
	if pval == 1:
		print("Since P-value of a upper tailed test is equal to (1 - \phi(|Z_0|)")
		print("P = 1 - \phi(" + str(zfinal) + ") ")
		pyperclip.copy(str(zfinal))
		webbrowser.open("https://www.easycalculation.com/statistics/p-value-for-z-score.php")
		forP = float(input())
		print("P = 1 - " + str(forP))
		print("P = " + str(round(1 - forP, 4)))
	crit = zs.get(alpha*2, 0)
	if crit == 0:
		crit = float(input("critical value = "))
	if zfinal > crit :
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are Z_" + str(alpha*2) + " = -" + str(crit) + " and we note that Z_0 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the mean is not equal to " + str(mean))
	else:
		print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are Z_" + str(alpha*2) + " = -" + str(crit) + " and we note that Z_0 does not falls in the critical region. Therefore, we fail to reject H_0.")
'''
