import math
from tabulate import tabulate

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

print("Legend for types\n 1. Mean\n 2. Median\n 3. Range \n 4. Variance \n 5. Standard Deviation \n 6. Quartile 1 and 3 \n 7. Maximum and minimum \n 8. Interquartile Range\n 9. Coefficient of Variation\n 10. Finding all outliers\n 11. Pearson’s Coefficient of Skewness")
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
		print("Mean(\\bar{x}) = \\frac{\sum_{i=1}^n x_i}{n}")
		print("Where n is the number of data points")
		print("Now")
		print("\sum_{i=1}^n x_i = " + str(sum(xs)))
		print("and n = " + str(n))
		print("This implies that")
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
		print(chr(sec) + ") Since we know that")
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
		lower, high = boundOutliers(Q1, Q3, IQR)
		print("Since we know that the outliers are those points in the data set which are either less than 1.5 times the IQR from Quartile 1 or more than 1.5 times the IQR from Quartile 3")
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
		

print("Please hit thumps up if the answer helped you.")
