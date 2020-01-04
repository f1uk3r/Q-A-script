import math, webbrowser
import scipy.stats as st

def calChi(s, sd, n):
	return round(((n-1) * (s)) / (sd), 4)

def calF(s1, s2):
	return round(s1/s2, 4)
print("1. Alternative hypothesis \\neq\n2. Alternative hypothesis <\n3. Alternative hypothesis >")
print("4. For 2 distributions alternative hypothesis \\neq\n5. For 2 distributions alternative hypothesis <\n6. For 2 distributions alternative hypothesis >")
type1 = int(input("Mention the type as legend: "))
varOrSd = int(input("Given values of 1. Variance or 2. Standard deviation: "))
if type1 < 4:
	n = int(input("Sample Size (n) = "))
	if varOrSd == 1:
		sd = float(input("Variance \sigma_0^2 = "))
		s = float(input("Sample variance (S^2) = "))
	if varOrSd == 2:
		sdSquare = float(input("Standard Deviation \\sigma_0 = "))
		sSquare = float(input("Sample standard deviation (S) = "))
		sd = sdSquare**2
		s = sSquare**2
	alpha = round(float(input("\\alpha = ")) / 2, 4)
elif type1>3 and type1<7:
	if varOrSd == 1:
		var1 = float(input("\\\\Variance1(S_1^2) = "))
		var2 = float(input("\\\\Variance2(S_2^2) = "))
	elif varOrSd == 2:
		var1 = float(input("\\\\Standard\\; Deviation 1(S_1) = ")) ** 2
		var2 = float(input("\\\\Standard\\; Deviation 2(S_2) = ")) ** 2
	n1 = int(input("\\\\Sample\\;Size(n_1) = "))
	n2 = int(input("\\\\Sample\\;Size(n_2) = "))
	alpha = round(float(input("\\alpha = ")) / 2, 4)

if type1 == 1:
	print("We are interested in testing the hypothesis")
	print("\\\\Null\\;Hypothesis --> H_0: \\sigma^2 = \\sigma_0^2")
	print("\\\\Alternate\\;Hypothesis --> H_1: \\sigma^2 \\ne \\sigma_0^2")
	print("Now, the value of test static can be found out by following formula: ")
	print("\\\\\\chi_0^2 = \\frac{(n-1)S^2}{\\sigma_0^2}")
	print("\\\\\\chi_0^2 = \\frac{(" + str(n) + "-1)" + str(s) + "}{" + str(sd) + "}")
	cFinal = calChi(s, sd, n)
	print("\\\\\\chi_0^2 = " + str(cFinal))
	crit_1 = st.chi2.ppf(alpha,n-1)
	crit_2 = st.chi2.ppf(1-(alpha),n-1)
	print(f"\\chi_{{1-\\alpha/2, n-1}}^2 = {crit_1}")
	print(f"\\chi_{{\\alpha/2, n-1}}^2 = {crit_2}")
	print("Decision Rule: Reject the null hypothesis if, \\chi_0^2 > \\chi_{\\alpha/2, n-1} or \\chi_0^2 < \\chi_{1-\\alpha/2, n-1}; otherwise do not reject H0")
	print(f"The rejection region is \\chi_0^2 > {crit_2} or \\chi_0^2 < {crit_1}")
	if cFinal > crit_2:
		print(f"Since the test statistic value {cFinal} is greater than the critical value {crit_2}, so the test statistic value falls in critical region, so we reject the null hypothesis")
	elif cFinal < crit_1:
		print(f"Since the test statistic value {cFinal} is less than the critical value {crit_1}, so the test statistic value falls in critical region, so we reject the null hypothesis")
	else:
		print(f"Since the test statistic value {cFinal} is between {crit_1} and {crit_2}, so we fail to reject the null hypothesis.")

elif type1 == 2:
	type2 = int(input("1. Null Hypothesis =\n2. Null Hypophesis \\le"))
	print("We are interested in testing the hypothesis")
	if type2 == 1:
		print("\\\\Null\\;Hypothesis --> H_0: \\sigma^2 = \\sigma_0^2")
	else:
		print("\\\\Null\\;Hypothesis --> H_0: \\sigma^2 \\ge \\sigma_0^2")
	print("\\\\Alternate\\;Hypothesis --> H_1: \\sigma^2 < \\sigma_0^2")
	print("Now, the value of test static can be found out by following formula: ")
	print("\\\\\\chi_0^2 = \\frac{(n-1)S^2}{\\sigma_0^2}")
	print("\\\\\\chi_0^2 = \\frac{(" + str(n) + "-1)" + str(s) + "}{" + str(sd) + "}")
	cFinal = calChi(s, sd, n)
	print("\\\\\\chi_0^2 = " + str(cFinal))
	crit = st.chi2.ppf(alpha*2,n-1)
	print(f"\\\\\\chi_{{1-\\alpha, n-1}}^2 = {crit}")
	print("Decision Rule: Reject the null hypothesis if, \\chi_0^2 < \\chi_{1-\\alpha, n-1}; otherwise do not reject H0")
	print(f"The rejection region is \\chi_0^2 < {crit}")
	if cFinal < crit:
		print(f"Since the test statistic value {cFinal} is less than the critical value {crit}, so the test statistic value falls in critical region, so we reject the null hypothesis")
	else:
		print(f"Since the test statistic value {cFinal} is greater than the critical value {crit}, so fail to reject the null hypothesis.")

elif type1 == 3:
	type2 = int(input("1. Null Hypothesis =\n2. Null Hypophesis \\ge"))
	print("We are interested in testing the hypothesis")
	if type2 == 1:
		print("\\\\Null\;Hypothesis --> H_0: \\sigma^2 = \\sigma_0^2")
	else:
		print("\\\\Null\;Hypothesis --> H_0: \\sigma^2 /le \\sigma_0^2")
	print("\\\\Alternate\;Hypothesis --> H_1: \\sigma^2 > \\sigma_0^2")
	print("Now, the value of test static can be found out by following formula: ")
	print("\\\\\\chi_0^2 = \\frac{(n-1)S^2}{\\sigma_0^2}")
	print("\\\\\\chi_0^2 = \\frac{(" + str(n) + "-1)" + str(s) + "}{" + str(sd) + "}")
	cFinal = calChi(s, sd, n)
	print("\\\\\\chi_0^2 = " + str(cFinal))
	crit = st.chi2.ppf(1-(alpha*2),n-1)
	print(f"\\\\\\chi_{{\\alpha, n-1}}^2 = {crit}")
	print("Decision Rule: Reject the null hypothesis if, \\chi_0^2 > \\chi_{\\alpha, n-1}; otherwise do not reject H0")
	print(f"The rejection region is \\chi_0^2 > {crit}")
	if cFinal > crit:
		print(f"Since the test statistic value {cFinal} is greater than the critical value {crit}, so the test statistic value falls in critical region, so we reject the null hypothesis")
	else:
		print(f"Since the test statistic value {cFinal} is less than the critical value {crit}, so fail to reject the null hypothesis.")

if type1 == 4:
	print("We are interested in testing the hypothesis")
	print("\\\\Null\;Hypothesis --> H_0: \\sigma_1^2 = \\sigma_2^2")
	print("\\\\Alternate\\;Hypothesis --> H_1: \\sigma_1^2 \\ne \\sigma_2^2")
	print("Assuming normality of the sampled populations, the F-static is ")
	print("\\\\f_0 = \\frac{S_1^2}{S_2^2}")
	print(f"\\\\f_0 = \\frac{{{var1}}}{{{var2}}}")
	print(f"\\\\f_0 = {round(var1/var2, 6)}")
	fFinal = round(var1/var2, 4)
	print("from the table of Percentage Points of the F-distribution, we find that")
	crit_1 = st.f.ppf(alpha, n1-1, n2-1)
	crit_2 = st.f.ppf(1-alpha, n1-1, n2-1)
	print(f"\\\\f_{{1-\\alpha/2, n_1-1, n_2-1}} = \\\\f_{{{1-alpha}, {n1-1}, {n2-1}}} = {crit_1}")
	print(f"\\\\f_{{\\alpha/2, n_1-1, n_2-1}} = f_{{{alpha}, {n1-1}, {n2-1}}} = {crit_2}")
	print("Decision Rule: Reject the null hypothesis if, f_0 > f_{\\alpha/2, n_1-1,n_2-1} or f_0 < f_{1-\\alpha/2, n_1-1,n_2-1}; otherwise do not reject H0")
	print(f"The rejection region is f_0 > {crit_2} or f_0 < {crit_1}")
	if fFinal > crit_2:
		print(f"Since the test statistic value {fFinal} is greater than the critical value {crit_2}, so the test statistic value falls in critical region, so we reject the null hypothesis")
	elif fFinal < crit_1:
		print(f"Since the test statistic value {fFinal} is less than the critical value {crit_1}, so the test statistic value falls in critical region, so we reject the null hypothesis")
	else:
		print(f"Since the test statistic value {fFinal} is between {crit_1} and {crit_2}, so we fail to reject the null hypothesis.")

elif type1 == 5:
	type2 = int(input("1. Null Hypothesis =\n2. Null Hypophesis \\le"))
	print("We are interested in testing the hypothesis")
	if type2 == 1:
		print("\\\\Null\\;Hypothesis --> H_0: \\sigma_1^2 = \\sigma_2^2")
	else:
		print("\\\\Null\\;Hypothesis --> H_0: \\sigma_1^2 \\ge \\sigma_2^2")
	print("\\\\Alternate\\;Hypothesis --> H_1: \\sigma_1^2 < \\sigma_2^2")
	print("\\\\f_0 = \\frac{S_1^2}{S_2^2}")
	print(f"\\\\f_0 = \\frac{{{var1}}}{{{var2}}}")
	print(f"\\\\f_0 = {round(var1/var2, 6)}")
	fFinal = round(var1/var2, 4)
	print("from the table of Percentage Points of the F-distribution, we find that")
	crit = st.f.ppf(alpha*2, n1-1, n2-1)
	print(f"\\\\f_{{1-\\alpha, n_1-1, n_2-1}} = f_{{{1-(alpha*2)}, {n1-1}, {n2-1}}} = {crit}")
	print("Decision Rule: Reject the null hypothesis if, f_0 > f_{\\alpha/2, n_1-1,n_2-1} or f_0 < f_{1-\\alpha/2, n_1-1,n_2-1}; otherwise do not reject H0")
	print(f"The rejection region is f_0 < {crit}")
	if fFinal < crit:
		print(f"Since the test statistic value {fFinal} is less than the critical value {crit}, so the test statistic value falls in critical region, so we reject the null hypothesis")
	else:
		print(f"Since the test statistic value {fFinal} is greater than the critical value {crit}, so fail to reject the null hypothesis.")

elif type1 == 6:
	type2 = int(input("1. Null Hypothesis =\n2. Null Hypophesis \\ge"))
	print("We are interested in testing the hypothesis")
	if type2 == 1:
		print("\\\\Null\\;Hypothesis --> H_0: \\sigma^2 = \\sigma_0^2")
	else:
		print("\\\\Null\\;Hypothesis --> H_0: \\sigma^2 \\le \\sigma_0^2")
	print("\\\\Alternate\\;Hypothesis --> H_1: \\sigma^2 > \\sigma_0^2")
	print("\\\\f_0 = \\frac{S_1^2}{S_2^2}")
	print(f"\\\\f_0 = \\frac{{{var1}}}{{{var2}}}")
	print(f"\\\\f_0 = {round(var1/var2, 6)}")
	fFinal = round(var1/var2, 4)
	print("from the table of Percentage Points of the F-distribution, we find that")
	crit = st.f.ppf(1-(alpha*2), n1-1, n2-1)
	print(f"\\\\f_{{\\alpha, n_1-1, n_2-1}} = f_{{{alpha*2}, {n1-1}, {n2-1}}} = {crit}")
	print("Decision Rule: Reject the null hypothesis if, f_0 > f_{\\alpha, n_1-1,n_2-1}; otherwise do not reject H0")
	print(f"The rejection region is f_0 > {crit}")
	if fFinal > crit:
		print(f"Since the test statistic value {fFinal} is greater than the critical value {crit}, so the test statistic value falls in critical region, so we reject the null hypothesis")
	else:
		print(f"Since the test statistic value {fFinal} is less than the critical value {crit}, so fail to reject the null hypothesis.")
