import webbrowser, time, math
import scipy.stats as st

def zvalue(x, p, n):
	return round((x - (n * p))/(math.sqrt(n*p*(1-p))), 4)
def zvalueproportion(p, p0, n):
	return round((p - p0)/((p0*(1-p0)/n)**0.5), 4)
def get_p_hat_two_proportion(x1, x2,n1,n2):
	return round((x1+x2)/(n1+n2), 4)
def get_test_static_two_proportion(p1, p2, hatP, n1, n2):
	return round((p1-p2)/math.sqrt(hatP*(1-hatP)*((1/n1)+(1/n2))),4)

print("1. Alternative hypothesis \\neq\n2. Alternative hypothesis < (not fully tested)\n3. Alternative hypothesis >")
print("4. For 2 distributions alternative hypothesis \\neq\n5. For 2 distributions alternative hypothesis <\n6. For 2 distributions alternative hypothesis >")
pval = int(input("Need to calculate P value also? Press 1 for yes: "))
type1 = int(input("Mention the type as legend: "))
proportionOrNumber = int(input("Give 1. proportion or 2. number of event"))
if type1<4:
	p0 = float(input("\\\\Proportion (p_0) = "))
	if proportionOrNumber == 1:
		p = float(input("\\\\\\hat p = "))
		n = int(input("Total number of sample (n) = "))
	elif proportionOrNumber == 2:
		n = int(input("Total number of sample (n) = "))
		x = int(input("number of favourable events (X) = "))
		p = round(x/n, 4)
		print(f"\\hat p = X/n = {x}/{n} = {p}")
else:
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


alpha = round(float(input("\\\\\\alpha = ")) / 2, 4)

print("We are interested in testing the hypothesis")
if type1 == 1:
	print("\\\\\\text{Null Hypothesis }--> H_0: p = p_0")
	print("\\\\\\text{Alternate Hypothesis }--> H_1: p \\ne p_0")
	if proportionOrNumber == 2:
		print("\\\\Z_0 = \\frac{X - np_0}{\\sqrt{np_0(1-p_0)}}")
		print(f"\\\\Z_0 = \\frac{{{x}-{n}*{p0}}}{{\\sqrt{{{n}*{p0}(1-{p0})}}}}")
		print(f"\\\\Z_0 = \\frac{{{x}-{n*p0}}}{{\\sqrt{{{n*p0}({1-p0})}}}}")
		print(f"\\\\Z_0 = \\frac{{{round(x-(n*p0), 4)}}}{{\\sqrt{{{n*p0}({1-p0})}}}}")
		print(f"\\\\Z_0 = \\frac{{{round(x-(n*p0), 4)}}}{{{round((n*p0*(1-p0))**0.5, 4)}}}")
		zfinal = zvalue(x, p0, n)
		print(f"\\\\Z_0 = {zfinal}")
	elif proportionOrNumber == 1:
		print("\\\\Z_0 = \\frac{p - p_0}{\\sqrt{\\frac{p_0(1-p_0)}{n}}}")
		print(f"\\\\Z_0 = \\frac{{{p} - {p0}}}{{\\sqrt{{\\frac{{{p0}(1-{p0})}}{{{n}}}}}}}")
		print(f"\\\\Z_0 = \\frac{{{p - p0}}}{{\\sqrt{{\\frac{{{p0}({1-p0})}}{{{n}}}}}}}")
		print(f"\\\\Z_0 = \\frac{{{p - p0}}}{{\\sqrt{{\\frac{{{round(p0*(1-p0), 4)}}}{{{n}}}}}}}")
		print(f"\\\\Z_0 = \\frac{{{p - p0}}}{{\\sqrt{{{round((p0*(1-p0))/n, 4)}}}}}")
		zfinal = zvalueproportion(p, p0, n)
		print(f"\\\\Z_0 = {zfinal}")
	if pval == 1:
		print("Since P-value of a two tailed test is equal to 2(\\phi(-|Z_0|))")
		print(f"P = 2(\\phi(-{abs(zfinal)}))")
		forP = st.norm.cdf(-abs(zfinal))
		print(f"P = 2({forP})")
		print(f"P = {round(2 * (forP), 4)}")
	print(f"\\\\\\text{{Since, the test is two-tail test at }}\\alpha = {alpha * 2}")
	print(f"\\\\z_{{\\alpha/2}} = z_{{{alpha * 2}/2}} = z_{{{alpha}}}")
	print(f"\\\\z_{{\\alpha/2}} = \\pm {st.norm.ppf(1-alpha)}")
	crit = st.norm.ppf(1-alpha)
	print(f"\\\\\\text{{Rejection Region: }}z_0 > z_{{\\alpha/2}}\\text{{  or  }}z_0 < -z_{{\\alpha/2}}")
	print(f"Decision Rule: Reject the null hypothesis if the test statistic value is less than the critical value -{crit} or greater than the critical value {crit}")
	if zfinal > crit:
		print(f"The statistic value, {zfinal} is greater than the critical value {crit}. Hence, reject the null hypothesis.")
	elif zfinal < -crit:
		print(f"The statistic value, {zfinal} is less than the critical value -{crit}. Hence, reject the null hypothesis.")
	else:
		print(f"The statistic value, {zfinal} is between the critical values -{crit} and {crit}. Therefore, we fail to reject the null hypothesis.")
if type1 == 2:
	print("\\\\\\text{Null Hypothesis }--> H_0: p = p_0")
	print("\\\\\\text{Alternate Hypothesis }--> H_1: p < p_0")
	if proportionOrNumber == 2:
		print("\\\\Z_0 = \\frac{X - np_0}{\\sqrt{np_0(1-p_0)}}")
		print(f"\\\\Z_0 = \\frac{{{x}-{n}*{p0}}}{{\\sqrt{{{n}*{p0}(1-{p0})}}}}")
		print(f"\\\\Z_0 = \\frac{{{x}-{n*p0}}}{{\\sqrt{{{n*p0}({1-p0})}}}}")
		print(f"\\\\Z_0 = \\frac{{{round(x-(n*p0), 4)}}}{{\\sqrt{{{n*p0}({1-p0})}}}}")
		print(f"\\\\Z_0 = \\frac{{{round(x-(n*p0), 4)}}}{{{round((n*p0*(1-p0))**0.5, 4)}}}")
		zfinal = zvalue(x, p0, n)
		print(f"\\\\Z_0 = {zfinal}")
	elif proportionOrNumber == 1:
		print("\\\\Z_0 = \\frac{p - p_0}{\\sqrt{\\frac{p_0(1-p_0)}{n}}}")
		print(f"\\\\Z_0 = \\frac{{{p} - {p0}}}{{\\sqrt{{\\frac{{{p0}(1-{p0})}}{{{n}}}}}}}")
		print(f"\\\\Z_0 = \\frac{{{p - p0}}}{{\\sqrt{{\\frac{{{p0}({1-p0})}}{{{n}}}}}}}")
		print(f"\\\\Z_0 = \\frac{{{p - p0}}}{{\\sqrt{{\\frac{{{round(p0*(1-p0), 4)}}}{{{n}}}}}}}")
		print(f"\\\\Z_0 = \\frac{{{p - p0}}}{{\\sqrt{{{round((p0*(1-p0))/n, 4)}}}}}")
		zfinal = zvalueproportion(p, p0, n)
		print(f"\\\\Z_0 = {zfinal}")
	if pval == 1:
		print("Since P-value of a two tailed test is equal to (\\phi(Z_0))")
		print("P = (\\phi(" + str(zfinal) + ")) ")
		forP = st.norm.cdf(zfinal)
		print("P = (" + str(forP) + ") ")
		print("P = " + str(round((forP), 4)))
		if forP < alpha *2:
			print(f"Here, the P-value is less than the level of significance {alpha * 2}; reject the null hypothesis")
		else:
			print(f"Here, the P-value is greater than the level of significance {alpha * 2}; Fail to reject the null hypothesis")
	print(f"\\\\\\text{{Since, the test is two-tail test at }}\\alpha = {alpha * 2}")
	print(f"\\\\z_{{\\alpha/2}} = z_{{{alpha * 2}/2}} = z_{{{alpha}}}")
	print(f"\\\\z_{{\\alpha/2}} = {st.norm.ppf(1-alpha)}")
	crit = st.norm.ppf(1-(alpha*2))
	print(f"\\\\\\text{{Rejection Region: }}z_0 < -z_{{\\alpha}}")
	print(f"Decision Rule: Reject the null hypothesis if the test statistic value is less than the critical value -{crit} or greater than the critical value {crit}")
	if zfinal < -crit:
		print(f"The statistic value, {zfinal} is less than the critical value -{crit}. Hence, reject the null hypothesis.")
	else:
		print(f"The statistic value, {zfinal} is greater than the critical values -{crit} . Therefore, we fail to reject the null hypothesis.")
if type1 == 3:
	print("\\\\\\text{Null Hypothesis }--> H_0: p = p_0")
	print("\\\\\\text{Alternate Hypothesis }--> H_1: p > p_0")
	if proportionOrNumber == 2:
		print("\\\\Z_0 = \\frac{X - np_0}{\\sqrt{np_0(1-p_0)}}")
		print(f"\\\\Z_0 = \\frac{{{x}-{n}*{p0}}}{{\\sqrt{{{n}*{p0}(1-{p0})}}}}")
		print(f"\\\\Z_0 = \\frac{{{x}-{n*p0}}}{{\\sqrt{{{n*p0}({1-p0})}}}}")
		print(f"\\\\Z_0 = \\frac{{{round(x-(n*p0), 4)}}}{{\\sqrt{{{n*p0}({1-p0})}}}}")
		print(f"\\\\Z_0 = \\frac{{{round(x-(n*p0), 4)}}}{{{round((n*p0*(1-p0))**0.5, 4)}}}")
		zfinal = zvalue(x, p0, n)
		print(f"\\\\Z_0 = {zfinal}")
	elif proportionOrNumber == 1:
		print("\\\\Z_0 = \\frac{p - p_0}{\\sqrt{\\frac{p_0(1-p_0)}{n}}}")
		print(f"\\\\Z_0 = \\frac{{{p} - {p0}}}{{\\sqrt{{\\frac{{{p0}(1-{p0})}}{{{n}}}}}}}")
		print(f"\\\\Z_0 = \\frac{{{p - p0}}}{{\\sqrt{{\\frac{{{p0}({1-p0})}}{{{n}}}}}}}")
		print(f"\\\\Z_0 = \\frac{{{p - p0}}}{{\\sqrt{{\\frac{{{round(p0*(1-p0), 4)}}}{{{n}}}}}}}")
		print(f"\\\\Z_0 = \\frac{{{p - p0}}}{{\\sqrt{{{round((p0*(1-p0))/n, 4)}}}}}")
		zfinal = zvalueproportion(p, p0, n)
		print(f"\\\\Z_0 = {zfinal}")
	if pval == 1:
		print("Since P-value of a two tailed test is equal to 1-\\phi(Z_0)")
		print("P = (1-\\phi(" + str(abs(zfinal)) + ")) ")
		forP = st.norm.cdf(zfinal)
		print("P = (1-" + str(forP) + ") ")
		print("P = " + str(1-round((forP), 4)))
	print(f"\\\\\\text{{Since, the test is two-tail test at }}\\alpha = {alpha * 2}")
	print(f"\\\\z_{{\\alpha/2}} = z_{{{alpha * 2}/2}} = z_{{{alpha}}}")
	print(f"\\\\z_{{\\alpha/2}} = {st.norm.ppf(1-(alpha*2))}")
	crit = st.norm.ppf(1-(alpha*2))
	print(f"\\\\\\text{{Rejection Region: }}z_0 > z_{{\\alpha}}")
	print(f"Decision Rule: Reject the null hypothesis if the test statistic value is greater than the critical value {crit}")
	if zfinal > crit:
		print(f"The statistic value, {zfinal} is greater than the critical value {crit}. Hence, reject the null hypothesis.")
	else:
		print(f"The statistic value, {zfinal} is less than the critical values  {crit}. Therefore, we fail to reject the null hypothesis.")
if type1 == 4:
	print("\\\\\\text{Null Hypothesis }--> H_0: p_1 = p_2")
	print("\\\\\\text{Alternate Hypothesis }--> H_1: p_1 \\ne p_2")
	if proportionOrNumber == 2:
		print(f"\\\\\\hat P = \\frac{{X_1+X_2}}{{n_1+n_2}}")
		print(f"\\\\\\hat P = \\frac{{{x1}+{x2}}}{{{n1}+{n2}}}")
		print(f"\\\\\\hat P = \\frac{{{x1+x2}}}{{{n1+n2}}}")
		hatP = get_p_hat_two_proportion(x1, x2,n1,n2)
		print(f"\\\\\\hat P = {hatP}")
		print(f"\\\\Z_0 = \\frac{{\\hat P_1 - \\hat P_2}}{{\\sqrt{{\\hat P(1-\\hat P)\\left(\\frac{{1}}{{n_1}} + \\frac{{1}}{{n_2}}\\right)}}}}")
		print(f"\\\\Z_0 = \\frac{{{p1} - {p2}}}{{\\sqrt{{{hatP}(1-{hatP})\\left(\\frac{{1}}{{{n1}}} + \\frac{{1}}{{{n2}}}\\right)}}}}")
		print(f"\\\\Z_0 = \\frac{{{p1 - p2}}}{{\\sqrt{{{hatP}({1-hatP})({1/n1}+{1/n2})}}}}")
		print(f"\\\\Z_0 = \\frac{{{p1 - p2}}}{{\\sqrt{{{hatP*(1-hatP)*((1/n1)+(1/n2))}}}}}")
		zfinal = get_test_static_two_proportion(p1, p2, hatP, n1, n2)
		print(f"\\\\Z_0 = {zfinal}")

	if pval == 1:
		print("Since P-value of a two tailed test is equal to 2(\\phi(-|Z_0|)")
		print("P = 2(\\phi(-" + str(abs(zfinal)) + ")) ")
		forP = st.norm.cdf(-abs(zfinal))
		print("P = 2(" + str(forP) + ") ")
		print("P = " + str(round(2 * (forP), 4)))
	print(f"\\\\\\text{{Since, the test is two-tail test at }}\\alpha = {alpha * 2}")
	print(f"\\\\z_{{\\alpha/2}} = z_{{{alpha * 2}/2}} = z_{{{alpha}}}")
	print(f"\\\\z_{{\\alpha/2}} = \\pm {st.norm.ppf(1-alpha)}")
	crit = st.norm.ppf(1-(alpha*2))
	print(f"\\\\\\text{{Rejection Region: }}z_0 > z_{{\\alpha/2}}\\text{{  or  }}z_0 < -z_{{\\alpha/2}}")
	print(f"Decision Rule: Reject the null hypothesis if the test statistic value is less than the critical value -{crit} or greater than the critical value {crit}")
	if zfinal > crit:
		print(f"The statistic value, {zfinal} is greater than the critical value {crit}. Hence, reject the null hypothesis.")
	elif zfinal < -crit:
		print(f"The statistic value, {zfinal} is less than the critical value -{crit}. Hence, reject the null hypothesis.")
	else:
		print(f"The statistic value, {zfinal} is between the critical values -{crit} and {crit}. Therefore, we fail to reject the null hypothesis.")
if type1 == 5:
	print("\\\\\\text{Null Hypothesis }--> H_0: p_1 = p_2")
	print("\\\\\\text{Alternate Hypothesis }--> H_1: p_1 < p_2")
	print(f"\\\\\\hat P = \\frac{{X_1+X_2}}{{n_1+n_2}}")
	print(f"\\\\\\hat P = \\frac{{{x1}+{x2}}}{{{n1}+{n2}}}")
	print(f"\\\\\\hat P = \\frac{{{x1+x2}}}{{{n1+n2}}}")
	hatP = get_p_hat_two_proportion(x1, x2,n1,n2)
	print(f"\\\\\\hat P = {hatP}")
	print(f"\\\\Z_0 = \\frac{{\\hat P_1 - \\hat P_2}}{{\\sqrt{{\\hat P(1-\\hat P)\\left(\\frac{{1}}{{n_1}} + \\frac{{1}}{{n_2}}\\right)}}}}")
	print(f"\\\\Z_0 = \\frac{{{p1} - {p2}}}{{\\sqrt{{{hatP}(1-{hatP})\\left(\\frac{{1}}{{{n1}}} + \\frac{{1}}{{{n2}}}\\right)}}}}")
	print(f"\\\\Z_0 = \\frac{{{p1 - p2}}}{{\\sqrt{{{hatP}({1-hatP})({1/n1}+{1/n2})}}}}")
	print(f"\\\\Z_0 = \\frac{{{p1 - p2}}}{{\\sqrt{{{hatP*(1-hatP)*((1/n1)+(1/n2))}}}}}")
	zfinal = get_test_static_two_proportion(p1, p2, hatP, n1, n2)
	print("\\\\Z_0 = " + str(zfinal))
	if pval == 1:
		print("Since P-value of a two tailed test is equal to (\\phi(Z_0)")
		print("P = (\\phi(" + str(zfinal) + ")) ")
		forP = st.norm.cdf(zfinal)
		print("P = (" + str(forP) + ") ")
		print("P = " + str(round((forP), 4)))
		if forP < alpha *2:
			print(f"Here, the P-value is less than the level of significance {alpha * 2}; reject the null hypothesis")
		else:
			print(f"Here, the P-value is greater than the level of significance {alpha * 2}; Fail to reject the null hypothesis")
	print(f"\\\\z_{{\\alpha/2}} = z_{{{alpha * 2}/2}} = z_{{{alpha}}}")
	print(f"\\\\z_{{\\alpha/2}} = {st.norm.ppf(1-alpha)}")
	crit = st.norm.ppf(1-(alpha*2))
	print(f"\\\\\\text{{Rejection Region: }}z_0 < -z_{{\\alpha}}")
	print(f"Decision Rule: Reject the null hypothesis if the test statistic value is less than the critical value -{crit} or greater than the critical value {crit}")
	if zfinal < -crit:
		print(f"The statistic value, {zfinal} is less than the critical value -{crit}. Hence, reject the null hypothesis.")
	else:
		print(f"The statistic value, {zfinal} is greater than the critical values -{crit} . Therefore, we fail to reject the null hypothesis.")
if type1 == 6:
	print("\\\\\\text{Null Hypothesis }--> H_0: p_1 = p_2")
	print("\\\\\\text{Alternate Hypothesis }--> H_1: p_1 > p_2")
	print(f"\\\\\\hat P = \\frac{{X_1+X_2}}{{n_1+n_2}}")
	print(f"\\\\\\hat P = \\frac{{{x1}+{x2}}}{{{n1}+{n2}}}")
	print(f"\\\\\\hat P = \\frac{{{x1+x2}}}{{{n1+n2}}}")
	hatP = get_p_hat_two_proportion(x1, x2,n1,n2)
	print(f"\\\\\\hat P = {hatP}")
	print(f"\\\\Z_0 = \\frac{{\\hat P_1 - \\hat P_2}}{{\\sqrt{{\\hat P(1-\\hat P)\\left(\\frac{{1}}{{n_1}} + \\frac{{1}}{{n_2}}\\right)}}}}")
	print(f"\\\\Z_0 = \\frac{{{p1} - {p2}}}{{\\sqrt{{{hatP}(1-{hatP})\\left(\\frac{{1}}{{{n1}}} + \\frac{{1}}{{{n2}}}\\right)}}}}")
	print(f"\\\\Z_0 = \\frac{{{p1 - p2}}}{{\\sqrt{{{hatP}({1-hatP})({1/n1}+{1/n2})}}}}")
	print(f"\\\\Z_0 = \\frac{{{p1 - p2}}}{{\\sqrt{{{hatP*(1-hatP)*((1/n1)+(1/n2))}}}}}")
	zfinal = get_test_static_two_proportion(p1, p2, hatP, n1, n2)
	print("\\\\Z_0 = " + str(zfinal))
	if pval == 1:
		print("Since P-value of a two tailed test is equal to 1-\\phi(Z_0)")
		print("P = (1-\\phi(" + str(abs(zfinal)) + ")) ")
		forP = st.norm.cdf(zfinal)
		print("P = (1-" + str(forP) + ") ")
		print("P = " + str(1-round((forP), 4)))
	print(f"\\\\z_{{\\alpha/2}} = z_{{{alpha * 2}/2}} = z_{{{alpha}}}")
	print(f"\\\\z_{{\\alpha/2}} = {st.norm.ppf(1-(alpha*2))}")
	crit = st.norm.ppf(1-(alpha*2))
	print(f"\\\\\\text{{Rejection Region: }}z_0 > z_{{\\alpha}}")
	print(f"Decision Rule: Reject the null hypothesis if the test statistic value is greater than the critical value {crit}")
	if zfinal > crit:
		print(f"The statistic value, {zfinal} is greater than the critical value {crit}. Hence, reject the null hypothesis.")
	else:
		print(f"The statistic value, {zfinal} is less than the critical values  {crit}. Therefore, we fail to reject the null hypothesis.")
