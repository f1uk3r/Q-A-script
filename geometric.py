from binom import binom1, ncr

def geom2(k, x, p, q):
	sum = 0
	while k > 0:
		sum += binom1(k, x, p, q)
		k -= 1
	return round(sum, 4)

def geom3(k, x, p, q):
	sum = 0
	k -= 1
	while k > 0:
		sum += binom1(k, x, p, q)
		k -= 1
	return round(sum, 4)

def geom4(k, x, p, q):
	answ = 1 - geom3(k, x, p, q)
	return round(answ, 4)

def geom5(n, x, p, q):
	sum = 1 - geom2(k, x, p, q)
	return round(sum, 4)
print ("Legend for type \n 1 for = \n 2 and 3 for less than equal to and < \n 4 and 5 for \ge and > \n 6 for mean \n 7 for variance and standard deviation")
print ("This is a question of geometric distribution. The geometric distribution gives the probability that the first occurrences of success requires k independent trial each with success probability p, then the probability that the kth trial is the first success is")
parts = int(input("How many parts: "))
p = float(input("p = "))
q = round(1-p, 4)

print ("q = 1 - p = " + str(q))
print ("where")
print ("P(X=k) = p*(1-p)^{k-1}")

sec = 97
for i in range(parts):
	ty = int(input("Type of k: "))
	if ty == 6:
		mean = round(1 / p, 4)
		print (chr(sec) + ") Since we know that")
		sec += 1
		print ("\\\\Mean (\mu) = \\frac{1}{p} = " + str(mean))

	elif ty == 7:
		variance = round(q / p ** 2, 4)
		sd = round(math.sqrt(q / p ** 2), 4)
		print (chr(sec) + ") Since we know that")
		sec += 1
		print ("\\\\Mean (\mu) = \\frac{1}{p} = " + str(mean))
		print ("\\\\Variance (\sigma^2) = \\frac{q}{p^2} = " + str(sd))
		print ("\\\\Standard\; deviation (\sigma) = \sqrt{\\frac{q}{p^2}} = " + str(sd))

	else:
		if ty == 1:
			k = int(input(chr(sec) + ") " + "k = "))
			sec += 1 
			ans = round(binom1(k, 1, p, q), 4)
			print ("P(X = " + str(k) + ") = \\binom{" + str(k) + "}{" + str(1) + "} " + str(p) + "^{" + str(1) + "} "+ str(q) + "^{" + str(k) + "- 1}")
			print ("P(X = " + str(k) + ") = " + str(ans))
		elif ty == 2:
			k = int(input(chr(sec) + ") " + "k = "))
			sec += 1 
			ans = round(geom2(k, 1, p, q), 4)
			print ("P(X \le " + str(k) + ") = ", end=" ")
			for j in range(k):
				print("P(X = " + str(j) + ") + ", end=" ")
			print("P(X = " + str(k) + ")")
			print ("P(X \le " + str(k) + ") = " + str(ans))
		elif ty == 3:
			k = int(input(chr(sec) + ") " + "k = "))
			sec += 1 
			ans = round(geom3(k, 1, p, q), 4)
			print ("P(X < " + str(k) + ") = ", end=" ")
			for j in range(k-1):
				print("P(X = " + str(j) + ") + ", end=" ")
			print("P(X = " + str(k-1) + ")")
			print ("P(X < " + str(k) + ") = " + str(ans))
		elif ty == 4:
			k = int(input(chr(sec) + ") " + "k = "))
			sec += 1 
			ans = round(geom4(k, 1, p, q), 4)
			print ("\\\\P(X \ge " + str(k) + ") = 1 ", end=" ")
			for j in range(k-1):
				print("- P(X = " + str(j) + ") ", end=" ")
			print ("P(X = " + str(k-1) + ")")
			print ("P(X \ge " + str(k) + ") = " + str(ans))
		elif ty == 5:
			k = int(input(chr(sec) + ") " + "k = "))
			sec += 1 
			ans = round(geom5(k, 1, p, q), 4)
			print ("\\\\P(X > " + str(k) + ") = 1 ", end=" ")
			for j in range(k):
				print("- P(X = " + str(j) + ") ", end=" ")
			print ("P(X = " + str(k) + ")")
			print ("P(X > " + str(k) + ") = " + str(ans))

print ("Please hit thumps up if the answer helped you")