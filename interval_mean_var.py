import math
from tabulate import tabulate

def midInterval(list1, list2):
	neo = []
	for i in range(len(list1)):
		neo.append(round((list1[i] + list2[i]) / 2, 2))
	return neo

def square(list):
	neo = []
	sq = 0
	for i in range(len(list)):
		neo.append(round(list[i] ** 2, 4))
	return neo

def mul(list1, list2):
	neo = []
	multi = 0
	for i in range(len(list1)):
		neo.append(round(list1[i] * list2[i], 4))
	return neo

def makeInterval(list1, list2):
	neo = []
	for i in range(len(list1)):
		neo.append(str(list1[i]) + " - " + str(list2[i]))
	return neo

def mean(n1, n2):
	return round(n1 / n2, 4)

def variance(n1, n2, n3):
	return round(((n1)/(n2) - (n3 ** 2)), 4)

lls = list(map(float, input("Input all the lower limits of x: ").split()))
uls = list(map(float, input("Input all the upper limits of x: ").split()))
xs = midInterval(lls, uls)
fs = list(map(float, input("Input all the corresponding frequencies of x: ").split()))
fxs = mul(fs, xs)
xxs = square(xs)
fxxs = mul(fs, xxs)
Intervals = makeInterval(lls, uls)

header = ["Intervals", "x", "f", "fx", "xx", "fxx"]
table = zip(Intervals, xs, fs, fxs, xxs, fxxs)
print(tabulate((table), header, tablefmt="latex"))

f = round(sum(fs), 4)
fx = round(sum(fxs), 4)
fxx = round(sum(fxxs), 4)
avg = mean(fx, f)
var = variance(fxx, f, avg)
print("Since we know that")
print("Mean(\\bar{x}) = \\frac{\sum fx}{n} = " + str(avg))
print("Variance(\sigma^2) = \\frac{\sum fx^2}{n} - \\bar{x}^2 = \\frac{" + str(fxx) + "}{" + str(f) + "} - " + str(avg) + "^2 = " + str(var))
print("Standard Deviation(\sigma) = \sqrt{Variance} = " + str(round(math.sqrt(var), 4)))

print ("Please hit thumbs up if the answer helped you.")