
import math
def geom1(k, p, q):
	return round(p*(q**(k-1)), 4)
def geom2(k, p, q):
	sum = 0
	while k > 0:
		sum += geom1(k, p, q)
		k -= 1
	return round(sum, 4)

def geom3(k, p, q):
	sum = 0
	k -= 1
	while k > 0:
		sum += geom1(k, p, q)
		k -= 1
	return round(sum, 4)

def geom4(k, p, q):
	return round(1 - geom3(k, p, q), 4)

def geom5(k, p, q):
	return round(1 - geom2(k, p, q), 4)
print ("""Legend for type
1 for =
2 and 3 for \\le to and <
4 and 5 for \\ge and >
6 for mean 
7 for variance and standard deviation""")
print ("This is a question of geometric distribution.")
parts = int(input("How many parts: "))
p = float(input("p = "))
q = round(1-p, 4)

print ("q = 1 - p = " + str(q))
print ("The geometric distribution gives the probability that the first occurrences of success requires k independent trial each with success probability p, then the probability that the kth trial is the first success is")
print ("P(X=k) = p*(1-p)^{k-1}")

sec = 97
for i in range(parts):
	ty = int(input("Type of k: "))
	if ty == 1:
		k = int(input("k = "))
		ans = geom1(k, p, q)
		print (f"\\\\{chr(sec)})\\ P(X = {k}) = ({p}) {q}^{{{k}- 1}}")
		sec += 1 
		print (f"\\\\P(X = {k}) = ({p}) {q}^{{{k-1}}}")
		print (f"P(X = {k}) = ({p}) {round(q**(k-1), 4)}")
		print (f"P(X = {k}) = {ans}")
		print("\\\\ \\par\\noindent\\rule{\\textwidth}{0.4pt}")
	elif ty == 2:
		k = int(input("k = "))
		ans = round(geom2(k, p, q), 4)
		print (f"\\\\{chr(sec)})\\ P(X \\le {k}) = ", end=" ")
		sec += 1 
		for j in range(k):
			print(f"P(X = {j}) + ", end=" ")
		print(f"P(X = {k})")
		print (f"\\\\P(X \\le {k}) = ", end=" ")
		for j in range(k):
			print(f"({p}) {q}^{{{j}-1}} + ", end=" ")
		print(f"({p}) {q}^{{{k}- 1}}")
		print (f"\\\\P(X \\le {k}) = ", end=" ")
		for j in range(k):
			print(f"({p}) {q}^{{{j-1}}} + ", end=" ")
		print(f"({p}) {q}^{{{k-1}}}")
		print (f"\\\\P(X \\le {k}) = ", end=" ")
		for j in range(k):
			print(f"({p}) {round(q**(j-1), 4)} + ", end=" ")
		print(f"({p}) {round(q**(k-1), 4)}")
		print (f"\\\\P(X \\le {k}) = ", end=" ")
		for j in range(k):
			print(f"{round(p*(q**(j-1)), 4)} + ", end=" ")
		print(f"{round(p*(q**(k-1)), 4)}")
		print (f"\\\\P(X \\le {k}) =  {ans}")
	elif ty == 3:
		k = int(input("k = "))
		ans = round(geom3(k, p, q), 4)
		print (f"\\\\{chr(sec)})\\ P(X < {k}) = ", end=" ")
		sec += 1 
		for j in range(k-1):
			print(f"P(X = {j}) + ", end=" ")
		print(f"P(X = {k-1})")
		print (f"\\\\P(X < {k}) = ", end=" ")
		for j in range(k-1):
			print(f"({p}) {q}^{{{j}-1}} + ", end=" ")
		print(f"({p}) {q}^{{{k-1}- 1}}")
		print (f"\\\\P(X < {k}) = ", end=" ")
		for j in range(k-1):
			print(f"({p}) {q}^{{{j-1}}} + ", end=" ")
		print(f"({p}) {q}^{{{k-2}}}")
		print (f"\\\\P(X < {k}) = ", end=" ")
		for j in range(k-1):
			print(f"({p}) {round(q**(j-1), 4)} + ", end=" ")
		print(f"({p}) {round(q**(k-2), 4)}")
		print (f"\\\\P(X < {k}) = ", end=" ")
		for j in range(k-1):
			print(f"{round(p*(q**(j-1)), 4)} + ", end=" ")
		print(f"{round(p*(q**(k-2)), 4)}")
		print (f"\\\\P(X < {k}) =  {ans}")
	elif ty == 4:
		k = int(input("k = "))
		ans = round(geom4(k, p, q), 4)
		print (f"\\\\{chr(sec)})\\ P(X \\ge {k}) = 1 ", end=" ")
		sec += 1 
		for j in range(k-1):
			print(f"- P(X = {j}) ", end=" ")
		print (f"- P(X = {k-1})")
		print (f"\\\\P(X \\ge {k}) = ", end=" ")
		for j in range(k-1):
			print(f"- ({p}) {q}^{{{j}-1}} ", end=" ")
		print(f"- ({p}) {q}^{{{k-1}- 1}}")
		print (f"\\\\P(X \\ge {k}) = 1 ", end=" ")
		for j in range(k-1):
			print(f"- ({p}) {q}^{{{j-1}}} ", end=" ")
		print(f"- ({p}) {q}^{{{k-2}}}")
		print (f"\\\\P(X \\ge {k}) = 1 ", end=" ")
		for j in range(k-1):
			print(f"- ({p}) {round(q**(j-1), 4)} ", end=" ")
		print(f"- ({p}) {round(q**(k-2), 4)}")
		print (f"\\\\P(X \\ge {k}) = 1 ", end=" ")
		for j in range(k-1):
			print(f"- {round(p*(q**(j-1)), 4)} ", end=" ")
		print(f"- {round(p*(q**(k-2)), 4)}")
		print (f"\\\\P(X \\ge {k}) =  {ans}")
	elif ty == 5:
		k = int(input(chr(sec) + ") " + "k = "))
		sec += 1 
		ans = round(geom5(k, p, q), 4)
		print (f"\\\\{chr(sec)})\\ P(X > {k}) = 1 ", end=" ")
		sec += 1 
		for j in range(k):
			print(f"- P(X = {j}) ", end=" ")
		print (f"- P(X = {k})")
		print (f"\\\\P(X > {k}) = ", end=" ")
		for j in range(k):
			print(f"- ({p}) {q}^{{{j}-1}} ", end=" ")
		print(f"- ({p}) {q}^{{{k}- 1}}")
		print (f"\\\\P(X > {k}) = 1 ", end=" ")
		for j in range(k):
			print(f"- ({p}) {q}^{{{j-1}}} ", end=" ")
		print(f"- ({p}) {q}^{{{k-1}}}")
		print (f"\\\\P(X > {k}) = 1 ", end=" ")
		for j in range(k):
			print(f"- ({p}) {round(q**(j-1), 4)} ", end=" ")
		print(f"- ({p}) {round(q**(k-1), 4)}")
		print (f"\\\\P(X > {k}) = 1 ", end=" ")
		for j in range(k):
			print(f"- {round(p*(q**(j-1)), 4)} ", end=" ")
		print(f"- {round(p*(q**(k-1)), 4)}")
		print (f"\\\\P(X > {k}) =  {ans}")
	elif ty == 6:
		mean = round(1/p, 4)
		print (chr(sec) + ") Since we know that")
		sec += 1
		print (f"""\\\\ Mean (\\mu\\ or\\ E(X)) = 1/p
\\\\ Mean (\\mu\\ or\\ E(X)) = 1/{p})
\\\\ Mean (\\mu\\ or\\ E(X)) = {mean}""")
	elif ty == 7:
		variance = round(q/(p**2), 4)
		sd = round(math.sqrt(variance), 4)
		print (chr(sec) + ") Since we know that")
		sec += 1
		print (f"""\\\\ Variance (\\sigma^2\\ or\\ V(x)) = \\frac{{q}}{{p^2}}
\\\\ Variance (\\sigma^2\\ or\\ V(x)) = \\frac{{{q}}}{{{p}^2}}
\\\\ Variance (\\sigma^2\\ or\\ V(x)) = \\frac{{{q}}}{{{p**2}}}
\\\\ Variance (\\sigma^2\\ or\\ V(x)) = {variance}""")
		print (f"""\\\\ Standard\\; deviation (\\sigma\\ or\\ sd) = \\sqrt{{\\frac{{q}}{{p^2}}}}
\\\\ Standard\\; deviation (\\sigma\\ or\\ sd) = \\sqrt{{V(x)}}
\\\\ Standard\\; deviation (\\sigma\\ or\\ sd) = \\sqrt{variance}
\\\\ Standard\\; deviation (\\sigma\\ or\\ sd) = {sd}
\\\\ \\par\\noindent\\rule{{\\textwidth}}{{0.4pt}}""")

print ("Please hit thumps up if the answer helped you")