import webbrowser, pyperclip, time, math
def zvalue(x, p, n):
	return round((x - (n * p))/(math.sqrt(n*p*(1-p))), 4)
	
zs = dict([(0.15, 1.04), (0.125, 1.15), (0.1, 1.282), (0.075, 1.44), (0.05, 1.645), (0.04, 1.75), (0.025, 1.96), (0.02, 2.05), (0.01, 2.33), (0.005, 2.576), (0.0025, 2.807), (0.0005, 3.291)])
pval = int(input("Need to calculate P value also? Press 1 for yes: "))
p = float(input("Proportion (p_0) = "))
n = int(input("Sample size(n) = "))
x = float(input("X = "))
alpha = round(float(input("\\alpha = ")) / 2, 4)

print("We are interested in testing the hypothesis")
print("\\\\Null\;Hypothesis --> H_0: p = p_0")
print("\\\\Alternate\;Hypothesis --> H_1: p \\ne p_0")
print("Now, the value of test static van be found out by following formula: ")
print("Z_0 = \\frac{X - np_0}{\sqrt{np_0(1-p_0)}}")
print("Z_0 = \\frac{" + str(x) + "-" + str(n) + "." + str(p) + "}{\sqrt{" + str(n) + "." + str(p) + "(1-" + str(p) + ")}}")
zfinal = zvalue(x, p, n)
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
	print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are Z_" + str(alpha) + " = " + str(crit) + " and -Z_" + str(alpha) + " = -" + str(crit) + " and we note that Z_0 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the proportion is not equal to " + str(p))
else:
	print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are Z_" + str(alpha) + " = " + str(crit) + " and -Z_" + str(alpha) + " = -" + str(crit) + " and we note that Z_0 does not falls in the critical region. Therefore, we fail to reject H_0.")
