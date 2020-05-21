import math
import webbrowser
import scipy.stats as st

print ("""Legend for type
1 for less than <
2 for greater than >
3 for between
6 for equal to
7 for mean and variance""")
parts = int(input("How many parts: "))
print ("This is a Weibull distribution question with")
beta = float(input("\\\\\\beta= "))
delta = float(input("\\\\\\delta= "))
print("For a Weibull random variable X with parameters //delta and //beta, its cumulative distribution function is")
print("\\\\F(x)=1-exp\\left[-\\left(\\frac{x}{\\delta}\\right)^\\beta\\right]")

def prob(x, beta, delta):
	return round(1 - (math.exp(-((x/delta) ** beta))), 4)

def prob2(x, beta, delta):
	return round(math.exp(-((x/delta) ** beta)), 4)

sec = 97


for i in range(parts):
    ty = int(input("Type of this part: "))

    if ty == 1:
        x1 = float(input("x = "))
        print (f"\\\\{chr(sec)}) P(x < {x1})=?")
        sec += 1 
        print (f"\\\\P(x < {x1})=F({x1})")
        print (f"\\\\P(x < {x1})=1-exp\\left[-\\left(\\frac{{{x1}}}{{{delta}}}\\right)^{{{beta}}}\\right]")
        print (f"\\\\P(x < {x1})=1-exp\\left[-({x1/delta})^{{{beta}}}\\right]")
        print (f"\\\\P(x < {x1})=1-exp(-{(x1/delta) ** beta})")
        ans = prob(x1, beta, delta)
        print (f"\\\\P(x < {x1})={ans}")

    if ty == 2:
        x1 = float(input("x = "))
        print (f"\\\\{chr(sec)}) P(x > {x1})=?")
        sec += 1 
        print (f"\\\\P(x > {x1})=1-F({x1})")
        print (f"\\\\P(x > {x1})=1-\\left{{1-exp\\left[-\\left(\\frac{{{x1}}}{{{delta}}}\\right)^{{{beta}}}\\right]\\right}}")
        print (f"\\\\P(x > {x1})=exp\\left[-({x1/delta})^{{{beta}}}\\right]")
        print (f"\\\\P(x > {x1})=exp(-{(x1/delta) ** beta})")
        ans = prob2(x1, beta, delta)
        print (f"\\\\P(x > {x1})={ans}")

    if ty == 3:
        x1 = float(input("x1 = "))
        x2 = float(input("x2 = "))
        print (f"\\\\{chr(sec)}) P({x1}<x<{x2})=?")
        sec += 1 
        print (f"\\\\P({x1}<x<{x2})=F({x2}) - F({x1})")
        print (f"\\\\P({x1}<x<{x2})=\\left{{1-exp\\left[-\\left(\\frac{{{x2}}}{{{delta}}}\\right)^{{{beta}}}\\right]\\right}} - \\left{{1-exp\\left[-\\left(\\frac{{{x1}}}{{{delta}}}\\right)^{{{beta}}}\\right]\\right}}")
        print (f"\\\\P({x1}<x<{x2})=exp\\left[-({x1/delta})^{{{beta}}}\\right] - exp\\left[-({x2/delta})^{{{beta}}}\\right]")
        print (f"\\\\P({x1}<x<{x2})=exp(-{(x1/delta) ** beta}) - exp(-{(x2/delta) ** beta})")
        ans = prob2(x1, beta, delta) - prob2(x2, beta, delta)
        print (f"\\\\P({x1}<x<{x2})={ans}")


    elif ty == 6:
        x = float(input(chr(sec) + ") x = "))
        sec += 1
        print ("P(X = " + str(x) + ") = ?")
        print ("For a continous the probability is the integration of probability density function in an given interval. Since if we give a particular point as an interval the integration comes out as 0.")
        print ("P(X = " + str(x) + ") = 0")

    elif ty ==7:
        print("The mean of the Weibull distribution X can be calculated as")
        print(f"\\\\\\mu = E(X) = \\delta \\Gamma \\left(1 + \\frac{{1}}{{\\beta}}\\right)")
        print(f"\\\\E(X) = {delta} \\Gamma \\left(1 + \\frac{{1}}{{{beta}}}\\right)")
        print(f"\\\\E(X) = {delta} \\Gamma ({1+(1/beta)})")
        print(f"\\\\E(X) = {delta} *{round(math.gamma(1+(1/beta)),4)}")
        print(f"\\\\E(X) = {round(delta * math.gamma(1+(1/beta)),4)}")
        print("The variance of the Weibull distribution X can be calculated as")
        print(f"\\\\\\sigma^2 = V(X) = \\delta^2 \\Gamma \\left(1 + \\frac{{2}}{{\\beta}}\\right)-\\delta^2 \\left[\\Gamma \\left(1 + \\frac{{1}}{{\\beta}}\\right)\\right]^2")
        print(f"\\\\\\sigma^2 = V(X) = {delta}^2 \\Gamma \\left(1 + \\frac{{2}}{{{beta}}}\\right)-{delta}^2 \\left[\\Gamma \\left(1 + \\frac{{1}}{{{beta}}}\\right)\\right]^2")
        print(f"\\\\\\sigma^2 = V(X) = {delta ** 2} \\Gamma ({1 + (2/beta)})-{delta ** 2} \\left[\\Gamma ({1 + (1/beta)})\\right]^2")
        print(f"\\\\\\sigma^2 = V(X) = {delta ** 2}({math.gamma(1 + (2/beta))})-{delta ** 2} ({math.gamma(1 + (1/beta))})^2")
        print(f"\\\\\\sigma^2 = V(X) = {(delta ** 2)*(math.gamma(1 + (2/beta)))}-{(delta ** 2)*(math.gamma(1 + (1/beta))**2)}")
        print(f"\\\\\\sigma^2 = V(X) = {((delta ** 2)*(math.gamma(1 + (2/beta))))-((delta ** 2)*(math.gamma(1 + (1/beta))**2))}")




print ("PS: you have to refer z score table to find the final probabilities.")
print ("Please hit thumbs up if the answer helped you.")