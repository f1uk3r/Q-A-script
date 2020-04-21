import webbrowser, time, math
import scipy.stats as st
def zvalue(xbar, mean, sd, n):
	return round((xbar - mean)/(sd/math.sqrt(n)), 4)
	
def zfor2(x1, x2, s1, s2, n1, n2):
	return round((x1 - x2) / math.sqrt((s1/n1) + (s2/n2)), 4)

def varSq(s1, s2, n1, n2):
	return round((((n1 - 1) * s1) + ((n2 - 1) * s2)) / (n1 + n2 -2), 4)

def tvalue2(x1, x2, sp, n1, n2):
	return round((x1 - x2) / math.sqrt(sp * ((1/n1) + (1/n2))), 4)

def get_test_statistic_two_mean(barx1, barx2, delta0, var1, var2, n1, n2):
	return round((barx1 - barx2 - delta0)/math.sqrt((var1/n1)+(var2/n2)), 4)

def get_sp_square(var1, var2, n1, n2):
	return round((((n1-1)*var1)+((n2-1)*var2))/(n1+n2-2), 4)

def get_test_statistic_two_mean_unknown_var(barx1, barx2, delta0, sp, n1, n2):
	return round((barx1 - barx2 - delta0)/(sp*math.sqrt((1/n1)+(1/n2))), 4)

zs = dict([(0.15, 1.04), (0.125, 1.15), (0.1, 1.282), (0.075, 1.44), (0.05, 1.645), (0.04, 1.75), (0.025, 1.96), (0.02, 2.05), (0.01, 2.33), (0.005, 2.576), (0.0025, 2.807), (0.0005, 3.291)])
print("1. Alternative hypothesis \\neq\n2. Alternative hypothesis < (not fully tested)\n3. Alternative hypothesis >")
print("4. For two distributions Alternative hypothesis \\neq\n5. For two distributions Alternative hypothesis <\n6. For two distributions Alternative hypothesis >")
pval = int(input("Need to calculate P value also? Press 1 for yes: "))
type1 = int(input("Mention the type as legend: "))
var_type = int(input("1. Population variance or 2. Sample variance: "))


if type1 < 4:
	mean = float(input("\\mu_0 = "))
	n = int(input("n = "))
	if var_type == 1:
		sd = float(input("\\\\\\sigma = "))
	elif var_type == 2:
		sd = float(input("\\\\s = "))
	barx = float(input("\\\\\\bar{X} = "))
	alpha = round(float(input("\\\\\\alpha = ")) / 2, 4)
elif type1 > 3:
	type3 = int(input("Given value of standard deviations or variance? 1 for variance:"))
	type2 = int(input("Is actual mean given; i.e. mu1 and mu2; 1 for given:"))
	if type2 == 1:
		mean1 = float(input("\\\\\\mu_1 = "))
		mean2 = float(input("\\\\\\mu_2 = "))
		delta0 = mean1 - mean2
	else:
		delta0 = float(input("\\\\\\Delta_0 = "))
	barx1 = float(input("\\\\\\bar{X_1} = "))
	barx2 = float(input("\\\\\\bar{X_2} = "))
	if var_type == 1:
		if type3 == 1:
			var1 = float(input("\\\\\\sigma_1^2 = "))
			var2 = float(input("\\\\\\sigma_2^2 = "))
		else:
			sd1 = float(input("\\\\\\sigma_1 = "))
			sd2 = float(input("\\\\\\sigma_2 = "))
			var1 = sd1 ** 2
			var2 = sd2 ** 2
			print(f"\\\\\\sigma_1^2 = {var1}")
			print(f"\\\\\\sigma_2^2 = {var2}")
	if var_type == 2:
		if type3 == 1:
			var1 = float(input("\\\\\\S_1^2 = "))
			var2 = float(input("\\\\\\S_2^2 = "))
		else:
			sd1 = float(input("\\\\\\S_1 = "))
			sd2 = float(input("\\\\\\S_2 = "))
			var1 = sd1 ** 2
			var2 = sd2 ** 2startTimeEastern
			print(f"\\\\\\S_1^2 = {var1}")
			print(f"\\\\\\S_2^2 = {var2}")
	n1 = int(input("\\\\n_1 = "))
	n2 = int(input("\\\\n_2 = "))
	alpha = round(float(input("\\\\\\alpha = ")) / 2, 4)
	

if type1 == 1:
	print("The test hypothesis is")
	print("\\\\Null\\;Hypothesis --> H_0: \\mu = \\mu_0")
	print("\\\\Alternate\\;Hypothesis --> H_1: \\mu \\ne \\mu_0")
	print("This is a two-sided test because the alternative hypothesis is formulated to detect differences from the hypothesized mean value of 30 on either side.")
	print("Now, the value of test static can be found out by following formula: ")
	if var_type == 1:
		print("\\\\Z_0 = \\frac{\\bar{X} - \\mu_0}{\\sigma/\\sqrt{n}}")
		print("\\\\Z_0 = \\frac{" + str(barx) + "-" + str(mean) + "}{" + str(sd) + "/\\sqrt{" + str(n) + "}}")
		zfinal = zvalue(barx, mean, sd, n)
		print("\\\\Z_0 = " + str(zfinal))
		if pval == 1:
			print("Since P-value of a two tailed test is equal to 2(1 - \\phi(|Z_0|)")
			print(f"P = 2(1 - \\phi({abs(zfinal)}))")
			print(f"P = 2(1 - {st.norm.cdf(zfinal)})")
			print(f"P = {round(2 * (1 - st.norm.cdf(zfinal)), 6)}")
			crit = 2 * (1 - st.norm.cdf(zfinal))
			if crit < alpha * 2:
				print(f"Suppose that the significance level \\alpha is specified to be {alpha*2}, we would reject the null hypothesis H_0:\\mu= {mean} in favor of the alternative hypothesis H_1:\\mu\\ne{mean} because P = {crit}<{alpha*2}")
			else:
				print(f"Since P = {crit} > {alpha * 2}, we fail to reject the null hypothesis H_0: \\mu = {mean} at \\alpha = {alpha *2}")
		crit = round(1 - st.norm.cdf(zfinal), 4)
		if crit == 0:
			crit = float(input("critical value = "))
		elif zfinal < (-crit):
			print(f"For \\alpha = {alpha * 2}, z_{{\\alpha/2}}=z_{{{alpha}}}={crit}. Since z_0 = {zfinal} < -{crit} = -z_{{{alpha}}}, we reject the null hypothesis H_0:\\mu={mean} in favor of the alternative hypothesis H_1:\\mu\\ne{mean} at \\alpha={alpha*2}.")
		elif zfinal > crit:
			print(f"For \\alpha = {alpha * 2}, z_{{\\alpha/2}}=z_{{{alpha}}}={crit}. Since z_0 = {zfinal} > {crit} = -z_{{{alpha}}}, we reject the null hypothesis H_0:\\mu={mean} in favor of the alternative hypothesis H_1:\\mu\\ne{mean} at \\alpha={alpha*2}.")
		else:
			print(f"For \\alpha = {alpha * 2}, z_{{\\alpha/2}}=z_{{{alpha}}}={crit}. Since z_0 = {zfinal} < -{crit} = -z_{{{alpha}}}, we fail to reject the null hypothesis H_0:\\mu={mean} at \\alpha={alpha*2}.")
	elif var_type == 2:
		print("\\\\t_0 = \\frac{\\bar{X} - \\mu_0}{s/\\sqrt{n}}")
		print("\\\\t_0 = \\frac{" + str(barx) + "- " + str(mean) + "}{" + str(sd) + "/\\sqrt{" + str(n) + "}}")
		zfinal = zvalue(barx, mean, sd, n)
		print("\\\\t_0 = " + str(zfinal))
		if pval == 1:
			crit = 2 * st.t.cdf(-abs(zfinal), n-1)
			print(f"Using Excel's function =T.DIST.2T(|t_0|,n-1), the P-value for t_0 = {zfinal} in an t-test with {n-1} degrees of freedom can be computed as P = P(T_{{{n-1}}}>{zfinal})=T.DIST.2T(|{zfinal}|,{n-1})={crit}.")
			if crit < alpha * 2:
				print(f"We would reject the null hypothesis H_0:\\mu= {mean} in favor of the alternative hypothesis H_1:\\mu\\ne{mean} because P = {crit}<{alpha*2}")
			else:
				print(f"Since P = {crit} > {alpha * 2}, we fail to reject the null hypothesis H_0: \\mu = {mean} at \\alpha = {alpha *2}")
		crit = st.t.ppf(1 - (alpha), n-1)
		if zfinal < (-crit):
			print(f"For \\alpha = {alpha * 2}, t_{{\\alpha/2}}=t_{{{alpha}}}={crit}. Since t_0 = {zfinal} < -{crit} = -t_{{{alpha}}}, we reject the null hypothesis H_0:\\mu={mean} in favor of the alternative hypothesis H_1:\\mu\\ne{mean} at \\alpha={alpha*2}.")
		elif zfinal > crit:
			print(f"For \\alpha = {alpha * 2}, t_{{\\alpha/2}}=t_{{{alpha}}}={crit}. Since t_0 = {zfinal} > {crit} = -t_{{{alpha}}}, we reject the null hypothesis H_0:\\mu={mean} in favor of the alternative hypothesis H_1:\\mu\\ne{mean} at \\alpha={alpha*2}.")
		else:
			print(f"For \\alpha = {alpha * 2}, t_{{\\alpha/2}}=t_{{{alpha}}}={crit}. Since t_0 = {zfinal} < -{crit} = -t_{{{alpha}}}, we fail to reject the null hypothesis H_0:\\mu={mean} at \\alpha={alpha*2}.")

elif type1 == 2:
	type2 = int(input("1. Null Hypothesis =\\n2. Null Hypophesis \\ge"))
	print("The test hypothesis is")
	if type2 == 1:
		print("\\\\Null\\;Hypothesis --> H_0: \\mu = \\mu_0")
	elif type2 ==2:
		print("\\\\Null\\;Hypothesis --> H_0: \\mu \\ge \\mu_0")
	print("\\\\Alternate\\;Hypothesis --> H_1: \\mu < \\mu_0")
	print("Now, the value of test static can be found out by following formula: ")
	if var_type == 1:
		print("\\\\Z_0 = \\frac{\\bar{X} - \\mu_0}{\\sigma/\\sqrt{n}}")
		print("\\\\Z_0 = \\frac{" + str(barx) + "-" + str(mean) + "}{" + str(sd) + "/" + str(n) + "}")
		zfinal = zvalue(barx, mean, sd, n)
		print("\\\\Z_0 = " + str(zfinal))
		if pval == 1:
			print(f"Since P-value of a upper tailed test is equal to \\phi(|Z_0|)")
			print(f"\\\\P = \\phi({zfinal})")
			print(f"P = {round(st.norm.cdf(zfinal), 4)}")
			crit = st.norm.cdf(zfinal)
			if crit < alpha * 2:
				print(f"Since P = {crit} < {alpha*2}, we reject the null hypothesis H_0:\\mu= {mean} in favor of the alternative hypothesis H_1:\\mu>{mean} at \\alpha = {alpha*2}.")
			else:
				print(f"Since P = {crit} > {alpha*2}, we fail to reject the null hypothesis H_0: \\mu = {mean} at \\alpha = {alpha *2}")
		crit = st.norm.ppf(1 - (alpha * 2))
		if crit == 0:
			crit = float(input("critical value = "))
		if zfinal < (-crit):
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are -Z_" + str(alpha*2) + " = -" + str(crit) + " and we note that Z_0 falls in the critical region. Therefore, H_0 is rejected, and we concluded that the mean is not equal to " + str(mean))
		else:
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are -Z_" + str(alpha*2) + " = -" + str(crit) + " and we note that Z_0 does not falls in the critical region. Therefore, we fail to reject H_0.")
	elif var_type == 2:
		print("\\\\t_0 = \\frac{\\bar{X} - \\mu_0}{s/\\sqrt{n}}")
		print("\\\\t_0 = \\frac{" + str(barx) + "- " + str(mean) + "}{" + str(sd) + "/\\sqrt{" + str(n) + "}")
		zfinal = zvalue(barx, mean, sd, n)
		print("\\\\t_0 = " + str(zfinal))
		if pval == 1:
			crit = st.t.cdf(zfinal, n-1)
			print(f"Using Excel's function =T.DIST(t_0,n-1,TRUE), the P-value for t_0 = {zfinal} in an power-tailed t-test with {n-1} degrees of freedom can be computed as P = P(T_{{{n-1}}}<{zfinal})=T.DIST({zfinal},{n-1},TRUE)={crit}.")
			if crit < alpha * 2:
				print(f"Since P = {crit} < {alpha*2}, we reject the null hypothesis H_0:\\mu= {mean} in favor of the alternative hypothesis H_1:\\mu>{mean} at \\alpha = {alpha*2}.")
			else:
				print(f"Since P = {crit} > {alpha*2}, we fail to reject the null hypothesis H_0: \\mu = {mean} at \\alpha = {alpha *2}")
		print(f"Since the sample size is n = {n}, degrees of freedom on the t-test statistic are n-1 = {n}-1 = {n-1}")
		crit = st.t.ppf(1 - (alpha * 2), n-1)
		print(f"This implies that")
		print(f"t_{{\\alpha, n-1}} = t_{{{alpha * 2}, {n-1}}} = {crit}")
		print(f"Since, the t distribution is symmetric about zero, so -t_{{{alpha*2},{n-1}}}")
		if zfinal < (-crit):
			print(f"Since t_0 = {zfinal}<-{crit}=-t_{{{alpha*2}}}, we reject the null hypothesis H_0:\\mu={mean} in favor of the alternative hypothesis H_1:\\mu >{mean} at \\alpha = {alpha * 2}.")
		else:
			print(f"Since t_0 = {zfinal}>-{crit}=-t_{{{alpha*2}}}, we fail to reject the null hypothesis H_0:\\mu={mean} at \\alpha = {alpha * 2}.")
		

elif type1 == 3:
	type2 = int(input("1. Null Hypothesis =\n 2. Null Hypophesis \\le"))
	print("The test hypothesis is")
	if type2 == 1:
		print("\\\\Null\\;Hypothesis --> H_0: \\mu = \\mu_0")
	elif type2 ==2:
		print("\\\\Null\\;Hypothesis --> H_0: \\mu \\le \\mu_0")
	print("\\\\Alternate\\;Hypothesis --> H_1: \\mu > \\mu_0")
	print("This is a one-sided test because the alternative hypothesis is formulated to detect the difference from the hypothesized mean on the upper side")
	print("Now, the value of test static can be found out by following formula: ")
	if var_type == 1:
		print("\\\\Z_0 = \\frac{\\bar{X} - \\mu_0}{\\sigma/\\sqrt{n}}")
		print("\\\\Z_0 = \\frac{" + str(barx) + "-" + str(mean) + "}{" + str(sd) + "/" + str(n) + "}")
		zfinal = zvalue(barx, mean, sd, n)
		print("\\\\Z_0 = " + str(zfinal))
		if pval == 1:
			print("Since P-value of a upper tailed test is equal to (1 - \\phi(|Z_0|)")
			print(f"P = 2(1 - \\phi({zfinal}))")
			print(f"P = 2(1 - {st.norm.cdf(zfinal)})")
			print(f"P = {round(1 - st.norm.cdf(zfinal), 6)}")
			crit = 1 - st.norm.cdf(zfinal)
			if crit < alpha * 2:
				print(f"Since P = {crit} < {alpha*2}, we reject the null hypothesis H_0:\\mu= {mean} in favor of the alternative hypothesis H_1:\\mu>{mean} at \\alpha = {alpha*2}.")
			else:
				print(f"Since P = {crit} > {alpha*2}, we fail to reject the null hypothesis H_0: \\mu = {mean} at \\alpha = {alpha *2}")
		crit = st.norm.ppf(1 - (alpha * 2))
		if crit == 0:
			crit = float(input("critical value = "))
		if zfinal > crit :
			print(f"For \\alpha = {alpha * 2}, z_\\alpha = z_{{{alpha * 2}}} = {crit}. Since z_0 = {zfinal}>{crit}=z_{{{alpha*2}}}, we reject the null hypothesis H_0:\\mu={mean} in favor of the alternative hypothesis H_1:\\mu >{mean} at \\alpha = {alpha * 2}.")
		else:
			print(f"For \\alpha = {alpha * 2}, z_\\alpha = z_{{{alpha * 2}}} = {crit}. Since z_0 = {zfinal}<{crit}=z_{{{alpha*2}}}, we fail to reject the null hypothesis H_0:\\mu={mean} at \\alpha = {alpha * 2}.")
	elif var_type == 2:
		print("\\\\t_0 = \\frac{\\bar{X} - \\mu_0}{s/\\sqrt{n}}")
		print("\\\\t_0 = \\frac{" + str(barx) + "- " + str(mean) + "}{" + str(sd) + "/\\sqrt{" + str(n) + "}}")
		zfinal = zvalue(barx, mean, sd, n)
		print("\\\\t_0 = " + str(zfinal))
		if pval == 1:
			crit = st.t.cdf(-zfinal, n-1)
			print(f"Using Excel's function =T.DIST.RT(t_0,n-1), the P-value for t_0 = {zfinal} in an upper-tailed t-test with {n-1} degrees of freedom can be computed as P = P(T_{{{n-1}}}>{zfinal})=T.DIST.RT({zfinal},{n-1})={crit}.")
			if crit < alpha * 2:
				print(f"Since P = {crit} < {alpha*2}, we reject the null hypothesis H_0:\\mu= {mean} in favor of the alternative hypothesis H_1:\\mu>{mean} at \\alpha = {alpha*2}.")
			else:
				print(f"Since P = {crit} > {alpha*2}, we fail to reject the null hypothesis H_0: \\mu = {mean} at \\alpha = {alpha *2}")
		print(f"Since the sample size is n = {n}, degrees of freedom on the t-test statistic are n-1 = {n}-1 = {n-1}")
		crit = st.t.ppf(1 - (alpha * 2), n-1)
		print(f"This implies that")
		print(f"t_{{\\alpha, n-1}} = t_{{{alpha * 2}, {n-1}}} = {crit}")
		if zfinal > (crit):
			print(f"Since t_0 = {zfinal}>{crit}=t_{{{alpha*2}}}, we reject the null hypothesis H_0:\\mu={mean} in favor of the alternative hypothesis H_1:\\mu >{mean} at \\alpha = {alpha * 2}.")
		else:
			print(f"Since t_0 = {zfinal}<{crit}=t_{{{alpha*2}}}, we fail to reject the null hypothesis H_0:\\mu={mean} at \\alpha = {alpha * 2}.")
		

if type1 == 4:
	print("The test hypothesis is")
	if delta0 == 0:
		print("\\\\Null\\;Hypothesis --> H_0: \\mu_1 = \\mu_2, or \\; H_0: \\mu_1 - \\mu_2 = 0")
	else:
		print("\\\\Null\\;Hypothesis --> H_0: \\mu_1 - \\mu_2 = \\Delta_0")
	print("\\\\Alternate\\;Hypothesis --> H_1: \\mu_1 \\ne \\mu_2, or \\; H_0: \\mu_1 - \\mu_2 \\ne 0")
	print("This is a two-sided test because the alternative hypothesis is formulated to detect differences from the hypothesized difference in mean values on either side.")
	print("Now, the value of test static can be found out by following formula: ")
	if var_type == 1:
		print("\\\\Z_0 = \\frac{\\bar{X_1} -\\bar{X_2} - \\Delta_0}{\\sqrt{\\frac{\\sigma_1^2}{n_1}+\\frac{\\sigma_2^2}{n_2}}}")
		print(f"\\\\Z_0 = \\frac{{{barx1}-{barx2}-{delta0}}}{{\\sqrt{{\\frac{{{var1}}}{{{n1}}}+\\frac{{{var2}}}{{{n2}}}}}}}")
		zfinal = get_test_statistic_two_mean(barx1, barx2, delta0, var1, var2, n1, n2)
		print("\\\\Z_0 = " + str(zfinal))
		if pval == 1:
			print("Since P-value of a two tailed test is equal to 2(1 - \\phi(|Z_0|)")
			print(f"P = 2(1 - \\phi({abs(zfinal)}))")
			print(f"P = 2(1 - {st.norm.cdf(abs(zfinal))})")
			print(f"P = {round(2 * (1 - st.norm.cdf(abs(zfinal))), 6)}")
			crit = 2 * (1 - st.norm.cdf(abs(zfinal)))
			if crit < alpha * 2:
				print(f"Suppose that the significance level \\alpha is specified to be {alpha*2}, we would reject the null hypothesis H_0 in favor of the alternative hypothesis H_1 because P = {crit}<{alpha*2}")
			else:
				print(f"Since P = {crit} > {alpha * 2}, we fail to reject the null hypothesis H_0 at \\alpha = {alpha *2}")
		crit = st.norm.ppf(1 - (alpha))
		if crit == 0:
			crit = float(input("critical value = "))
		elif zfinal < (-crit):
			print(f"For \\alpha = {alpha * 2}, z_{{\\alpha/2}}=z_{{{alpha}}}={crit}. Since z_0 = {zfinal} < -{crit} = -z_{{{alpha}}}, we reject the null hypothesis H_0 in favor of the alternative hypothesis H_1 at \\alpha={alpha*2}.")
		elif zfinal > crit:
			print(f"For \\alpha = {alpha * 2}, z_{{\\alpha/2}}=z_{{{alpha}}}={crit}. Since z_0 = {zfinal} > {crit} = -z_{{{alpha}}}, we reject the null hypothesis H_0 in favor of the alternative hypothesis H_1 at \\alpha={alpha*2}.")
		else:
			print(f"For \\alpha = {alpha * 2}, z_{{\\alpha/2}}=z_{{{alpha}}}={crit}. Since z_0 = {zfinal} < -{crit} = -z_{{{alpha}}}, we fail to reject the null hypothesis H_0 at \\alpha={alpha*2}.")
	elif var_type == 2:
		print(f"\\\\S_p^2 = \\frac{{(n_1-1)S_1^2+(n_2-1)S_2^2}}{{n_1+n_2-2}}")
		print(f"\\\\S_p^2 = \\frac{{({n1}-1){var1}+({n2}-1){var2}}}{{{n1}+{n2}-2}}")
		print(f"\\\\S_p^2 = \\frac{{({n1-1}){var1}+({n2-1}){var2}}}{{{n1+n2-2}}}")
		print(f"\\\\S_p^2 = \\frac{{{(n1-1)*var1}+{(n2-1)*var2}}}{{{n1+n2-2}}}")
		sp = get_sp_square(var1, var2, n1, n2)
		print(f"\\\\S_p^2 = {sp}")
		print(f"\\\\S_p = {math.sqrt(sp)}")
		print("\\\\t_0 = \\frac{\\bar{X_1} -\\bar{X_2} - \\Delta_0}{S_p\\sqrt{\\frac{1}{n_1}+\\frac{1}{n_2}}}")
		print(f"\\\\t_0 = \\frac{{{barx1}-{barx2} - {delta0}}}{{{math.sqrt(sp)}\\sqrt{{\\frac{{1}}{{{n1}}}+\\frac{{1}}{{{n2}}}}}}}")
		zfinal = get_test_statistic_two_mean_unknown_var(barx1, barx2, delta0, math.sqrt(sp), n1, n2)
		print("\\\\t_0 = " + str(zfinal))
		if pval == 1:
			crit = 2 * st.t.cdf(-abs(zfinal), n1+n2-2)
			print(f"Using Excel's function =T.DIST.2T(|t_0|,n-1), the P-value for t_0 = {zfinal} in an t-test with {n1+n2-2} degrees of freedom can be computed as P = P(T_{{{n1+n2-2}}}>{zfinal})=T.DIST.2T(|{zfinal}|,{n1+n2-2})={crit}.")
			if crit < alpha * 2:
				print(f"We would reject the null hypothesis H_0 in favor of the alternative hypothesis H_1 because P = {crit}<{alpha*2}")
			else:
				print(f"Since P = {crit} > {alpha * 2}, we fail to reject the null hypothesis H_0 at \\alpha = {alpha *2}")
		print(f"Degrees of freedom on the t-test statistic are n1 + n2 - 2 = {n1} + {n2} - 2 = {n1+n2-2}")
		crit = st.t.ppf(1 - (alpha), n1+n2-2)
		if zfinal < (-crit):
			print(f"For \\alpha = {alpha * 2}, t_{{\\alpha, n_1+n_2-2}}=t_{{{alpha}, {n1 + n2 - 2}}}={crit}. Since t_0 = {zfinal} < -{crit} = -t_{{{alpha}, {n1 + n2 - 2}}}, we reject the null hypothesis H0 in favor of the alternative hypothesis H_1 at \\alpha={alpha*2}.")
		elif zfinal > crit:
			print(f"For \\alpha = {alpha * 2}, t_{{\\alpha, n_1+n_2-2}}=t_{{{alpha}, {n1 + n2 - 2}}}={crit}. Since t_0 = {zfinal} > {crit} = t_{{{alpha}, {n1 + n2 - 2}}}, we reject the null hypothesis H0 in favor of the alternative hypothesis H_1 at \\alpha={alpha*2}.")
		else:
			print(f"For \\alpha = {alpha * 2}, t_{{\\alpha, n_1+n_2-2}}=t_{{{alpha}, {n1 + n2 - 2}}}={crit}. Since -t_{{{alpha}, {n1 + n2 - 2}}}<t_0<t_{{{alpha}, {n1 + n2 - 2}}}, we fail to reject the null hypothesis H0 at \\alpha={alpha*2}.")

elif type1 == 5:
	type2 = int(input("1. Null Hypothesis = \n2. Null Hypophesis \\ge"))
	print("The test hypothesis is")
	if type2 == 1:
		if delta0 == 0:
			print("\\\\Null\\;Hypothesis --> H_0: \\mu_1 = \\mu_2, or \\; H_0: \\mu_1 - \\mu_2 = 0")
		else:
			print("\\\\Null\\;Hypothesis --> H_0: \\mu_1 - \\mu_2 = \\Delta_0")
	elif type2 ==2:
		if delta0 == 0:
			print("\\\\Null\\;Hypothesis --> H_0: \\mu_1 \\ge \\mu_2, or \\; H_0: \\mu_1 - \\mu_2 \\ge 0")
		else:
			print("\\\\Null\\;Hypothesis --> H_0: \\mu_1 - \\mu_2 \\ge \\Delta_0")
	if delta0 == 0:
		print("\\\\Alternate\\;Hypothesis --> H_0: \\mu_1 < \\mu_2, or \\; H_0: \\mu_1 - \\mu_2 < 0")
	else:
		print("\\\\Alternate\\;Hypothesis --> H_0: \\mu_1 - \\mu_2 < \\Delta_0")
	print("Now, the value of test static can be found out by following formula: ")
	if var_type == 1:
		print("\\\\Z_0 = \\frac{\\bar{X_1} -\\bar{X_2} - \\Delta_0}{\\sqrt{\\frac{\\sigma_1^2}{n_1}+\\frac{\\sigma_2^2}{n_2}}}")
		print(f"\\\\Z_0 = \\frac{{{barx1}-{barx2}-{delta0}}}{{\\sqrt{{\\frac{{{var1}}}{{{n1}}}+\\frac{{{var2}}}{{{n2}}}}}}}")
		zfinal = get_test_statistic_two_mean(barx1, barx2, delta0, var1, var2, n1, n2)
		print("\\\\Z_0 = " + str(zfinal))
		if pval == 1:
			print(f"Since P-value of a upper tailed test is equal to \\phi(|Z_0|)")
			print(f"\\\\P = \\phi({zfinal})")
			print(f"P = {round(st.norm.cdf(zfinal), 4)}")
			crit = st.norm.cdf(zfinal)
			if crit < alpha * 2:
				print(f"Since P = {crit} < {alpha*2}, we reject the null hypothesis H_0 in favor of the alternative hypothesis H_1 at \\alpha = {alpha*2}.")
			else:
				print(f"Since P = {crit} > {alpha*2}, we fail to reject the null hypothesis H_0 at \\alpha = {alpha *2}")
		crit = st.norm.ppf(1 - (alpha * 2))
		if zfinal < (-crit):
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are -Z_" + str(alpha*2) + " = -" + str(crit) + " and we note that Z0 falls in the critical region. Therefore, H0 is rejected")
		else:
			print("Since \\alpha = " + str(alpha * 2) + ", the boundaries of the critical region are -Z_" + str(alpha*2) + " = -" + str(crit) + " and we note that Z0 does not falls in the critical region. Therefore, we fail to reject H0.")
	elif var_type == 2:
		print(f"\\\\S_p^2 = \\frac{{(n_1-1)S_1^2+(n_2-1)S_2^2}}{{n_1+n_2-2}}")
		print(f"\\\\S_p^2 = \\frac{{({n1}-1){var1}+({n2}-1){var2}}}{{{n1}+{n2}-2}}")
		print(f"\\\\S_p^2 = \\frac{{({n1-1}){var1}+({n2-1}){var2}}}{{{n1+n2-2}}}")
		print(f"\\\\S_p^2 = \\frac{{{(n1-1)*var1}+{(n2-1)*var2}}}{{{n1+n2-2}}}")
		sp = get_sp_square(var1, var2, n1, n2)
		print(f"\\\\S_p^2 = {sp}")
		print(f"\\\\S_p = {math.sqrt(sp)}")
		print("\\\\t_0 = \\frac{\\bar{X_1} -\\bar{X_2} - \\Delta_0}{S_p\\sqrt{\\frac{1}{n_1}+\\frac{1}{n_2}}}")
		print(f"\\\\t_0 = \\frac{{{barx1}-{barx2} - {delta0}}}{{{math.sqrt(sp)}\\sqrt{{\\frac{{1}}{{{n1}}}+\\frac{{1}}{{{n2}}}}}}}")
		zfinal = get_test_statistic_two_mean_unknown_var(barx1, barx2, delta0, math.sqrt(sp), n1, n2)
		print("\\\\t_0 = " + str(zfinal))
		if pval == 1:
			crit = st.t.cdf(zfinal, n1+n2-2)
			print(f"Using Excel's function =T.DIST(t_0,n-1,TRUE), the P-value for t_0 = {zfinal} in an power-tailed t-test with {n1+n2-2} degrees of freedom can be computed as P = P(T_{{{n1+n2-2}}}<{zfinal})=T.DIST({zfinal},{n1+n2-2},TRUE)={crit}.")
			if crit < alpha * 2:
				print(f"Since P = {crit} < {alpha*2}, we reject the null hypothesis H_0 in favor of the alternative hypothesis H_1 at \\alpha = {alpha*2}.")
			else:
				print(f"Since P = {crit} > {alpha*2}, we fail to reject the null hypothesis H_0 at \\alpha = {alpha *2}")
		print(f"Degrees of freedom on the t-test statistic are n1 + n2 - 2 = {n1} + {n2} - 2 = {n1+n2-2}")
		crit = st.t.ppf(1 - (alpha * 2), n1+n2-2)
		print(f"This implies that")
		print(f"t_{{\\alpha, n_1+n_2-2}} = t_{{{alpha * 2}, {n1} + {n2} - 2}} = t_{{{alpha * 2}, {n1 + n2 - 2}}} = {crit}")
		print(f"Since, the t distribution is symmetric about zero, so -t_{{{alpha * 2}, {n1 + n2 - 2}}}")
		if zfinal < (-crit):
			print(f"Since t_0 = {zfinal}<-{crit}=-t_{{{alpha * 2}, {n1 + n2 - 2}}}, we reject the null hypothesis H0 in favor of the alternative hypothesis H1 at \\alpha = {alpha * 2}.")
		else:
			print(f"Since t_0 = {zfinal}>-{crit}=-t_{{{alpha * 2}, {n1 + n2 - 2}}}, we fail to reject the null hypothesis H0 at \\alpha = {alpha * 2}.")
		

elif type1 == 6:
	type2 = int(input("1. Null Hypothesis =\n 2. Null Hypophesis \\le"))
	print("The test hypothesis is")
	if type2 == 1:
		if delta0 == 0:
			print("\\\\Null\\;Hypothesis --> H_0: \\mu_1 = \\mu_2, or \\; H_0: \\mu_1 - \\mu_2 = 0")
		else:
			print("\\\\Null\\;Hypothesis --> H_0: \\mu_1 - \\mu_2 = \\Delta_0")
	elif type2 ==2:
		if delta0 == 0:
			print("\\\\Null\\;Hypothesis --> H_0: \\mu_1 \\le \\mu_2, or \\; H_0: \\mu_1 - \\mu_2 \\le 0")
		else:
			print("\\\\Null\\;Hypothesis --> H_0: \\mu_1 - \\mu_2 \\le \\Delta_0")
	if delta0 == 0:
		print("\\\\Alternate\\;Hypothesis --> H_0: \\mu_1 > \\mu_2, or \\; H_0: \\mu_1 - \\mu_2 > 0")
	else:
		print("\\\\Alternate\\;Hypothesis --> H_0: \\mu_1 - \\mu_2 > \\Delta_0")
	print("This is a one-sided test because the alternative hypothesis is formulated to detect the difference from the hypothesized mean on the upper side")
	print("Now, the value of test static can be found out by following formula: ")
	if var_type == 1:
		print("\\\\Z_0 = \\frac{\\bar{X_1} -\\bar{X_2} - \\Delta_0}{\\sqrt{\\frac{\\sigma_1^2}{n_1}+\\frac{\\sigma_2^2}{n_2}}}")
		print(f"\\\\Z_0 = \\frac{{{barx1}-{barx2}-{delta0}}}{{\\sqrt{{\\frac{{{var1}}}{{{n1}}}+\\frac{{{var2}}}{{{n2}}}}}}}")
		zfinal = get_test_statistic_two_mean(barx1, barx2, delta0, var1, var2, n1, n2)
		print("\\\\Z_0 = " + str(zfinal))
		if pval == 1:
			print("Since P-value of a upper tailed test is equal to (1 - \\phi(Z_0)")
			print(f"P = 2(1 - \\phi({zfinal}))")
			print(f"P = 2(1 - {st.norm.cdf(zfinal)})")
			print(f"P = {round(1 - st.norm.cdf(zfinal), 6)}")
			crit = 1 - st.norm.cdf(zfinal)
			if crit < alpha * 2:
				print(f"Since P = {crit} < {alpha*2}, we reject the null hypothesis H_0 in favor of the alternative hypothesis H_1 at \\alpha = {alpha*2}.")
			else:
				print(f"Since P = {crit} > {alpha*2}, we fail to reject the null hypothesis H_0 at \\alpha = {alpha *2}")
		crit = st.norm.ppf(1 - (alpha * 2))
		if zfinal > crit :
			print(f"For \\alpha = {alpha * 2}, z_\\alpha = z_{{{alpha * 2}}} = {crit}. Since z_0 = {zfinal}>{crit}=z_{{{alpha*2}}}, we reject the null hypothesis H_0 in favor of the alternative hypothesis H_1 at \\alpha = {alpha * 2}.")
		else:
			print(f"For \\alpha = {alpha * 2}, z_\\alpha = z_{{{alpha * 2}}} = {crit}. Since z_0 = {zfinal}<{crit}=z_{{{alpha*2}}}, we fail to reject the null hypothesis H_0 at \\alpha = {alpha * 2}.")
	elif var_type == 2:
		print(f"\\\\S_p^2 = \\frac{{(n_1-1)S_1^2+(n_2-1)S_2^2}}{{n_1+n_2-2}}")
		print(f"\\\\S_p^2 = \\frac{{({n1}-1){var1}+({n2}-1){var2}}}{{{n1}+{n2}-2}}")
		print(f"\\\\S_p^2 = \\frac{{({n1-1}){var1}+({n2-1}){var2}}}{{{n1+n2-2}}}")
		print(f"\\\\S_p^2 = \\frac{{{(n1-1)*var1}+{(n2-1)*var2}}}{{{n1+n2-2}}}")
		sp = get_sp_square(var1, var2, n1, n2)
		print(f"\\\\S_p^2 = {sp}")
		print(f"\\\\S_p = {math.sqrt(sp)}")
		print("\\\\t_0 = \\frac{\\bar{X_1} -\\bar{X_2} - \\Delta_0}{S_p\\sqrt{\\frac{1}{n_1}+\\frac{1}{n_2}}}")
		print(f"\\\\t_0 = \\frac{{{barx1}-{barx2} - {delta0}}}{{{math.sqrt(sp)}\\sqrt{{\\frac{{1}}{{{n1}}}+\\frac{{1}}{{{n2}}}}}}}")
		zfinal = get_test_statistic_two_mean_unknown_var(barx1, barx2, delta0, math.sqrt(sp), n1, n2)
		print("\\\\t_0 = " + str(zfinal))
		if pval == 1:
			crit = st.t.cdf(-zfinal, n1+n2-2)
			print(f"Using Excel's function =T.DIST.RT(t_0,n-1), the P-value for t_0 = {zfinal} in an upper-tailed t-test with {n1+n2-2} degrees of freedom can be computed as P = P(T_{{{n1+n2-2}}}>{zfinal})=T.DIST.RT({zfinal},{n1+n2-2})={crit}.")
			if crit < alpha * 2:
				print(f"Since P = {crit} < {alpha*2}, we reject the null hypothesis H_0 in favor of the alternative hypothesis H_1 at \\alpha = {alpha*2}.")
			else:
				print(f"Since P = {crit} > {alpha*2}, we fail to reject the null hypothesis H_0 at \\alpha = {alpha *2}")
		print(f"Degrees of freedom on the t-test statistic are n1 + n2 - 2 = {n1} + {n2} - 2 = {n1+n2-2}")
		crit = st.t.ppf(1 - (alpha * 2), n1+n2-2)
		print(f"This implies that")
		print(f"t_{{\\alpha, n_1+n_2-2}} = t_{{{alpha * 2}, {n1} + {n2} - 2}} = t_{{{alpha * 2}, {n1 + n2 - 2}}} = {crit}")
		if zfinal > (crit):
			print(f"Since t_0 = {zfinal}>{crit}=t_{{{alpha * 2}, {n1 + n2 - 2}}}, we reject the null hypothesis H_0 in favor of the alternative hypothesis H_1 at \\alpha = {alpha * 2}.")
		else:
			print(f"Since t_0 = {zfinal}<{crit}=t_{{{alpha * 2}, {n1 + n2 - 2}}}, we fail to reject the null hypothesis H_0 at \\alpha = {alpha * 2}.")

print("Please hit thumbs up if the answer helped you.")
