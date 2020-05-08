import math
from tabulate import tabulate
import matplotlib.pyplot as plt
import scipy.stats as st

def mean(list):
	return round(sum(list) / len(list), 4)

def median(list):
	n = len(list)
	if len(list)%2 == 0:
		return round((list[int(n/2)] + list[int((n/2) - 1)]) / 2, 4)
	else:
		return round(list[int((n - 1) / 2)], 4) 

def splitlist(list):
	list1 = []
	list2 = []
	if len(list)%2 == 0:
		list1 = list[0:int((len(list)/2))]
		list2 = list[int((len(list)/2)):int(len(list))]
		return list1, list2
	else:
		list1 = list[0:int((len(list) - 1) / 2)]
		list2 = list[int((len(list) + 1) / 2):int(len(list))]
		return list1, list2

def var(list, xbar):
	neo = []
	for i in range(len(list)):
		neo.append(round(list[i] - xbar, 4))
	return neo

def square(list):
	neo = []
	for i in range(len(list)):
		neo.append(round(list[i] ** 2, 4))
	return neo

def variance(sumsquare, n):
	return round(sumsquare / (n-1), 4)

def stddev(s2):
	return round(math.sqrt(s2), 4)

def coefOfVar(mean, std):
	return round(std / mean, 4)

def boundOutliers(q1, q3, iqr):
	lowBound = round(q1 - (1.5 * iqr), 4)
	uppBound = round(q3 + (1.5 * iqr), 4)
	return lowBound, uppBound

def stemAndLeaf(list):
	stemLeaflist = []
	#if list[0] % 1 == float(0.0) and list[1] % 1 == float(0.0) and list[2] % 1 == float(0.0):
	for i in range(len(list)):
		stem = int(list[i] // 10)
		leaf = int(list[i] % 10)
		if len(stemLeaflist) == 0:
			stemLeaflist.append({"stem": stem, "leaf": [leaf]})
		else:
			for j in range(len(stemLeaflist)):
				if stem == stemLeaflist[j]["stem"]:
					stemLeaflist[j]["leaf"].append(leaf)
				elif j == len(stemLeaflist) - 1:
					stemLeaflist.append({"stem": stem, "leaf": [leaf]})
	"""else:
		for i in range(len(list)):
			leaf, stem = math.modf(2.5)
			stem = int(stem)
			for j in range(len(stemLeafList)):
				if stem == stemLeafList[j]["stem"]:
					stemLeaflist[j]["leaf"].append(leaf)
				elif j == len(stemLeaflist) - 1:
					stemLeaflist.append({"stem": stem, "leaf": [leaf]})"""
	return stemLeaflist

def error(z, sd, n):
	return round((z * sd) / math.sqrt(n), 4)

def errort2(t, s1, s2, n1, n2):
	return round(t * (math.sqrt((((n1 - 1) * (s1 ** 2)) + ((n2 - 1) * (s2 ** 2))) / (n1 + n2 - 2))) * (math.sqrt((1/n1) + (1/n2))), 4)

def error2(z, s1, s2, n1, n2):
	return round(z * math.sqrt(((s1 ** 2) / n1) + ((s2 ** 2) / n2)), 4)

print(f"""Legend for types
1. Mean
2. Median
3. Range 
4. Variance 
5. Standard Deviation 
6. Quartile 1 and 3 
7. Maximum and minimum 
8. Interquartile Range
9. Coefficient of Variation
10. Finding all outliers
11. Pearson’s Coefficient of Skewness
12. Stem and Leaf Diagram
13. Box Plot
14. Mode
15. Confidence Interval one mean
16. Confidence Interval two means
17. Five Point Summary
18. Percentile""")
parts = int(input("How many parts: "))
xs = list(map(float, input("Input all the values of x: ").split()))
xbar = mean(xs)													#Mean of list
xinc = sorted(xs)												#List in increasing order
med = median(xinc)												#Median of list	
xmxbar = var(xs, xbar)				
xmxbarsq = square(xmxbar)
mode = max(set(xs), key=xs.count)
print(mode)
n = len(xs)														#length of list
xsumsquare = round(sum(xmxbarsq), 4)							
lh, uh = splitlist(xinc)										#Splitted lists for Q1, Q3 calculation
s2 = variance(xsumsquare, n)									#Variance
s = stddev(s2)													#Standard Deviation
Q1 = median(lh)													#Lower Quartile
Q3 = median(uh)													#Upper Quartile
IQR = Q3 - Q1													#Inter Quartile Range
cv = coefOfVar(xbar, s)											#Coefficient of Variance

sec = 97
print(xs)
print(xinc)

header = ["X", "X - mean", "(X-mean)^2"]
table = zip(xs, xmxbar, xmxbarsq)
print(tabulate((table), header, tablefmt="latex"))

for i in range(parts):
	ty = int(input("Type of part: "))
	if ty == 1:
		print(chr(sec) + ") Since we know that")
		sec += 1
		print("\\\\Mean(\\bar{x}) = \\frac{\\sum_{i=1}^n x_i}{n}")
		print("\\\\Where\\ n\\ is\\ the\\ number\\ of\\ data\\ points")
		print("\\\\Now")
		print("\\\\\\sum_{i=1}^n x_i = " + str(sum(xs)))
		print("\\\\and\\ n = " + str(n))
		print("\\\\This\\ implies\\ that")
		print("\\\\Mean(\\bar{x}) = \\frac{" + str(sum(xs)) + "}{" + str(n) + "}")
		print("\\\\Mean(\\bar{x}) = " + str(xbar))
	if ty == 2:
		print(chr(sec) + ") Since we know that")
		sec += 1
		print("Median for a list of even number of data point is the mean of 2 middle most values if we sort the list in increasing order while for a list of odd number it is the middle most value if the list is sorted in increasing order.")
		if len(xs)%2 == 0:
			print("Since our list have even number of data points, this implies that")
			print("Median = " + str(med))
		else:
			print("Since our list have odd number of data points, this implies that")
			print("Median = " + str(med))
	if ty == 3:
		print(chr(sec) + ") Since we know that")
		sec += 1
		print("The range is the difference between the largest and smallest values in a set of values.")
		print("This implies that")
		print("Range = " + str(xinc[-1]) + "-" + str(xinc[0]))
		print("Range = " + str(xinc[-1] - xinc[0]))
	if ty == 4:
		print(chr(sec) + ") Since we know that")
		sec += 1
		print("\\\\Variance(s^2) = \\frac{(\sum{x_i - \\bar{x}})^2}{n-1}")
		print("\\\\(\sum{x_i - \\bar{x}})^2 = " + str(xsumsquare))
		print("\\\\n = " + str(n))
		print("\\\\Variance(s^2) = \\frac{" + str(xsumsquare) + "}{" + str(n-1) + "}")
		print("\\\\Variance(s^2) = " + str(s2))
	if ty == 5:
		print("\\\\" + chr(sec) + ")\\ Since\\ we\\ know\\ that")
		sec += 1
		print("\\\\Variance(s^2) = \\frac{(\sum{x_i - \\bar{x}})^2}{n-1}")
		print("\\\\(\sum{x_i - \\bar{x}})^2 = " + str(xsumsquare))
		print("\\\\n = " + str(n))
		print("\\\\Variance(s^2) = \\frac{" + str(xsumsquare) + "}{" + str(n-1) + "}")
		print("\\\\Variance(s^2) = " + str(s2))
		print("\\\\Standard\;Deviation(s) = \sqrt{Variance}")
		print("\\\\Standard\;Deviation(s) = " + str(s))                      
	if ty == 6:
		print(chr(sec) + ") Since we know that")
		sec += 1
		print("The lower quartile(Q1) is the median of the lower half of the data set while upper quartile(Q3) is the median of the upper half of the data set.")
		print("Also, median for a list of even number of data point is the mean of 2 middle most values if we sort the list in increasing order while for a list of odd number it is the middle most value if the list is sorted in increasing order.")
		if len(xs)%2 == 0:
			print("Since our list have even number of data points, this implies that")
			print("Median = " + str(med))
			print("Lower half of our list is " + str(lh))
			print("Since our lower half list have even number of data points, this implies that")
			print("Q1 = " + str(Q1))
			print("Upper half of our list is " + str(uh))
			print("Since our upper half list have even number of data points, this implies that")
			print("Q3 = " + str(Q3))
		else:
			print("Since our list have odd number of data points, this implies that")
			print("Median = " + str(med))
			print("Lower half of our list is " + str(lh))
			print("Since our lower half list have even number of data points, this implies that")
			print("Q1 = " + str(Q1))
			print("Upper half of our list is " + str(uh))
			print("Since our upper half list have even number of data points, this implies that")
			print("Q3 = " + str(Q3))
	if ty == 7:
		print(chr(sec) + ") The maximum and the minimum values are as follows")
		print("Maximum value = " + str(xinc[-1]))
		print("Minimum value = " + str(xinc[0]))
	if ty == 8:
		print(chr(sec) + "Interquartile range is equal to the distance between quartile 1(Q1) and quartile 3(Q3).")
		print("IQR = Q3 - Q2")
		print("IQR = " + str(Q3) + "-" + str(Q1))
		print("IQR = " + str(IQR))
	if ty == 9:
		print("Mean(\\bar{x}) = \\frac{\sum_{i=1}^n x_i}{n}")
		print("Where n is the number of data points")
		print("Now")
		print("\sum_{i=1}^n x_i = " + str(sum(xs)))
		print("and n = " + str(n))
		print("This implies that")
		print("\\\\Mean(\\bar{x}) = \\frac{" + str(sum(xs)) + "}{" + str(n) + "}")
		print("\\\\Mean(\\bar{x}) = " + str(xbar))
		print("\\\\Variance(s^2) = \\frac{(\sum{x_i - \\bar{x}})^2}{n-1}")
		print("\\\\(\sum{x_i - \\bar{x}})^2 = " + str(xsumsquare))
		print("n = " + str(n))
		print("\\\\Variance(s^2) = \\frac{" + str(xsumsquare) + "}{" + str(n-1) + "}")
		print("\\\\Variance(s^2) = " + str(s2))
		print("\\\\Standard\;Deviation(s) = \sqrt{Variance}")
		print("\\\\Standard\;Deviation(s) = " + str(s))
		print(chr(sec) + ") Coefficient of variance can be coumputed by dividing mean from the standard deviation.")
		sec += 1
		print("\\\\CV = \\frac{Standard\;Deviation}{Mean} ")
		print("\\\\CV = \\frac{" + str(s) + "}{" + str(xbar) + "}" )
		print("CV = "+ str(cv))
	if ty == 10:
		print("Since we know that")
		print("Also, median for a list of even number of data point is the mean of 2 middle most values if we sort the list in increasing order while for a list of odd number it is the middle most value if the list is sorted in increasing order.")
		if len(xs)%2 == 0:
			print("Since our list have even number of data points, this implies that")
			print("Median = " + str(med))
			print("The lower quartile(Q1) is the median of the lower half of the data set while upper quartile(Q3) is the median of the upper half of the data set.")
			print("Lower half of our list is " + str(lh))
			print("Since our lower half list have even number of data points, this implies that")
			print("Q1 = " + str(Q1))
			print("Upper half of our list is " + str(uh))
			print("Since our upper half list have even number of data points, this implies that")
			print("Q3 = " + str(Q3))
		else:
			print("Since our list have odd number of data points, this implies that")
			print("Median = " + str(med))
			print("The lower quartile(Q1) is the median of the lower half of the data set while upper quartile(Q3) is the median of the upper half of the data set.")
			print("Lower half of our list is " + str(lh))
			print("Since our lower half list have even number of data points, this implies that")
			print("Q1 = " + str(Q1))
			print("Upper half of our list is " + str(uh))
			print("Since our upper half list have even number of data points, this implies that")
			print("Q3 = " + str(Q3))
		print("Interquartile range is equal to the distance between quartile 1(Q1) and quartile 3(Q3).")
		print("IQR = Q3 - Q2")
		print("IQR = " + str(Q3) + "-" + str(Q1))
		print("IQR = " + str(IQR))
		lower, high = boundOutliers(Q1, Q3, IQR)
		print("Since we know that the outliers are those points in the data set which are either less than 1.5 times the IQR from Quartile 1 or more than 1.5 times the IQR from Quartile 3")
		print(f"lower bound = {Q1} - 1.5 * {IQR}")
		print(f"lower bound = {Q1} - {1.5 * IQR}")
		print(f"lower bound = {lower}")
		print(f"upper bound = {Q3} + 1.5 * {IQR}")
		print(f"upper bound = {Q3} + {1.5 * IQR}")
		print(f"upper bound = {high}")
		print("Therefore following points are outliers")
		for each in xs:
			if float(each)<lower or float(each)>high:
				print(str(each), end=", ")
		print(" ")
	if ty == 11:
		print("Pearson’s Coefficient of Skewness (Sk) = \\frac{\\bar{x} - Mo}{s}")
		print("Pearson’s Coefficient of Skewness (Sk) = \\frac{" + str(xbar) + " - " + str(mode) + "}{" + str(s) + "}")
		print("Pearson’s Coefficient of Skewness (Sk) = " + str(round((xbar - mode) / s, 4)))
		print("Pearson’s Coefficient of Skewness (Sk) = \\frac{3(\\bar{x} - Median)}{s}")
		print("Pearson’s Coefficient of Skewness (Sk) = \\frac{3(" + str(xbar) + " - " + str(med) + ")}{" + str(s) + "}")
		print("Pearson’s Coefficient of Skewness (Sk) = " + str(round((3*(xbar - med)) / s, 4)))
	if ty == 12:
		print("Stem and Leaf of the sample")
		stemLeafList = stemAndLeaf(xinc)
		for each in stemLeafList:
			print(str(each["stem"]) + "     ", end=" ")
			for j in range(len(each["leaf"])):
				print(each["leaf"][j], end="")
			print("")
	if ty == 13:
		print(chr(sec) + ") For a box plot, the ends of the box are located at the first third quartiles. The median is the vertical line with the box, The whiskers of the box plot connents the ends of the box to the smallest and largest data values within 1.5 interquartile ranges from the ends of the box. Points outside these plots are outliers.")
		sec += 1
		plt.boxplot(xs)
		plt.savefig('chegg-boxplot.png', patch_artist=True, vert=False)
		plt.close()
		print("")
	if ty == 14:
		print(f"{chr(sec)}) Mode is the number which appears most often in a set of numbers.")
		sec += 1
		print(f"Mode = {max(set(xs), key=xs.count)}")
	if ty == 15:
		mean = xbar
		sd = s
		print("\\\\Mean (\\bar{x}) = " + str(mean))
		print("Sample size (n) = " + str(n))
		print("Standard deviation (s) = " + str(s))
		ci = float(input("Confidence interval(in %) = "))
		if n < 30:
			t = round(st.t.ppf(1-((1-(ci/100))/2), n-1), 4)
			print ("\\\\t_{\\alpha/2, n-1} = " + str(t))
			print ("\\\\Since\\ we\\ know\\ that")
			print ("\\\\Confidence\\; interval = \\bar{x} \\pm t_{\\alpha/2, n-1}\\frac{s}{\\sqrt{n}}")
			E = error(t, sd, n)
			ll = round(mean - E, 4)
			ul = round(mean + E, 4)
			print ("\\\\Required\\ confidence\\ interval = (" + str(mean) + "-" + str(t) + "\\frac{" + str(sd) + "}{\\sqrt{" + str(n) + "}}, "+ str(mean) + "+" + str(t) + "\\frac{" + str(sd) + "}{\\sqrt{" + str(n) + "}})")
			print ("Required confidence interval = (" + str(mean) + "-" + str(E) + ", "+ str(mean) + "+" + str(E) + ")")
			print ("Required confidence interval = (" + str(ll) + ", " + str(ul) + ")")
		else:
			z = round(st.norm.ppf(1-((1-(ci/100))/2)), 4)
			print ("z @ " + str(ci) + "% = " + str(z))
			print ("\\\\Since\\ we\\ know\\ that")
			print ("\\\\Confidence\\; interval = \\bar{x} \\pm z\\frac{s}{\\sqrt{n}}")
			E = error(z, sd, n)
			ll = round(mean - E, 4)
			ul = round(mean + E, 4)
			print ("\\\\Required\\ confidence\\ interval = (" + str(mean) + "-" + str(z) + "\\frac{" + str(sd) + "}{\\sqrt{" + str(n) + "}}, "+ str(mean) + "+" + str(z) + "\\frac{" + str(sd) + "}{\\sqrt{" + str(n) + "}})")
			print ("Required confidence interval = (" + str(mean) + "-" + str(E) + ", "+ str(mean) + "+" + str(E) + ")")
			print ("Required confidence interval = (" + str(ll) + ", " + str(ul) + ")")
		print(f"Interpretion: We are {ci}% confident that the true mean of the population lie between the interval {ll} and {ul}.")
	if ty == 16: 
		ci = float(input("Confidence interval(in %) = "))
		xs2 = list(map(float, input("Input all the values of x: ").split()))
		xbar2 = mean(xs2)
		xmxbar2 = var(xs2, xbar2)
		xmxbarsq2 = square(xmxbar2)
		n2 = len(xs2)
		xsumsquare2 = round(sum(xmxbarsq2), 4)
		var2 = variance(xsumsquare2, n)
		sd2 = stddev(var2)

		header = ["X", "X - mean", "(X-mean)^2"]
		table = zip(xs2, xmxbar2, xmxbarsq2)
		print(tabulate((table), header, tablefmt="latex"))

		print("\\\\\\sum_{i=1}^n x_i = " + str(sum(xs2)))
		print("\\\\and\\ n = " + str(n2))
		print("\\\\This\\ implies\\ that")
		print("\\\\Mean(\\bar{x}) = \\frac{" + str(sum(xs2)) + "}{" + str(n2) + "}")
		print("\\\\Mean(\\bar{x}) = " + str(xbar2))

		print("\\\\(\sum{x_i - \\bar{x}})^2 = " + str(xsumsquare2))
		print("\\\\n = " + str(n2))
		print("\\\\Variance(s^2) = \\frac{" + str(xsumsquare2) + "}{" + str(n2-1) + "}")
		print("\\\\Variance(s^2) = " + str(var2))
		print("\\\\Standard\;Deviation(s) = \sqrt{Variance}")
		print("\\\\Standard\;Deviation(s) = " + str(sd2)) 

		mean1 = xbar
		print("\\\\Mean\\ 1 (\\bar{X_1}) = " + str(mean1))
		n1 = n
		print("\\\\Sample\\ size\\ 1 (n_1) = " + str(n))
		sd1 = s
		print("\\\\Standard\\ deviation\\ 1 (s_1) = " + str(s))
		mean2 = xbar2
		print("\\\\Mean\\ 2 (\\bar{X_2}) = " + str(xbar2))
		print("\\\\Sample\\ size\\ 2 (n_2) = " + str(n2))
		print("\\\\Standard\\ deviation\\ 2 (s_2) = " + str(sd2))
		if n1 + n2 < 30:
			t = round(st.t.ppf(1-((1-(ci/100))/2), n1 + n2 - 1), 4)
			print("\\\\t_{\\alpha/2, n_1 + n_2 -2} = " + str(t))
			print ("\\\\Since\\ we\\ know\\ that")
			print ("\\\\Confidence\\; interval = \\bar{X_1}-\\bar{X_2} \\pm t_{\\alpha/2, n-1}S_P\sqrt{\\frac{1}{n_1}+\\frac{1}{n_2}}")
			print ("\\\\S_P = \sqrt{\\frac{(n_1-1)s1^2 + (n_2-1)s2^2}{n_1 + n_2 - 2}}")
			E = errort2(t, sd1, sd2, n1, n2)
			ll = round(mean1 - mean2 - E, 4)
			ul = round(mean1 - mean2 + E, 4)
			mean = round(mean1 - mean2, 4)
			print ("\\\\Required\\; confidence\\; interval = (" + str(mean1) + "-" + str(mean2) + "-" + str(t) + "S_P\sqrt{\\frac{1}{" + str(n1) + "}+\\frac{1}{" + str(n2) + "}}, "+ str(mean1) + "-" + str(mean2) + "+" + str(t) + "S_P\sqrt{\\frac{1}{" + str(n1) + "}+\\frac{1}{" + str(n2) + "}})")
			print ("Required confidence interval = (" + str(mean) + "-" + str(E) + ", "+ str(mean) + "+" + str(E) + ")")
			print ("Required confidence interval = (" + str(ll) + ", " + str(ul) + ")")
		else:
			z = round(st.norm.ppf(1-((1-(ci/100))/2)), 4)
			print ("z @ " + str(ci) + "% = " + str(z))
			print ("\\\\Since\\ we\\ know\\ that")
			print ("\\\\Confidence\\; interval = \\bar{X_1}-\\bar{X_2} \\pm z_{\\alpha/2}\sqrt{\\frac{\sigma_1^2}{n_1} + \\frac{\sigma_2^2}{n_2}")
			E = error2(z, sd1, sd2, n1, n2)
			ll = round(mean1 - mean2 - E, 4)
			ul = round(mean1 - mean2 + E, 4)
			print ("\\\\Required\\ confidence\\ interval = (" + str(mean1) + "-" + str(mean2) + "-" + str(z) + "\sqrt{\\frac{" + str(sd1) + "^2}{" + str(n1) + "} + \\frac{" + str(sd2) + "^2}{" + str(n2) + "}}, " + str(mean1) + "-" + str(mean2) + "+" + str(z) + "\sqrt{\\frac{" + str(sd1) + "^2}{" + str(n1) + "} + \\frac{" + str(sd2) + "^2}{" + str(n2) + "}})")
			print ("Required confidence interval = (" + str(mean1) + "-" + str(mean2) + "-" + str(E) + ", "+ str(mean1) + "-" + str(mean2) + "+" + str(E) + ")")
			print ("Required confidence interval = (" + str(ll) + ", " + str(ul) + ")")
	if ty == 17:
		print("The maximum and the minimum values are as follows")
		print(f"Minimum value = {xinc[0]}")
		print(f"Maximum value = {xinc[-1]}")
		print("Since we know that")
		print("Median for a list of even number of data point is the mean of 2 middle most values if we sort the list in increasing order while for a list of odd number it is the middle most value if the list is sorted in increasing order.")
		if len(xs)%2 == 0:
			print("Since our list have even number of data points, this implies that")
			print("Median = " + str(med))
		else:
			print("Since our list have odd number of data points, this implies that")
			print("Median = " + str(med))
		print("Since we know that")
		print("The lower quartile(Q1) is the median of the lower half of the data set while upper quartile(Q3) is the median of the upper half of the data set.")
		if len(xs)%2 == 0:
			print("Lower half of our list is " + str(lh))
			print("Since our lower half list have even number of data points, this implies that")
			print("Q1 = " + str(Q1))
			print("Upper half of our list is " + str(uh))
			print("Since our upper half list have even number of data points, this implies that")
			print("Q3 = " + str(Q3))
		else:
			print("Lower half of our list is " + str(lh))
			print("Since our lower half list have even number of data points, this implies that")
			print("Q1 = " + str(Q1))
			print("Upper half of our list is " + str(uh))
			print("Since our upper half list have even number of data points, this implies that")
			print("Q3 = " + str(Q3))
		print(f"Five point summary = {xinc[0]}, {Q1}, {med}, {Q3}, {xinc[-1]}")
		print(f"Min = {xinc[0]}")
		print(f"Q1 = {Q1}")
		print(f"Med = {med}")
		print(f"Q3 = {Q3}")
		print(f"Max = {xinc[-1]}")
	if ty == 18:
		perc = float(input("Percentile = "))
		print(f"Ordered list: {xinc}")
		print("index = percentile * n")
		print(f"index = {perc/100} * {n}")
		index = (perc/100) * n
		print(f"index = {index}")
		if index.is_integer():
			print(f"The {perc}th percentile is the average of value corresponding to index and the value that directly follows it.")
			print(f"{perc}th percentile = ({xinc[int(index-1)]} + {xinc[int(index)]})/2")
			print(f"{perc}th percentile = {xinc[int(index-1)] + xinc[int(index)]}/2")
			print(f"{perc}th percentile = {(xinc[int(index-1)] + xinc[int(index)])/2}")
		else:
			print(f"The corresponding value to the index in your data set is the {perc}th percentile")
			print(f"{perc}th percentile = {xinc[int(round(index-1))]}")


print("Please hit thumbs up if the answer helped you.")
