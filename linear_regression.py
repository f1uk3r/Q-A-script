import math
import matplotlib.pyplot as plt
import scipy.stats as st
from tabulate import tabulate
import webbrowser

def a(x, y, xy, xx, n):
	return round(((y * xx) - (x * xy)) / ((n * xx) - (x*x)), 4)

def b(x, y, xy, xx, n):
	return round(((n * xy) - (x * y)) / ((n * xx) - (x*x)), 4)

def r(x, y, xy, xx, yy, n):
	return round(((n * xy) - (x * y)) / math.sqrt(((n * xx) - (x*x)) * ((n * yy) - (y*y))), 4)

def square(list):
	neo = []
	sq = 0
	for i in range(len(list)):
		neo.append(round(list[i] ** 2, 4))
	return neo

def mul(list1, list2):
	neo = []
	for i in range(len(list1)):
		neo.append(round(list1[i] * list2[i], 4))
	return neo

def sub(list1, list2):
	neo = []
	for i in range(len(list1)):
		neo.append(round(list1[i] - list2[i], 8))
	return neo

def yforline(list, a, b):
	neo = []
	for i in range(len(list)):
		neo.append(round(a + b * list[i], 8))
	return neo

def estimate(a, b):
	return round(math.sqrt(a / b), 4)

print('''
Legend for option 
1. for regression\n2. for correlation \n3. Scatter plot 
4. Line Graph \n5. Scatterplot and Line graph \n6. Residual for one value
7. Residual Table \n8. Scatterplot of residual 
9. Residual sum of squares or error sum of square and estimation of variance
10. Question with six parts 
11. Coefficient of determination r^2 (Calculated by squaring r)
12. Testing Correlation's significance
13. SST=S_{yy}(total sum of square) SSR(regression sum of squares) SSE(residual sum of squares)
14. estimated variance (using sst and ssr)
15. Confidence interval on the slope beta_1
16. Confidence interval on the intercept beta_0
''')

parts = int(input("How many parts: "))
xs = list(map(float, input("Input all the values of x: ").split()))
ys = list(map(float, input("Input all the values of y: ").split()))
xys = mul(xs, ys)
xxs = square(xs)
yys = square(ys)


header = ["X", "Y", "XY", "XX", "YY"]
table = zip(xs, ys, xys, xxs, yys)
print(tabulate((table), header, tablefmt="latex"))

n = len(xs)
x = round(sum(xs), 4)
y = round(sum(ys), 4)
ysq = y**2
xy = round(sum(xys), 4)
xx = round(sum(xxs), 4)
yy = round(sum(yys), 4)
xbar = round(x/n, 4)
ybar = round(y/n, 4)

df = n - 2
sst = yy - (ysq/n)
ssrnum = (xy - (x*y/n))**2
ssrden = xx-(x**2/n)
ssr = ssrnum/ssrden
sec = 97

a1 = a(x, y, xy, xx, n)
b1 = b(x, y, xy, xx, n)
r1 = r(x, y, xy, xx, yy, n)
r2 = round(r1 * r1, 4)

somey = yforline(xs, a1, b1)
es = sub(ys, somey)
ees = square(es)

ee = round(sum(ees),4)

sxx = round(xx - (x*x/n), 4)
seb = round((((sst-ssr)/(n-2))/sxx)**0.5, 4)

print ("\\\\ \sum X =" + str(x) + ", \sum Y =" + str(y) + "\\\\ \sum XY =" + str(xy) + ", \sum XX =" + str(xx) + ", \sum YY =" + str(yy))
for i in range(parts):
	option = int(input("Choose type from legend: "))
	if option == 1:
		print (f"\\\\{chr(sec)}) \\hat y = a + bx")
		sec += 1
		print ("\\\\ a = \\frac{\\sum Y * \\sum XX-\sum X*\\sum XY}{n\\sum X^2 -(\\sum X)^2}")
		print ("\\\\ a = \\frac{" + str(y) + "*" + str(xx) + " - " + str(x) + "*" + str(xy) + "}{" + str(n) + "*" + str(xx) + " - " + str(x) + "*" + str(x) + "} \\approx " + str(a1))
		print ("\\\\ b = \\frac{n\\sum XY -\\sum X*\\sum Y}{n\\sum X^2 -(\\sum X)^2}")
		print ("\\\\ b = \\frac{" + str(n) + "*" + str(xy) + " - " + str(x) + "*" + str(y) + "}{" + str(n) + "*" + str(xx) + " - " + str(x) + "*" + str(x) + "} \\approx " + str(b1))
		if b1>0:
			print (f"\\\\ \\hat y = {a1} + {b1}x")
		else:
			print(f"\\\\ \\hat y = {a1} {b1}x")
		est = int(input("Press 0 if no estimation part, press number of parts if there are any estimation parts: "))
		for i in range(est):
			xhat = float(input("x = "))
			if b1>0:
				print(f"\\\\ \\hat y = {a1} + {b1}({xhat})")
			else:
				print(f"\\\\ \\hat y = {a1} {b1}({xhat})")
			yhat = round(a1 + (b1 * xhat), 4)
			print (f"\\\\ \\hat y = {yhat}")

	elif option == 2:
		print (chr(sec) + ")\\\\ r = \\frac{n\sum XY -\sum X*\sum Y}{\sqrt{\left(n\sum X^2 -(\sum X)^2\\right)\left(n\sum Y^2 -(\sum Y)^2\\right)}}")
		sec += 1
		print ("\\\\ r = \\frac{" + str(n) + "*" + str(xy) + " - " + str(x) + "*" + str(y) + "}{ \sqrt{(" + str(n) + "*" + str(xx) + " - " + str(x) + "^2)(" + str(n) + "*" + str(yy) + " - " + str(y) + "^2)}} \\approx " + str(r1))

	elif option == 3:
		print(chr(sec) + ")")
		sec += 1
		plt.scatter(xs, ys)
		plt.savefig('chegg.png', bbox_inches='tight')
		plt.close()

	elif option == 4:
		print(chr(sec) + ")")
		sec += 1
		plt.plot(xs, somey)
		plt.savefig('chegg2.png', bbox_inches='tight')
		plt.close()

	elif option == 5:
		print(chr(sec) + ")")
		sec += 1
		plt.scatter(xs, ys)
		plt.plot(xs, somey)
		plt.savefig('chegg3.png', bbox_inches='tight')
		plt.close()

	elif option == 6:
		xhat = float(input(chr(sec) + ") x = "))
		sec += 1
		index = xs.index(xhat)
		print ("\\\\ \hat y = " + str(a1) + "+" + str(b1) + "(" + str(xhat) + ")")
		yhat = somey[index]
		yold = ys[index]
		print ("\\\\ \hat y = " + str(yhat))
		print ("\\\\Residual (e)= y-\hat{y}")
		print ("e = " + str(yold) + "- " + str(yhat))
		print ("e = " + str(round(yold - yhat, 4)))

	elif option == 7:
		print(chr(sec) + ")")
		sec += 1
		print ("\\\\Residual (e)= y-\hat{y}")
		header = ["X", "Y", "^Y", "e"]
		table = zip(xs, ys, somey, es)
		print(tabulate((table), header, tablefmt="latex"))

	elif option == 8:
		print(chr(sec) + ")")
		sec += 1
		plt.scatter(xs, es)
		plt.savefig('chegg4.png', bbox_inches='tight')
		plt.close()
	
	elif option == 10:
		print(chr(sec) + ")")
		sec += 1
		plt.scatter(xs, ys)
		plt.savefig('chegg.png', bbox_inches='tight')
		plt.close()
		print(chr(sec) + ")")
		sec += 1
		print ("\\\\ \sum X =" + str(x) + "\\\\ \sum Y =" + str(y) + "\\\\ \sum XY =" + str(xy) + "\\\\ \sum XX =" + str(xx) + "\\\\ \sum YY =" + str(yy))
		print ("\\\\ r = \\frac{n\sum XY -\sum X*\sum Y}{\sqrt{\left(n\sum X^2 -(\sum X)^2\\right)\left(n\sum Y^2 -(\sum Y)^2\\right)}}")
		print ("\\\\ r = \\frac{" + str(n) + "*" + str(xy) + " - " + str(x) + "*" + str(y) + "}{ \sqrt{(" + str(n) + "*" + str(xx) + " - " + str(x) + "^2)(" + str(n) + "*" + str(yy) + " - " + str(y) + "^2)}} \\approx " + str(r1))
		print(chr(sec) + ")")
		sec += 1
		print("\\\\ \\bar{x} = " + str(xbar))		
		print("\\\\ \\bar{y} = " + str(ybar))
		print ("\\\\ \hat y = a + bx")
		print ("\\\\ a = \\frac{\sum Y * \sum XX-\sum X*\sum XY}{n\sum X^2 -(\sum X)^2}")
		print ("\\\\ a = \\frac{" + str(y) + "*" + str(xx) + " - " + str(x) + "*" + str(xy) + "}{" + str(n) + "*" + str(xx) + " - " + str(x) + "*" + str(x) + "} \\approx " + str(a1))
		print ("\\\\ b = \\frac{n\sum XY -\sum X*\sum Y}{n\sum X^2 -(\sum X)^2}")
		print ("\\\\ b = \\frac{" + str(n) + "*" + str(xy) + " - " + str(x) + "*" + str(y) + "}{" + str(n) + "*" + str(xx) + " - " + str(x) + "*" + str(x) + "} \\approx " + str(b1))
		print ("\\\\ \hat y = " + str(a1) + "+" + str(b1) + "x")
		print(chr(sec) + ")")
		sec += 1
		plt.plot(xbar, ybar, 'ro')
		plt.plot(xs, somey)
		plt.savefig('chegg3.png', bbox_inches='tight')
		plt.close()
		print(f"\\\\{chr(sec)}) r^2 = " + str(r1) + "^2")
		print("\\\\ r^2 = " + str(round(r1 * r1, 3)))
		print("\\\\ explained = " + str(round(r2 * 100, 1)))
		print("\\\\ unexplained = " + str(round(100 - (r2 * 100), 1)))
		sec += 1
		xhat = float(input(f"{chr(sec)}) x = "))
		sec += 1
		print ("\\\\ \hat y = " + str(a1) + "+" + str(b1) + "(" + str(xhat) + ")")
		yhat = round(a1 + (b1 * xhat), 4)
		print ("\\\\ \hat y = " + str(yhat))
	
	elif option == 9:
		print(chr(sec) + ")")
		sec += 1
		header = ["X", "Y", "^Y", "Y-^Y", "(Y-^Y)(Y-^Y)"]
		table = zip(xs, ys, somey, es, ees)
		print(tabulate((table), header, tablefmt="latex"))
		print("\\\\\\sum (Y-\\hat{Y})^2 = " + str(ee))
		print ("\\\\Mean\\ Square\\ Error(\\hat{\\sigma}^2) = \\frac{\sum (Y-\hat{Y})^2}{n-2}")
		print ("\\\\n = " + str(n))
		print ("\\\\Mean\\ Square\\ Error(\\hat{\\sigma}^2) = \\frac{" + str(ee) + "}{" + str(n) + "-2}")
		print ("\\\\Mean\\ Square\\ Error(\\hat{\\sigma}^2) =" + str(estimate(ee, n-2)))
	
	elif option == 11:
		print(f"{chr(sec)}) Coefficient of Determination(R-squared):")
		sec += 1
		print(f"It gives the measure of how close the data points are to the best fit line. In other words, it gives the proportion of variability in dependent variable that can be explained by the independent variable. Higher the Rsquared value, better the model is.")
		print("\\\\ r^2 = " + str(r1) + "^2")
		print("\\\\ r^2 = " + str(round(r1 * r1, 3)))
	elif option == 12:
		print("Since, we know that")
		print("Degree of freedom (df) can be found out by n-2, where n is number of data points")
		print("df = n-2")
		print("df = " + str(n) + "-2")
		print("df = " + str(df))
		alpha = float(input("\\alpha = "))
		webbrowser.open('https://www.statisticssolutions.com/table-of-critical-values-pearson-correlation/')
		crit = float(input("critical value @ (df = " + str(df) + " and \\alpha = " + str(alpha) + ") = "))
		if r1 < -crit:
			print("Since, r = " + str(r1) + " is less than -" + str(crit) + ". Therefore, r is significant")
		elif r1 > crit:
			print("Since, r = " + str(r1) + " is greater than " + str(crit) + ". Therefore, r is significant")
		else:
			print("Since, r = " + str(r1) + " is between -" + str(crit) + " and " + str(crit) + ". Therefore, r is not significant")
	elif option == 13:
		print(f"\\\\SST = \\sum Y^2 - \\frac{{(\\sum Y)^2}}{{n}}")
		print(f"\\\\SST = {yy} - \\frac{{({y})^2}}{{{n}}}")
		print(f"\\\\SST = {yy} - \\frac{{{y**2}}}{{{n}}}")
		print(f"\\\\SST = {yy} - {ysq/n}")
		print(f"\\\\SST = {sst}")
		print(f"\\\\SSR = \\frac{{(\\sum XY - \\frac{{\\sum X\\sum Y}}{{n}})^2}}{{\\sum X^2 - \\frac{{(\\sum X)^2}}{{n}}}}")
		print(f"\\\\SSR = \\frac{{({xy} - \\frac{{{x}({y})}}{{{n}}})^2}}{{{xx} - \\frac{{({x})^2}}{{{n}}}}}")
		print(f"\\\\SSR = \\frac{{({xy} - {x*y/n})^2}}{{{xx} - {x**2/n}}}")
		print(f"\\\\SSR = \\frac{{{ssrnum}}}{{{ssrden}}}")
		print(f"\\\\SSR = {ssr}")
		print(f"\\\\SSE = SST - SSR")
		print(f"\\\\SSE = {sst} - {ssr}")
		print(f"\\\\SSE = {sst - ssr}")
	elif option == 14:
		print(f"\\hat{{\\sigma}}^2 = \frac{{SS_E}}{{n-2}}")
		print(f"\\hat{{\\sigma}}^2 = \frac{{SS_T - SS_R}}{{n-2}}")
		print(f"\\hat{{\\sigma}}^2 = \frac{{{sst}-{ssr}}}{{{n}-2}}")
		print(f"\\hat{{\\sigma}}^2 = \frac{{{sst-ssr}}}{{{n-2}}}")
		print(f"\\hat{{\\sigma}}^2 = {(sst-ssr)/(n-2)}")
	elif option == 15:
		ci = float(input("Confidence Interval (in %) = "))
		t = round(st.t.ppf(1-((1-(ci/100))/2), n-2), 4)
		print(f"\\\\\\alpha = {round(1-(ci/100), 4)} and d.f. = n-2 = {n-2}")
		print(f"\\\\t_{{\\alpha/2, n-2}} = t_{{{round((1-(ci/100))/2,4)}, {n-2}}} = {t}")
		print ("\\\\ \\hat{\\beta}_1 = \\frac{n\\sum XY -\\sum X*\\sum Y}{n\\sum X^2 -(\\sum X)^2}")
		print ("\\\\ \\hat{\\beta}_1 = \\frac{" + str(n) + "*" + str(xy) + " - " + str(x) + "*" + str(y) + "}{" + str(n) + "*" + str(xx) + " - " + str(x) + "*" + str(x) + "} \\approx " + str(b1))
		print("\\\\S.E.(\\hat{\\beta}_1) =\\ standard\\ error\\ of\\ \\hat{\\beta}_1 = \\sqrt{\\frac{\\sigma^2}{S_{xx}}}")
		print(f"\\\\Where,\\ \\sigma^2 = \\hat{{\\sigma}}^2 = {(sst-ssr)/(n-2)}")
		print(f"\\\\And,\\ S_{{xx}} = \\sum X^2 -\\frac{{(\\sum X)^2}}{{n}}")
		print(f"\\\\S_{{xx}} = {xx} -\\frac{{({x})^2}}{{{n}}}")
		print(f"\\\\S_{{xx}} = {sxx}")
		print(f"\\\\So,\\ S.E.(\\hat{{\\beta}}_1) =\\sqrt{{\\frac{{{(sst-ssr)/(n-2)}}}{{{sxx}}}}}")
		print(f"\\\\S.E.(\\hat{{\\beta}}_1) = {seb}")
		print("Since we know that")
		print("\\\\\\beta_1 - t_{\\alpha/2, n-2}*S.E.(\\hat{\\beta}_1) < \\beta_1 < \\beta_1 + t_{\\alpha/2, n-2}*S.E.(\\hat{\\beta}_1)")
		print(f"\\\\{b1}- {t}*{seb} < \\beta_1 < {b1} + {t}*{seb}")
		print(f"\\\\{b1}- {round(t*seb,4)} < \\beta_1 < {b1} + {round(t*seb,4)}")
		print(f"\\\\ {round(b1 - (t*seb),4)} < \\beta_1 < {round(b1 + (t*seb),4)}")
	elif option == 16:
		ci = float(input("Confidence Interval (in %) = "))
		t = round(st.t.ppf(1-((1-(ci/100))/2), n-2), 4)
		print(f"\\\\\\alpha = {round(1-(ci/100), 4)} and d.f. = n-2 = {n-2}")
		print(f"\\\\t_{{\\alpha/2, n-2}} = t_{{{round((1-(ci/100))/2,4)}, {n-2}}} = {t}")
		print ("\\\\ \\beta_0 = \\frac{\\sum Y * \\sum XX-\sum X*\\sum XY}{n\\sum X^2 -(\\sum X)^2}")
		print ("\\\\ \\beta_0 = \\frac{" + str(y) + "*" + str(xx) + " - " + str(x) + "*" + str(xy) + "}{" + str(n) + "*" + str(xx) + " - " + str(x) + "*" + str(x) + "} \\approx " + str(a1))
		
print("Please hit thumps up if the answer helped you")
