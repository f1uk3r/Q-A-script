import math
from tabulate import tabulate
def mul(list1, list2):
	neo = []
	multi = 0
	for i in range(len(list1)):
		neo.append(round(list1[i] * list2[i], 2))
	return neo

def var(xpx, xxpx):
	return round(xxpx - xpx ** 2, 4)
xs = list(map(float, input("Input all the values of x: ").split()))
pxs = list(map(float, input("Input all the values of px: ").split()))
xpxs = mul(xs, pxs)
xxpxs = mul(xpxs, xs)

header = ["X", "P(X)", "X.P(X)", "X^2.P(X)"]
table = zip(xs, pxs, xpxs, xxpxs)
print(tabulate((table), header, tablefmt="latex"))

xpx = round(sum(xpxs), 4)
xxpx = round(sum(xxpxs), 4)
vari = var(xpx, xxpx)
sd = round(math.sqrt(vari), 4)

print ("\sum x.P(x) = " + str(xpx) + ", \sum x^2.P(x) = " + str(xxpx))
print ("Since we know that,")
print ("\\\\Mean = \sum x.P(x) = " + str(xpx))
print ("\\\\Variance = \sum x^2.P(x) - \left(\sum x.P(x)\\right)^2 = " + str(vari))
print ("\\\\Standard\;deviation = \sqrt{\sum x^2.P(x) - \left(\sum x.P(x)\\right)^2} = " + str(sd))
print ("Please hit thumps up if the answer helped you")
