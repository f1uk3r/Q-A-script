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

def get_test_statistic_two_mean_unknown_inequal_var(barx1, barx2, delta0, var1, var2, n1, n2):
	return round((barx1 - barx2 - delta0)/(math.sqrt((var1/n1)+(var2/n2))), 4)

zs = dict([(0.15, 1.04), (0.125, 1.15), (0.1, 1.282), (0.075, 1.44), (0.05, 1.645), (0.04, 1.75), (0.025, 1.96), (0.02, 2.05), (0.01, 2.33), (0.005, 2.576), (0.0025, 2.807), (0.0005, 3.291)])
print("1. Alternative hypothesis \\neq\n2. Alternative hypothesis < (not fully tested)\n3. Alternative hypothesis >")
print("4. For two distributions Alternative hypothesis \\neq\n5. For two distributions Alternative hypothesis <\n6. For two distributions Alternative hypothesis >")
pval = int(input("Need to calculate P value also? Press 1 for yes: "))
type1 = int(input("Mention the type as legend: "))
var_type = int(input("1. Population variance or 2. Sample variance: "))


if type1 < 4:
	mean = float(input("\\\\\\mu_0 = "))
	n = int(input("\\\\n = "))
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
			var1 = float(input("\\\\S_1^2 = "))
			var2 = float(input("\\\\S_2^2 = "))
		else:
			sd1 = float(input("\\\\S_1 = "))
			sd2 = float(input("\\\\S_2 = "))
			var1 = sd1 ** 2
			var2 = sd2 ** 2
			print(f"\\\\S_1^2 = {var1}")
			print(f"\\\\S_2^2 = {var2}")
	n1 = int(input("\\\\n_1 = "))
	n2 = int(input("\\\\n_2 = "))
	alpha = round(float(input("\\\\\\alpha = ")) / 2, 4)


if type1 == 1:
	print("The test hypothesis is")
	print("\\\\\\text{Null Hypothesis }--> H_0: \\mu = \\mu_0")
	print("\\\\\\text{Alternate Hypothesis }--> H_1: \\mu \\ne \\mu_0")
	print("This is a two-sided test because the alternative hypothesis is formulated to detect hypothesized mean value on either side.")
	print("Now, the value of test static can be found out by following formula: ")
	if var_type == 1:
		print("\\\\Z_0 = \\frac{\\bar{X} - \\mu_0}{\\sigma/\\sqrt{n}}")
		print(f"\\\\Z_0 = \\frac{{{barx}-{mean}}}{{{sd}/\\sqrt{{{n}}}}}")
		zfinal = zvalue(barx, mean, sd, n)
		print(f"\\\\Z_0 = {zfinal}")
		if pval == 1:
			print("Since P-value of a two tailed test is equal to 2(1 - \\phi(|Z_0|)")
			print(f"P = 2(1 - \\phi({abs(zfinal)}))")
			print(f"P = 2(1 - {st.norm.cdf(zfinal)})")
			print(f"P = {round(2 * (1 - st.norm.cdf(zfinal)), 4)}")
			crit = 2 * (1 - st.norm.cdf(zfinal))
			if crit < alpha * 2:
				print(f"\\\\\\\\\\text{{Suppose that the significance level }}\\alpha\\text{{ is specified to be {alpha*2}, we would reject the null hypothesis }} H_0:\\mu={mean} \\text{{ in favor of the alternative hypothesis }}H_1:\\mu\\ne{mean}\\text{{ because P = }}{crit}<{alpha*2}")
			else:
				print(f"\\\\\\\\\\text{{Since P = }}{crit} > {alpha * 2}\\text{{,\\text{{ we fail to reject the null hypothesis }}H_0: }}\\mu = {mean}\\text{{ at }}\\alpha = {alpha *2}")
		crit = round(st.norm.ppf(1 - alpha), 4)
		print(f"\\\\\\\\\\text{{Critical value = }}z_{{\\alpha/2}} = z_{{{round(alpha, 4)}}} = {crit}")
		print(f"\\\\\\\\\\text{{Rejection Region: }}z_0 > z_{{\\alpha/2}}\\text{{  or  }}z_0 < -z_{{\\alpha/2}}")
		if zfinal < (-crit):
			print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, z_{{\\alpha/2}}=z_{{{alpha}}}={crit}.\\text{{ Since }}z_0 = {zfinal} < -{crit} = -z_{{{alpha}}},\\text{{ we reject the null hypothesis }}H_0:\\mu={mean}\\text{{ in favor of the alternative hypothesis }}H_1:\\mu\\ne{mean}\\text{{ at }}\\alpha={alpha*2}.")
		elif zfinal > crit:
			print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, z_{{\\alpha/2}}=z_{{{alpha}}}={crit}.\\text{{ Since }}z_0 = {zfinal} > {crit} = z_{{{alpha}}},\\text{{ we reject the null hypothesis }}H_0:\\mu={mean}\\text{{ in favor of the alternative hypothesis }}H_1:\\mu\\ne{mean}\\text{{ at }}\\alpha={alpha*2}.")
		else:
			print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, z_{{\\alpha/2}}=z_{{{alpha}}}={crit}.\\text{{ Since }}z_0 = {zfinal} < -{crit} = -z_{{{alpha}}},\\text{{ we fail to reject the null hypothesis }}H_0:\\mu={mean}\\text{{ at }}\\alpha={alpha*2}.")
	elif var_type == 2:
		print("\\\\t_0 = \\frac{\\bar{X} - \\mu_0}{s/\\sqrt{n}}")
		print(f"\\\\t_0 = \\frac{{{barx}- {mean}}}{{{sd}/\\sqrt{{{n}}}}}")
		zfinal = zvalue(barx, mean, sd, n)
		print(f"\\\\t_0 = {zfinal}")
		if pval == 1:
			crit = 2 * st.t.cdf(-abs(zfinal), n-1)
			print(f"\\\\\\\\\\text{{Using Excel's function }}=T.DIST.2T(|t_0|,n-1)\\text{{, the P-value for }}t_0 = {zfinal}\\text{{ in an t-test with {n-1} degrees of freedom can be computed as P = }}P(T_{{{n-1}}}>{zfinal})=T.DIST.2T(|{zfinal}|,{n-1})={crit}.")
			if crit < alpha * 2:
				print(f"\\\\\\\\\\text{{We would reject the null hypothesis }}H_0:\\mu= {mean}\\text{{ in favor of the alternative hypothesis }}H_1:\\mu\\ne{mean}\\text{{ because P = }}{crit}<{alpha*2}")
			else:
				print(f"\\\\\\\\\\text{{Since P = {crit} > {alpha * 2}, we fail to reject the null hypothesis }}H_0: \\mu = {mean}\\text{{ at }}\\alpha = {alpha *2}")
		crit = round(st.t.ppf(1 - (alpha), n-1), 4)
		print(f"\\\\\\\\\\text{{Critical value = }}t_{{\\alpha/2, n-1}} = t_{{{round(alpha/2, 4)}, {n-1}}} = {crit}")
		print(f"\\\\\\\\\\text{{Rejection Region: }}t_0 > t_{{\\alpha/2, n-1}}\\text{{  or  }}t_0 < -t_{{\\alpha/2, n-1}}")
		if zfinal < (-crit):
			print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, t_{{\\alpha/2, n-1}}=t_{{{alpha}, {n-1}}}={crit}.\\text{{ Since }}t_0 = {zfinal} < -{crit} = -t_{{{alpha}}},\\text{{ we reject the null hypothesis }}H_0:\\mu={mean}\\text{{ in favor of the alternative hypothesis }}H_1:\\mu\\ne{mean}\\text{{ at }}\\alpha={alpha*2}.")
		elif zfinal > crit:
			print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, t_{{\\alpha/2, n-1}}=t_{{{alpha}, {n-1}}}={crit}.\\text{{ Since }}t_0 = {zfinal} > {crit} = -t_{{{alpha}}},\\text{{ we reject the null hypothesis }}H_0:\\mu={mean}\\text{{ in favor of the alternative hypothesis }}H_1:\\mu\\ne{mean}\\text{{ at }}\\alpha={alpha*2}.")
		else:
			print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, t_{{\\alpha/2, n-1}}=t_{{{alpha}, {n-1}}}={crit}.\\text{{ Since }}t_0 = {zfinal} < -{crit} = -t_{{{alpha}}},\\text{{ we fail to reject the null hypothesis }}H_0:\\mu={mean}\\text{{ at }}\\alpha={alpha*2}.")

elif type1 == 2:
	type2 = int(input("1. Null Hypothesis =\n2. Null Hypophesis \\ge"))
	print("The test hypothesis is")
	if type2 == 1:
		print("\\\\\\text{Null Hypothesis }--> H_0: \\mu = \\mu_0")
	elif type2 ==2:
		print("\\\\\\text{Null Hypothesis }--> H_0: \\mu \\ge \\mu_0")
	print("\\\\\\text{Alternate Hypothesis }--> H_1: \\mu < \\mu_0")
	print(f"This is a left-tailed test because the alternative hypothesis is formulated to detect claim if mean is less than {mean}.")
	print("Now, the value of test static can be found out by following formula: ")
	if var_type == 1:
		print("\\\\Z_0 = \\frac{\\bar{X} - \\mu_0}{\\sigma/\\sqrt{n}}")
		print(f"\\\\Z_0 = \\frac{{{barx}-{mean}}}{{{sd}/\\sqrt{{{n}}}}}")
		zfinal = zvalue(barx, mean, sd, n)
		print(f"\\\\Z_0 = {zfinal}")
		if pval == 1:
			print(f"Since P-value of a upper tailed test is equal to \\phi(|Z_0|)")
			print(f"\\\\P = \\phi({zfinal})")
			print(f"P = {round(st.norm.cdf(zfinal), 4)}")
			crit = st.norm.cdf(zfinal)
			if crit < alpha * 2:
				print(f"\\\\\\\\\\text{{Since P = {crit} < {alpha*2}, we reject the null hypothesis }}H_0:\\mu= {mean}\\text{{ in favor of the alternative hypothesis }}H_1:\\mu>{mean}\\text{{ at }}\\alpha = {alpha*2}.")
			else:
				print(f"\\\\\\\\\\text{{Since P = {crit} > {alpha*2}, we fail to reject the null hypothesis }}H_0: \\mu = {mean}\\text{{ at }}\\alpha = {alpha *2}")
		crit = round(st.norm.ppf(1 - (alpha * 2)), 4)
		print(f"\\\\\\\\\\text{{Critical value = }}z_{{\\alpha}} = z_{{{alpha*2}}} = {crit}")
		print(f"\\\\\\\\\\text{{Rejection Region: }}z_0 < -z_{{\\alpha}}")
		if zfinal < (-crit):
			print(f"\\\\\\\\\\text{{Since }}\\alpha = {alpha * 2}\\text{{, the boundaries of the critical region are }}-Z_{{{alpha*2}}} = -{crit}\\text{{ and we note that }}Z_0\\text{{ falls in the critical region. Therefore, }}H_0\\text{{ is rejected, and we concluded that the mean is not equal to {mean}}}")
		else:
			print(f"\\\\\\\\\\text{{Since }}\\alpha = {alpha * 2}\\text{{, the boundaries of the critical region are }}-Z_{{{alpha*2}}} = -{crit}\\text{{ and we note that }}Z_0\\text{{ does not falls in the critical region. Therefore, we fail to reject }}H_0.")
	elif var_type == 2:
		print("\\\\t_0 = \\frac{\\bar{X} - \\mu_0}{s/\\sqrt{n}}")
		print(f"\\\\t_0 = \\frac{{{barx}- {mean}}}{{{sd}/\\sqrt{{{n}}}}}")
		zfinal = zvalue(barx, mean, sd, n)
		print(f"\\\\t_0 = {zfinal}")
		if pval == 1:
			crit = st.t.cdf(zfinal, n-1)
			print(f"\\\\\\\\\\text{{Using Excel's function }}=T.DIST(t_0,n-1,TRUE)\\text{{, the P-value for }}t_0 = {zfinal} \\text{{in an power-tailed t-test with {n-1} degrees of freedom can be computed as P = }}P(T_{{{n-1}}}<{zfinal})=T.DIST({zfinal},{n-1},TRUE)={crit}.")
			if crit < alpha * 2:
				print(f"\\\\\\\\\\text{{Since P = {crit} < {alpha*2}, we reject the null hypothesis }}H_0:\\mu= {mean}\\text{{ in favor of the alternative hypothesis }}H_1:\\mu>{mean}\\text{{ at }}\\alpha = {alpha*2}.")
			else:
				print(f"\\\\\\\\\\text{{Since P = {crit} > {alpha*2}, we fail to reject the null hypothesis }}H_0: \\mu = {mean}\\text{{ at }}\\alpha = {alpha *2}")
		crit = round(st.t.ppf(1 - (alpha * 2), n-1), 4)
		print(f"\\\\\\\\\\text{{Critical value = }}t_{{\\alpha, n-1}} = t_{{{alpha*2}, {n-1}}} = {crit}")
		print(f"\\\\\\\\\\text{{Rejection Region: }}t_0 < -t_{{\\alpha/2, n-1}}")
		if zfinal < (-crit):
			print(f"\\\\\\\\\\text{{Since }}t_0 = {zfinal}<-{crit}=-t_{{{alpha*2}}},\\text{{ we reject the null hypothesis }}H_0:\\mu={mean}\\text{{ in favor of the alternative hypothesis }}H_1:\\mu >{mean}\\text{{ at }}\\alpha = {alpha * 2}.")
		else:
			print(f"\\\\\\\\\\text{{Since }}t_0 = {zfinal}>-{crit}=-t_{{{alpha*2}}},\\text{{ we fail to reject the null hypothesis }}H_0:\\mu={mean}\\text{{ at }}\\alpha = {alpha * 2}.")


elif type1 == 3:
	type2 = int(input("1. Null Hypothesis =\n 2. Null Hypophesis \\le"))
	print("The test hypothesis is")
	if type2 == 1:
		print("\\\\\\text{Null Hypothesis }--> H_0: \\mu = \\mu_0")
	elif type2 ==2:
		print("\\\\\\text{Null Hypothesis }--> H_0: \\mu \\le \\mu_0")
	print("\\\\\\text{Alternate Hypothesis }--> H_1: \\mu > \\mu_0")
	print("This is a right-tailed test because the alternative hypothesis is formulated to detect claim if difference of data is more than 0.")
	print("Now, the value of test static can be found out by following formula: ")
	if var_type == 1:
		print("\\\\Z_0 = \\frac{\\bar{X} - \\mu_0}{\\sigma/\\sqrt{n}}")
		print(f"\\\\Z_0 = \\frac{{{barx}-{mean}}}{{{sd}/\\sqrt{{{n}}}}}")
		zfinal = zvalue(barx, mean, sd, n)
		print(f"\\\\Z_0 = {zfinal}")
		if pval == 1:
			print("Since P-value of a upper tailed test is equal to (1 - \\phi(|Z_0|))")
			print(f"P = (1 - \\phi({zfinal}))")
			print(f"P = (1 - {st.norm.cdf(zfinal)})")
			print(f"P = {round(1 - st.norm.cdf(zfinal), 6)}")
			crit = 1 - st.norm.cdf(zfinal)
			if crit < alpha * 2:
				print(f"\\\\\\\\\\text{{Since P = {crit} < {alpha*2}, we reject the null hypothesis }}H_0:\\mu= {mean}\\text{{ in favor of the alternative hypothesis }}H_1:\\mu>{mean}\\text{{ at }}\\alpha = {alpha*2}.")
			else:
				print(f"\\\\\\\\\\text{{Since P = {crit} > {alpha*2}, we fail to reject the null hypothesis }}H_0: \\mu = {mean}\\text{{ at }}\\alpha = {alpha *2}")
		crit = round(st.norm.ppf(1 - (alpha * 2)), 4)
		print(f"\\\\\\\\\\text{{Critical value = }}z_{{\\alpha}} = z_{{{alpha*2}}} = {crit}")
		print(f"\\\\\\\\\\text{{Rejection Region: }}z_0 > z_{{\\alpha}}")
		if zfinal > crit :
			print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, z_\\alpha = z_{{{alpha * 2}}} = {crit}\\text{{. Since }}z_0 = {zfinal}>{crit}=z_{{{alpha*2}}},\\text{{ we reject the null hypothesis }}H_0:\\mu={mean}\\text{{ in favor of the alternative hypothesis }}H_1:\\mu >{mean}\\text{{ at }}\\alpha = {alpha * 2}.")
		else:
			print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, z_\\alpha = z_{{{alpha * 2}}} = {crit}\\text{{. Since }}z_0 = {zfinal}<{crit}=z_{{{alpha*2}}},\\text{{ we fail to reject the null hypothesis }}H_0:\\mu={mean}\\text{{ at }}\\alpha = {alpha * 2}.")
	elif var_type == 2:
		print("\\\\t_0 = \\frac{\\bar{X} - \\mu_0}{s/\\sqrt{n}}")
		print(f"\\\\t_0 = \\frac{{{barx}- {mean}}}{{{sd}/\\sqrt{{{n}}}}}")
		zfinal = zvalue(barx, mean, sd, n)
		print(f"\\\\t_0 = {zfinal}")
		if pval == 1:
			crit = st.t.cdf(-zfinal, n-1)
			print(f"\\\\\\\\\\text{{Using Excel's function }}=T.DIST.RT(t_0,n-1)\\text{{, the P-value for }}t_0 = {zfinal}\\text{{ in an upper-tailed t-test with {n-1} degrees of freedom can be computed as P = }}P(T_{{{n-1}}}>{zfinal})=T.DIST.RT({zfinal},{n-1})={crit}.")
			if crit < alpha * 2:
				print(f"\\\\\\\\\\text{{Since P = {crit} < {alpha*2}, we reject the null hypothesis }}H_0:\\mu= {mean}\\text{{ in favor of the alternative hypothesis }}H_1:\\mu>{mean}\\text{{ at }}\\alpha = {alpha*2}.")
			else:
				print(f"\\\\\\\\\\text{{Since P = {crit} > {alpha*2}, we fail to reject the null hypothesis }}H_0: \\mu = {mean}\\text{{ at }}\\alpha = {alpha *2}")
		crit = round(st.t.ppf(1 - (alpha * 2), n-1), 4)
		print(f"\\\\\\\\\\text{{Critical value = }}t_{{\\alpha, n-1}} = t_{{{alpha*2}, {n-1}}} = {crit}")
		print(f"\\\\\\\\\\text{{Rejection Region: }}t_0 > t_{{\\alpha, n-1}}")
		if zfinal > (crit):
			print(f"\\\\\\\\\\text{{Since }}t_0 = {zfinal}>{crit}=t_{{{alpha*2}}},\\text{{ we reject the null hypothesis }}H_0:\\mu={mean}\\text{{ in favor of the alternative hypothesis }}H_1:\\mu >{mean}\\text{{ at }}\\alpha = {alpha * 2}.")
		else:
			print(f"\\\\\\\\\\text{{Since }}t_0 = {zfinal}<{crit}=t_{{{alpha*2}}},\\text{{ we fail to reject the null hypothesis }}H_0:\\mu={mean}\\text{{ at }}\\alpha = {alpha * 2}.")


if type1 == 4:
	print("The test hypothesis is")
	if delta0 == 0:
		print("\\\\\\text{Null Hypothesis }--> H_0: \\mu_1 = \\mu_2, or \\; H_0: \\mu_1 - \\mu_2 = 0")
	else:
		print("\\\\\\text{Null Hypothesis }--> H_0: \\mu_1 - \\mu_2 = \\Delta_0")
	print("\\\\\\text{Alternate Hypothesis }--> H_1: \\mu_1 \\ne \\mu_2, or \\; H_1: \\mu_1 - \\mu_2 \\ne 0")
	print("This is a two-sided test because the alternative hypothesis is formulated to detect differences from the hypothesized difference in mean values on either side.")
	print("Now, the value of test static can be found out by following formula: ")
	if var_type == 1:
		print("\\\\Z_0 = \\frac{\\bar{X_1} -\\bar{X_2} - \\Delta_0}{\\sqrt{\\frac{\\sigma_1^2}{n_1}+\\frac{\\sigma_2^2}{n_2}}}")
		print(f"\\\\Z_0 = \\frac{{{barx1}-{barx2}-{delta0}}}{{\\sqrt{{\\frac{{{var1}}}{{{n1}}}+\\frac{{{var2}}}{{{n2}}}}}}}")
		print(f"\\\\Z_0 = \\frac{{{barx1-barx2-delta0}}}{{\\sqrt{{{round(var1/n1, 4)}+{round(var2/n2, 4)}}}}}")
		print(f"\\\\Z_0 = \\frac{{{barx1-barx2-delta0}}}{{\\sqrt{{{round(var1/n1, 4)+round(var2/n2, 4)}}}}}")
		print(f"\\\\Z_0 = \\frac{{{barx1-barx2-delta0}}}{{{round(((var1/n1)+(var2/n2))**0.5, 4)}}}")
		zfinal = get_test_statistic_two_mean(barx1, barx2, delta0, var1, var2, n1, n2)
		print(f"\\\\Z_0 = {zfinal}")
		if pval == 1:
			print("Since P-value of a two tailed test is equal to 2(1 - \\phi(|Z_0|))")
			print(f"P = 2(1 - \\phi({abs(zfinal)}))")
			print(f"P = 2(1 - {st.norm.cdf(abs(zfinal))})")
			print(f"P = {round(2 * (1 - st.norm.cdf(abs(zfinal))), 6)}")
			crit = 2 * (1 - st.norm.cdf(abs(zfinal)))
			if crit < alpha * 2:
				print(f"\\\\\\\\\\text{{Suppose that the significance level }}\\alpha\\text{{ is specified to be {alpha*2}, we would reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ because P = }}{crit}<{alpha*2}")
			else:
				print(f"\\\\\\\\\\text{{Since P = {crit} > {alpha * 2},}}\\text{{ we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha = {alpha *2}")
		crit = round(st.norm.ppf(1 - (alpha)), 4)
		print(f"\\\\\\\\\\text{{Critical value = }}z_{{\\alpha/2}} = z_{{{round(alpha, 4)}}} = {crit}")
		print(f"\\\\\\\\\\text{{Rejection Region: }}z_0 > z_{{\\alpha/2}}\\text{{  or  }}z_0 < -z_{{\\alpha/2}}")
		if zfinal < (-crit):
			print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, z_{{\\alpha/2}}=z_{{{alpha}}}={crit}\\text{{. Since }}z_0 = {zfinal} < -{crit} = -z_{{{alpha}}},\\text{{ we reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ at }}\\alpha={alpha*2}.")
		elif zfinal > crit:
			print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, z_{{\\alpha/2}}=z_{{{alpha}}}={crit}\\text{{. Since }}z_0 = {zfinal} > {crit} = -z_{{{alpha}}},\\text{{ we reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ at }}\\alpha={alpha*2}.")
		else:
			print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, z_{{\\alpha/2}}=z_{{{alpha}}}={crit}\\text{{. Since }}z_0 = {zfinal} < -{crit} = -z_{{{alpha}}},\\text{{ we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha={alpha*2}.")
	elif var_type == 2:
		variance_equality = int(input("1. If population variance are equal(If nothing is written about equality of population variance, most of the time they are equal)"))
		if variance_equality == 1:
			sp = get_sp_square(var1, var2, n1, n2)
			print(f"\\\\S_p^2 = \\frac{{(n_1-1)S_1^2+(n_2-1)S_2^2}}{{n_1+n_2-2}}")
			print(f"\\\\S_p^2 = \\frac{{({n1}-1){var1}+({n2}-1){var2}}}{{{n1}+{n2}-2}}")
			print(f"\\\\S_p^2 = \\frac{{({n1-1}){var1}+({n2-1}){var2}}}{{{n1+n2-2}}}")
			print(f"\\\\S_p^2 = \\frac{{{(n1-1)*var1}+{(n2-1)*var2}}}{{{n1+n2-2}}}")
			print(f"\\\\S_p^2 = {sp}")
			print(f"\\\\S_p = {math.sqrt(sp)}")
			print("Now, the value of test static can be found out by following formula: ")
			print("\\\\t_0 = \\frac{\\bar{X_1} -\\bar{X_2} - \\Delta_0}{S_p\\sqrt{\\frac{1}{n_1}+\\frac{1}{n_2}}}")
			print(f"\\\\t_0 = \\frac{{{barx1}-{barx2} - {delta0}}}{{{math.sqrt(sp)}\\sqrt{{\\frac{{1}}{{{n1}}}+\\frac{{1}}{{{n2}}}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{{math.sqrt(sp)}\\sqrt{{{round(1/n1,4)}+{round(1/n1,4)}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{{math.sqrt(sp)}\\sqrt{{{round((1/n1)+(1/n2),4)}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{{math.sqrt(sp)}({round(((1/n1)+(1/n2))**0.5,4)})}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{{round((((1/n1)+(1/n2))*sp)**0.5,4)}}}")
			zfinal = get_test_statistic_two_mean_unknown_var(barx1, barx2, delta0, math.sqrt(sp), n1, n2)
			print(f"\\\\t_0 = {zfinal}")
			if pval == 1:
				crit = 2 * st.t.cdf(-abs(zfinal), n1+n2-2)
				print(f"\\\\\\\\\\text{{Using Excel's function }}=T.DIST.2T(|t_0|,n-1)\\text{{, the P-value for }}t_0 = {zfinal}\\text{{ in an t-test with {n1+n2-2} degrees of freedom can be computed as P = }}P(T_{{{n1+n2-2}}}>{zfinal})=T.DIST.2T(|{zfinal}|,{n1+n2-2})={crit}.")
				if crit < alpha * 2:
					print(f"\\\\\\\\\\text{{We would reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ because P = }}{crit}<{alpha*2}")
				else:
					print(f"\\\\\\\\\\text{{Since P = {crit} > {alpha * 2},}}\\text{{ we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha = {alpha *2}")
			print(f"Degrees of freedom on the t-test statistic are n1 + n2 - 2 = {n1} + {n2} - 2 = {n1+n2-2}")
			crit = round(st.t.ppf(1 - (alpha), n1+n2-2), 4)
			print(f"\\\\\\\\\\text{{Critical value = }}t_{{\\alpha/2, n_1 + n_2 - 2}} = t_{{{round(alpha, 4)}, {n1+n2-2}}} = {crit}")
			print(f"\\\\\\\\\\text{{Rejection Region: }}t_0 > t_{{\\alpha/2, n_1 + n_2 - 2}}\\text{{  or  }}t_0 < -t_{{\\alpha/2, n_1 + n_2 - 2}}")
			if zfinal < (-crit):
				print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, t_{{\\alpha/2, n_1+n_2-2}}=t_{{{alpha}, {n1 + n2 - 2}}}={crit}\\text{{. Since }}t_0 = {zfinal} < -{crit} = -t_{{{alpha}, {n1 + n2 - 2}}},\\text{{ we reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ at }}\\alpha={alpha*2}.")
			elif zfinal > crit:
				print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, t_{{\\alpha/2, n_1+n_2-2}}=t_{{{alpha}, {n1 + n2 - 2}}}={crit}\\text{{. Since }}t_0 = {zfinal} > {crit} = t_{{{alpha}, {n1 + n2 - 2}}},\\text{{ we reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ at }}\\alpha={alpha*2}.")
			else:
				print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, t_{{\\alpha/2, n_1+n_2-2}}=t_{{{alpha}, {n1 + n2 - 2}}}={crit}\\text{{. Since }}-t_{{{alpha}, {n1 + n2 - 2}}}<t_0<t_{{{alpha}, {n1 + n2 - 2}}},\\text{{ we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha={alpha*2}.")
		else:
			print("Now, the value of test static can be found out by following formula: ")
			print("\\\\t_0 = \\frac{\\bar{X_1} -\\bar{X_2} - \\Delta_0}{\\sqrt{\\frac{S_1^2}{n_1}+\\frac{S_2^2}{n_2}}}")
			print(f"\\\\t_0 = \\frac{{{barx1}-{barx2} - {delta0}}}{{\\sqrt{{\\frac{{{var1}}}{{{n1}}}+\\frac{{{var2}}}{{{n2}}}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{\\sqrt{{{round(var1/n1,4)}+{round(var2/n1,4)}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{\\sqrt{{{round((var1/n1)+(var2/n2),4)}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{{round(((var1/n1)+(var2/n2))**0.5,4)}}}")
			zfinal = get_test_statistic_two_mean_unknown_inequal_var(barx1, barx2, delta0, var1, var2, n1, n2)
			print(f"\\\\t_0 = {zfinal}")
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
			if pval == 1:
				crit = 2 * st.t.cdf(-abs(zfinal), df)
				print(f"\\\\\\\\\\text{{Using Excel's function }}=T.DIST.2T(|t_0|,n-1)\\text{{, the P-value for }}t_0 = {zfinal}\\text{{ in an t-test with {n1+n2-2} degrees of freedom can be computed as P = }}P(T_{{{n1+n2-2}}}>{zfinal})=T.DIST.2T(|{zfinal}|,{n1+n2-2})={crit}.")
				if crit < alpha * 2:
					print(f"\\\\\\\\\\text{{We would reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ because P = }}{crit}<{alpha*2}")
				else:
					print(f"\\\\\\\\\\text{{Since P = {crit} > {alpha * 2},}}\\text{{ we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha = {alpha *2}")
			print(f"Degrees of freedom on the t-test statistic are \\nu = {df}")
			crit = round(st.t.ppf(1 - (alpha), df), 4)
			print(f"\\\\\\\\\\text{{Critical value = }}t_{{\\alpha/2, \\nu}} = t_{{{round(alpha, 4)}, {df}}} = {crit}")
			print(f"\\\\\\\\\\text{{Rejection Region: }}t_0 > t_{{\\alpha/2, \\nu}}\\text{{  or  }}t_0 < -t_{{\\alpha/2, \\nu}}")
			if zfinal < (-crit):
				print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, t_{{\\alpha/2, \\nu}}=t_{{{alpha}, {df}}}={crit}\\text{{. Since }}t_0 = {zfinal} < -{crit} = -t_{{{alpha}, {df}}},\\text{{ we reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ at }}\\alpha={alpha*2}.")
			elif zfinal > crit:
				print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, t_{{\\alpha/2, \\nu}}=t_{{{alpha}, {df}}}={crit}\\text{{. Since }}t_0 = {zfinal} > {crit} = t_{{{alpha}, {df}}},\\text{{ we reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ at }}\\alpha={alpha*2}.")
			else:
				print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, t_{{\\alpha/2, \\nu}}=t_{{{alpha}, {df}}}={crit}\\text{{. Since }}-t_{{{alpha}, {df}}}<t_0<t_{{{alpha}, {df}}},\\text{{ we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha={alpha*2}.")
elif type1 == 5:
	type2 = int(input("1. Null Hypothesis = \n2. Null Hypophesis \\ge"))
	print("The test hypothesis is")
	if type2 == 1:
		if delta0 == 0:
			print("\\\\\\text{Null Hypothesis }--> H_0: \\mu_1 = \\mu_2, or \\; H_0: \\mu_1 - \\mu_2 = 0")
		else:
			print("\\\\\\text{Null Hypothesis }--> H_0: \\mu_1 - \\mu_2 = \\Delta_0")
	elif type2 ==2:
		if delta0 == 0:
			print("\\\\\\text{Null Hypothesis }--> H_0: \\mu_1 \\ge \\mu_2, or \\; H_0: \\mu_1 - \\mu_2 \\ge 0")
		else:
			print("\\\\\\text{Null Hypothesis }--> H_0: \\mu_1 - \\mu_2 \\ge \\Delta_0")
	if delta0 == 0:
		print("\\\\\\text{Alternate Hypothesis }--> H_1: \\mu_1 < \\mu_2, or \\; H_1: \\mu_1 - \\mu_2 < 0")
	else:
		print("\\\\\\text{Alternate Hypothesis }--> H_1: \\mu_1 - \\mu_2 < \\Delta_0")
	print("Now, the value of test static can be found out by following formula: ")
	if var_type == 1:
		print("\\\\Z_0 = \\frac{\\bar{X_1} -\\bar{X_2} - \\Delta_0}{\\sqrt{\\frac{\\sigma_1^2}{n_1}+\\frac{\\sigma_2^2}{n_2}}}")
		print(f"\\\\Z_0 = \\frac{{{barx1}-{barx2}-{delta0}}}{{\\sqrt{{\\frac{{{var1}}}{{{n1}}}+\\frac{{{var2}}}{{{n2}}}}}}}")
		print(f"\\\\Z_0 = \\frac{{{barx1-barx2-delta0}}}{{\\sqrt{{{round(var1/n1, 4)}+{round(var2/n2, 4)}}}}}")
		print(f"\\\\Z_0 = \\frac{{{barx1-barx2-delta0}}}{{\\sqrt{{{round(var1/n1, 4)+round(var2/n2, 4)}}}}}")
		print(f"\\\\Z_0 = \\frac{{{barx1-barx2-delta0}}}{{{round(((var1/n1)+(var2/n2))**0.5, 4)}}}")
		zfinal = get_test_statistic_two_mean(barx1, barx2, delta0, var1, var2, n1, n2)
		print(f"\\\\Z_0 = {zfinal}")
		if pval == 1:
			print(f"Since P-value of a upper tailed test is equal to \\phi(|Z_0|)")
			print(f"\\\\P = \\phi({zfinal})")
			print(f"P = {round(st.norm.cdf(zfinal), 4)}")
			crit = st.norm.cdf(zfinal)
			if crit < alpha * 2:
				print(f"\\\\\\\\\\text{{Since P = {crit} < {alpha*2}, we reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ at }}\\alpha = {alpha*2}.")
			else:
				print(f"\\\\\\\\\\text{{Since P = {crit} > {alpha*2}, we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha = {alpha *2}")
		crit = round(st.norm.ppf(1 - (alpha * 2)), 4)
		print(f"\\\\\\\\\\text{{Critical value = }}z_{{\\alpha}} = z_{{{alpha*2}}} = {crit}")
		print(f"\\\\\\\\\\text{{Rejection Region: }}z_0 < -z_{{\\alpha}}")
		if zfinal < (-crit):
			print("\\\\\\\\\\text{Since }\\alpha = " + str(alpha * 2) + "\\text{, the boundaries of the critical region are }-Z_{" + str(alpha*2) + " = -" + str(crit) + "}\\text{ and we note that }Z_0\\text{ falls in the critical region. Therefore, }H_0\\text{ is rejected}")
		else:
			print("\\\\\\\\\\text{Since }\\alpha = " + str(alpha * 2) + "\\text{, the boundaries of the critical region are }-Z_{" + str(alpha*2) + " = -" + str(crit) + "}\\text{ and we note that }Z_0\\text{ does not falls in the critical region. Therefore, we fail to reject }H_0.")
	elif var_type == 2:
		variance_equality = int(input("1. If population variance are equal(If nothing is written about equality of population variance, most of the time they are equal)"))
		if variance_equality == 1:
			sp = get_sp_square(var1, var2, n1, n2)
			print(f"\\\\S_p^2 = \\frac{{(n_1-1)S_1^2+(n_2-1)S_2^2}}{{n_1+n_2-2}}")
			print(f"\\\\S_p^2 = \\frac{{({n1}-1){var1}+({n2}-1){var2}}}{{{n1}+{n2}-2}}")
			print(f"\\\\S_p^2 = \\frac{{({n1-1}){var1}+({n2-1}){var2}}}{{{n1+n2-2}}}")
			print(f"\\\\S_p^2 = \\frac{{{(n1-1)*var1}+{(n2-1)*var2}}}{{{n1+n2-2}}}")
			print(f"\\\\S_p^2 = {sp}")
			print(f"\\\\S_p = {math.sqrt(sp)}")
			print("Now, the value of test static can be found out by following formula: ")
			print("\\\\t_0 = \\frac{\\bar{X_1} -\\bar{X_2} - \\Delta_0}{S_p\\sqrt{\\frac{1}{n_1}+\\frac{1}{n_2}}}")
			print(f"\\\\t_0 = \\frac{{{barx1}-{barx2} - {delta0}}}{{{math.sqrt(sp)}\\sqrt{{\\frac{{1}}{{{n1}}}+\\frac{{1}}{{{n2}}}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{{math.sqrt(sp)}\\sqrt{{{round(1/n1,4)}+{round(1/n1,4)}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{{math.sqrt(sp)}\\sqrt{{{round((1/n1)+(1/n2),4)}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{{math.sqrt(sp)}({round(((1/n1)+(1/n2))**0.5,4)})}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{{round((((1/n1)+(1/n2))*sp)**0.5,4)}}}")
			zfinal = get_test_statistic_two_mean_unknown_var(barx1, barx2, delta0, math.sqrt(sp), n1, n2)
			print(f"\\\\t_0 = {zfinal}")
			if pval == 1:
				crit = st.t.cdf(zfinal, n1+n2-2)
				print(f"\\\\\\\\\\text{{Using Excel's function }}=T.DIST(t_0,n-1,TRUE)\\text{{, the P-value for }}t_0 = {zfinal}\\text{{ in an power-tailed t-test with {n1+n2-2} degrees of freedom can be computed as P = }}P(T_{{{n1+n2-2}}}<{zfinal})=T.DIST({zfinal},{n1+n2-2},TRUE)={crit}.")
				if crit < alpha * 2:
					print(f"\\\\\\\\\\text{{Since P = {crit} < {alpha*2}, we reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ at }}\\alpha = {alpha*2}.")
				else:
					print(f"\\\\\\\\\\text{{Since P = {crit} > {alpha*2}, we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha = {alpha *2}")
			print(f"Degrees of freedom on the t-test statistic are n1 + n2 - 2 = {n1} + {n2} - 2 = {n1+n2-2}")
			crit = round(st.t.ppf(1 - (alpha * 2), n1+n2-2), 4)
			print(f"This implies that")
			print(f"\\\\\\\\\\text{{Critical value = }}t_{{\\alpha, n_1+n_2-2}})= t_{{{alpha*2}, {n1+n2-2}}} = {crit}")
			print(f"\\\\\\\\\\text{{Rejection Region: }}t_0 < -t_{{\\alpha, n_1+n_2-2}}")
			if zfinal < (-crit):
				print(f"\\\\\\\\\\text{{Since }}t_0 = {zfinal}<-{crit}=-t_{{{alpha * 2}, {n1 + n2 - 2}}},\\text{{ we reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ at }}\\alpha = {alpha * 2}.")
			else:
				print(f"\\\\\\\\\\text{{Since }}t_0 = {zfinal}>-{crit}=-t_{{{alpha * 2}, {n1 + n2 - 2}}},\\text{{ we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha = {alpha * 2}.")
		else:
			print("Now, the value of test static can be found out by following formula: ")
			print("\\\\t_0 = \\frac{\\bar{X_1} -\\bar{X_2} - \\Delta_0}{\\sqrt{\\frac{S_1^2}{n_1}+\\frac{S_2^2}{n_2}}}")
			print(f"\\\\t_0 = \\frac{{{barx1}-{barx2} - {delta0}}}{{\\sqrt{{\\frac{{{var1}}}{{{n1}}}+\\frac{{{var2}}}{{{n2}}}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{\\sqrt{{{round(var1/n1,4)}+{round(var2/n1,4)}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{\\sqrt{{{round((var1/n1)+(var2/n2),4)}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{{round(((var1/n1)+(var2/n2))**0.5,4)}}}")
			zfinal = get_test_statistic_two_mean_unknown_inequal_var(barx1, barx2, delta0, var1, var2, n1, n2)
			print(f"\\\\t_0 = {zfinal}")
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
			if pval == 1:
				crit = 2 * st.t.cdf(-abs(zfinal), df)
				print(f"\\\\\\\\\\text{{Using Excel's function }}=T.DIST.2T(|t_0|,n-1)\\text{{, the P-value for }}t_0 = {zfinal}\\text{{ in an t-test with {n1+n2-2} degrees of freedom can be computed as P = }}P(T_{{{n1+n2-2}}}>{zfinal})=T.DIST.2T(|{zfinal}|,{n1+n2-2})={crit}.")
				if crit < alpha * 2:
					print(f"\\\\\\\\\\text{{We would reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ because P = }}{crit}<{alpha*2}")
				else:
					print(f"\\\\\\\\\\text{{Since P = {crit} > {alpha * 2},}}\\text{{ we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha = {alpha *2}")
			print(f"Degrees of freedom on the t-test statistic are \\nu = {df}")
			crit = round(st.t.ppf(1 - (alpha * 2), df), 4)
			print(f"This implies that")
			print(f"\\\\\\\\\\text{{Critical value = }}t_{{\\alpha, \\nu}})= t_{{{alpha*2}, {df}}} = {crit}")
			print(f"\\\\\\\\\\text{{Rejection Region: }}t_0 < -t_{{\\alpha, \\nu}}")
			if zfinal < (-crit):
				print(f"\\\\\\\\\\text{{Since }}t_0 = {zfinal}<-{crit}=-t_{{{alpha * 2}, {df}}},\\text{{ we reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ at }}\\alpha = {alpha * 2}.")
			else:
				print(f"\\\\\\\\\\text{{Since }}t_0 = {zfinal}>-{crit}=-t_{{{alpha * 2}, {df}}},\\text{{ we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha = {alpha * 2}.")
elif type1 == 6:
	type2 = int(input("1. Null Hypothesis =\n 2. Null Hypophesis \\le"))
	print("The test hypothesis is")
	if type2 == 1:
		if delta0 == 0:
			print("\\\\\\text{Null Hypothesis }--> H_0: \\mu_1 = \\mu_2, or \\; H_0: \\mu_1 - \\mu_2 = 0")
		else:
			print("\\\\\\text{Null Hypothesis }--> H_0: \\mu_1 - \\mu_2 = \\Delta_0")
	elif type2 ==2:
		if delta0 == 0:
			print("\\\\\\text{Null Hypothesis }--> H_0: \\mu_1 \\le \\mu_2, or \\; H_0: \\mu_1 - \\mu_2 \\le 0")
		else:
			print("\\\\\\text{Null Hypothesis }--> H_0: \\mu_1 - \\mu_2 \\le \\Delta_0")
	if delta0 == 0:
		print("\\\\\\text{Alternate Hypothesis }--> H_1: \\mu_1 > \\mu_2, or \\; H_1: \\mu_1 - \\mu_2 > 0")
	else:
		print("\\\\\\text{Alternate Hypothesis }--> H_1: \\mu_1 - \\mu_2 > \\Delta_0")
	print("This is a one-sided test because the alternative hypothesis is formulated to detect the difference from the hypothesized mean on the upper side")
	print("Now, the value of test static can be found out by following formula: ")
	if var_type == 1:
		print("\\\\Z_0 = \\frac{\\bar{X_1} -\\bar{X_2} - \\Delta_0}{\\sqrt{\\frac{\\sigma_1^2}{n_1}+\\frac{\\sigma_2^2}{n_2}}}")
		print(f"\\\\Z_0 = \\frac{{{barx1}-{barx2}-{delta0}}}{{\\sqrt{{\\frac{{{var1}}}{{{n1}}}+\\frac{{{var2}}}{{{n2}}}}}}}")
		print(f"\\\\Z_0 = \\frac{{{barx1-barx2-delta0}}}{{\\sqrt{{{round(var1/n1, 4)}+{round(var2/n2, 4)}}}}}")
		print(f"\\\\Z_0 = \\frac{{{barx1-barx2-delta0}}}{{\\sqrt{{{round(var1/n1, 4)+round(var2/n2, 4)}}}}}")
		print(f"\\\\Z_0 = \\frac{{{barx1-barx2-delta0}}}{{{round(((var1/n1)+(var2/n2))**0.5, 4)}}}")
		zfinal = get_test_statistic_two_mean(barx1, barx2, delta0, var1, var2, n1, n2)
		print(f"\\\\Z_0 = {zfinal}")
		if pval == 1:
			print("Since P-value of a upper tailed test is equal to (1 - \\phi(Z_0)")
			print(f"P = (1 - \\phi({zfinal}))")
			print(f"P = (1 - {st.norm.cdf(zfinal)})")
			print(f"P = {round(1 - st.norm.cdf(zfinal), 6)}")
			crit = 1 - st.norm.cdf(zfinal)
			if crit < alpha * 2:
				print(f"\\\\\\\\\\text{{Since P = {crit} < {alpha*2}, we reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ at }}\\alpha = {alpha*2}.")
			else:
				print(f"\\\\\\\\\\text{{Since P = {crit} > {alpha*2}, we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha = {alpha *2}")
		crit = round(st.norm.ppf(1 - (alpha * 2)), 4)
		print(f"\\\\\\\\\\text{{Critical value = }}z_{{\\alpha}} = z_{{{alpha*2}}} = {crit}")
		print(f"\\\\\\\\\\text{{Rejection Region: }}z_0 > z_{{\\alpha}}")
		if zfinal > crit :
			print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, z_\\alpha = z_{{{alpha * 2}}} = {crit}\\text{{. Since }}z_0 = {zfinal}>{crit}=z_{{{alpha*2}}},\\text{{ we reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ at }}\\alpha = {alpha * 2}.")
		else:
			print(f"\\\\\\\\\\text{{For }}\\alpha = {alpha * 2}, z_\\alpha = z_{{{alpha * 2}}} = {crit}\\text{{. Since }}z_0 = {zfinal}<{crit}=z_{{{alpha*2}}},\\text{{ we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha = {alpha * 2}.")
	elif var_type == 2:
		variance_equality = int(input("1. If population variance are equal(If nothing is written about equality of population variance, most of the time they are equal)"))
		if variance_equality == 1:
			sp = get_sp_square(var1, var2, n1, n2)
			print(f"\\\\S_p^2 = \\frac{{(n_1-1)S_1^2+(n_2-1)S_2^2}}{{n_1+n_2-2}}")
			print(f"\\\\S_p^2 = \\frac{{({n1}-1){var1}+({n2}-1){var2}}}{{{n1}+{n2}-2}}")
			print(f"\\\\S_p^2 = \\frac{{({n1-1}){var1}+({n2-1}){var2}}}{{{n1+n2-2}}}")
			print(f"\\\\S_p^2 = \\frac{{{(n1-1)*var1}+{(n2-1)*var2}}}{{{n1+n2-2}}}")
			print(f"\\\\S_p^2 = {sp}")
			print(f"\\\\S_p = {math.sqrt(sp)}")
			print("Now, the value of test static can be found out by following formula: ")
			print("\\\\t_0 = \\frac{\\bar{X_1} -\\bar{X_2} - \\Delta_0}{S_p\\sqrt{\\frac{1}{n_1}+\\frac{1}{n_2}}}")
			print(f"\\\\t_0 = \\frac{{{barx1}-{barx2} - {delta0}}}{{{math.sqrt(sp)}\\sqrt{{\\frac{{1}}{{{n1}}}+\\frac{{1}}{{{n2}}}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{{math.sqrt(sp)}\\sqrt{{{round(1/n1,4)}+{round(1/n1,4)}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{{math.sqrt(sp)}\\sqrt{{{round((1/n1)+(1/n2),4)}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{{math.sqrt(sp)}({round(((1/n1)+(1/n2))**0.5,4)})}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{{round((((1/n1)+(1/n2))*sp)**0.5,4)}}}")
			zfinal = get_test_statistic_two_mean_unknown_var(barx1, barx2, delta0, math.sqrt(sp), n1, n2)
			print(f"\\\\t_0 = {zfinal}")
			if pval == 1:
				crit = st.t.cdf(-zfinal, n1+n2-2)
				print(f"\\\\\\\\\\text{{Using Excel's function }}=T.DIST.RT(t_0,n-1)\\text{{, the P-value for }}t_0 = {zfinal}\\text{{ in an upper-tailed t-test with {n1+n2-2} degrees of freedom can be computed as P = }}P(T_{{{n1+n2-2}}}>{zfinal})=T.DIST.RT({zfinal},{n1+n2-2})={crit}.")
				if crit < alpha * 2:
					print(f"\\\\\\\\\\text{{Since P = {crit} < {alpha*2}, we reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ at }}\\alpha = {alpha*2}.")
				else:
					print(f"\\\\\\\\\\text{{Since P = {crit} > {alpha*2}, we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha = {alpha *2}")
			print(f"Degrees of freedom on the t-test statistic are n1 + n2 - 2 = {n1} + {n2} - 2 = {n1+n2-2}")
			crit = round(st.t.ppf(1 - (alpha * 2), n1+n2-2), 4)
			print(f"This implies that")
			print(f"\\\\\\\\\\text{{Critical value = }}t_{{\\alpha, n_1+n_2-2}} = t_{{{alpha*2}, {n1+n2-2}}} = {crit}")
			print(f"\\\\\\\\\\text{{Rejection Region: }}t_0 > t_{{\\alpha, n_1+n_2-2}}")
			if zfinal > (crit):
				print(f"\\\\\\\\\\text{{Since }}t_0 = {zfinal}>{crit}=t_{{{alpha * 2}, {n1 + n2 - 2}}},\\text{{ we reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ at }}\\alpha = {alpha * 2}.")
			else:
				print(f"\\\\\\\\\\text{{Since }}t_0 = {zfinal}<{crit}=t_{{{alpha * 2}, {n1 + n2 - 2}}},\\text{{ we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha = {alpha * 2}.")
		else:
			print("Now, the value of test static can be found out by following formula: ")
			print("\\\\t_0 = \\frac{\\bar{X_1} -\\bar{X_2} - \\Delta_0}{\\sqrt{\\frac{S_1^2}{n_1}+\\frac{S_2^2}{n_2}}}")
			print(f"\\\\t_0 = \\frac{{{barx1}-{barx2} - {delta0}}}{{\\sqrt{{\\frac{{{var1}}}{{{n1}}}+\\frac{{{var2}}}{{{n2}}}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{\\sqrt{{{round(var1/n1,4)}+{round(var2/n1,4)}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{\\sqrt{{{round((var1/n1)+(var2/n2),4)}}}}}")
			print(f"\\\\t_0 = \\frac{{{barx1-barx2 - delta0}}}{{{round(((var1/n1)+(var2/n2))**0.5,4)}}}")
			zfinal = get_test_statistic_two_mean_unknown_inequal_var(barx1, barx2, delta0, var1, var2, n1, n2)
			print(f"\\\\t_0 = {zfinal}")
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
			if pval == 1:
				crit = 2 * st.t.cdf(-abs(zfinal), df)
				print(f"\\\\\\\\\\text{{Using Excel's function }}=T.DIST.2T(|t_0|,n-1)\\text{{, the P-value for }}t_0 = {zfinal}\\text{{ in an t-test with {n1+n2-2} degrees of freedom can be computed as P = }}P(T_{{{n1+n2-2}}}>{zfinal})=T.DIST.2T(|{zfinal}|,{n1+n2-2})={crit}.")
				if crit < alpha * 2:
					print(f"\\\\\\\\\\text{{We would reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ because P = }}{crit}<{alpha*2}")
				else:
					print(f"\\\\\\\\\\text{{Since P = {crit} > {alpha * 2},}}\\text{{ we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha = {alpha *2}")
			print(f"Degrees of freedom on the t-test statistic are \\nu = {df}")
			crit = round(st.t.ppf(1 - (alpha * 2), n1+n2-2), 4)
			print(f"This implies that")
			print(f"\\\\\\\\\\text{{Critical value = }}t_{{\\alpha, \\nu}} = t_{{{alpha*2}, {df}}} = {crit}")
			print(f"\\\\\\\\\\text{{Rejection Region: }}t_0 > t_{{\\alpha, \\nu}}")
			if zfinal > (crit):
				print(f"\\\\\\\\\\text{{Since }}t_0 = {zfinal}>{crit}=t_{{{alpha * 2}, {df}}},\\text{{ we reject the null hypothesis }}H_0\\text{{ in favor of the alternative hypothesis }}H_1\\text{{ at }}\\alpha = {alpha * 2}.")
			else:
				print(f"\\\\\\\\\\text{{Since }}t_0 = {zfinal}<{crit}=t_{{{alpha * 2}, {df}}},\\text{{ we fail to reject the null hypothesis }}H_0\\text{{ at }}\\alpha = {alpha * 2}.")
print("Please hit thumbs up if the answer helped you.")
