import math
import webbrowser
import scipy.stats as st

print ("""Legend for type
1 for less than <
2 for greater than >
3 for between
5 for finding x from z value
6 for equal to
7 mean and standard deviation""")
parts = int(input("How many parts: "))
print ("This is a lognormal distribution question with")
theta = float(input("\\\\\\theta= "))
omega_sq = float(input("\\\\\\omega^2= "))
omega = round(math.sqrt(omega_sq), 4)
print("If W has a normal distributino with mean \\theta and variance \\omega^2 then X = exp(W) has a lognormal distribution")
print("To calculate probabilities for X, we need to make a transformation for X")
print("\\\\P(X\\le x) = P[exp(W)\\le x] = P[W\\le ln(x)] = P[Z\\le \\frac{ln(x)-\\theta}{\\omega}]")

def z(x, theta, omega):
	return round((x - theta) / omega, 4)

def xi(z, theta, omega):
	return round(theta + (z * omega), 4)

def mean(theta, omega_sq):
    power = theta + (omega_sq/2)
    return round(math.exp(power), 4)

sec = 97


for i in range(parts):
    ty = int(input("Type of this part: "))

    if ty == 1:
        x1 = float(input(chr(sec) + ") " + "x = "))
        print (f"\\\\{chr(sec)}) P(x < {str(x1)})=?")
        sec += 1 
        print(f"\\\\P(X < {x1}) = P[exp(W)<{x1}]")
        print(f"\\\\P(X < {x1}) = P[W<ln({x1})]")
        print(f"\\\\P(X < {x1}) = P[Z<\\frac{{ln({x1})-{theta}}}{{\\sqrt{{{omega_sq}}}}}]")
        z1 = z(math.log(x1), theta, omega)
        ans = round(st.norm.cdf(z1), 4)
        print (f"\\\\P(X < {x1}) = P(Z < {z1})")
        print (f"\\\\P(x < {x1}) = \\textbf{{{ans}}}")

    if ty == 2:
        x1 = float(input(chr(sec) + ") " + "x = "))
        print (f"\\\\{chr(sec)}) P(x > {str(x1)})=?")
        sec += 1 
        print(f"\\\\P(X > {x1}) = P[exp(W)>{x1}]")
        print(f"\\\\P(X > {x1}) = P[W>ln({x1})]")
        print(f"\\\\P(X > {x1}) = P[Z>\\frac{{ln({x1})-{theta}}}{{\\sqrt{{{omega_sq}}}}}]")
        z1 = z(math.log(x1), theta, omega)
        ans = round(1 - st.norm.cdf(z1), 4)
        print (f"\\\\P(X > {x1}) = P(Z > {z1}) = 1 - P(Z < {z1})")
        print (f"\\\\P(x > {x1}) = \\textbf{{{ans}}}")

    elif ty == 3:
        x1 = float(input("x1 = "))
        x2 = float(input("x2 = "))
        print (f"{chr(sec)}) P({x1} < X < {x2})=?")
        sec += 1 
        print (f"\\\\P({x1} < X < {x2})=P[{x1}<exp(W)<{x2}]")
        print (f"\\\\P({x1} < X < {x2})=P[ln({x1})<exp(W)<ln({x2})]")
        print (f"\\\\P({x1} < X < {x2})=P[\\frac{{ln({x1})-{theta}}}{{\\sqrt{omega_sq}}}<Z<\\frac{{ln({x2})-{theta}}}{{\\sqrt{omega_sq}}}]")
        z1 = z(math.log(x1), theta, omega)
        z2 = z(math.log(x2), theta, omega)
        print (f"P({x1} < X < {x2})=P[{z1}<Z<{z2}]")
        print (f"P({x1} < X < {x2})=P(Z<{z2})-P(Z<{z1})")
        print (f"P({x1} < X < {x2})={st.norm.cdf(z2)} - {st.norm.cdf(z1)}")
        ans = round(st.norm.cdf(z2) - st.norm.cdf(z1), 4)
        print (f"P({x1} < X < {x2}) = {ans}")
    elif ty == 4:
        x1 = float(input("x1 = "))
        x2 = float(input("x2 = "))
        print (f"{chr(sec)}) P({x1} < X < {x2})=?")
        sec += 1 
        print (f"\\\\P({x1} < X < {x2})=P[{x1}<exp(W)<{x2}]")
        print (f"\\\\P({x1} < X < {x2})=P[ln({x1})<exp(W)<ln({x2})]")
        print (f"\\\\P({x1} < X < {x2})=P[\\frac{{ln({x1})-{theta}}}{{\\sqrt{omega_sq}}}<Z<\\frac{{ln({x2})-{theta}}}{{\\sqrt{omega_sq}}}]")
        z1 = z(math.log(x1), theta, omega)
        z2 = z(math.log(x2), theta, omega)
        print (f"P({x1} < X < {x2})=P[{z1}<Z<{z2}]")
        print (f"P({x1} < X < {x2})=P(Z<{z2})-P(Z<{z1})")
        print (f"P({x1} < X < {x2})={st.norm.cdf(z2)} - {st.norm.cdf(z1)}")
        ans = round(st.norm.cdf(z2) - st.norm.cdf(z1), 4)
        print (f"P({x1} < X < {x2}) = {ans}")
        ans = round(1 - st.norm.cdf(z2) + st.norm.cdf(z1), 4)
        print ("This implies that")
        print ("P(X < " + str(x1) + " or X > " + str(x2) + ") = P(z < " + str(z1) + " or z > " + str(z2) + ") = " +str(ans))

    elif ty == 5:
        pn = float(input("p = "))
        zn = st.norm.ppf(pn)
        xn = xi(zn, theta, omega)
        print (chr(sec) + ") Given in the question ")
        sec += 1
        print ("P(X < x) = " + str(pn))
        print(f"\\\\P(X < x) = P[exp(W)<x]")
        print(f"\\\\P(X < x) = P[W<ln(x)]")
        print(f"\\\\P(X < x) = P[Z<\\frac{{ln(x)-{theta}}}{{\\sqrt{{{omega_sq}}}}}]")
        print ("P(Z < " + str(zn) + ") = " + str(pn))
        print ("With the help of formula for z, we can say that")
        print (f"\\\\ ln(x) = \\theta + z\\omega")
        print (f"\\\\ ln(x) = {theta} + ({zn}) {omega}") 
        print ("ln(x) = " + str(xn))
        print(f"x = {math.exp(xn)}")

    elif ty == 6:
        x = float(input(chr(sec) + ") x = "))
        sec += 1
        print ("P(X = " + str(x) + ") = ?")
        print ("For a continous the probability is the integration of probability density function in an given interval. Since if we give a particular point as an interval the integration comes out as 0.")
        print ("P(X = " + str(x) + ") = 0")

    elif ty ==7:
        print("The mean of the lognormal random variable X can be calculated as")
        print(f"\\\\E(X) = e^{{\\theta + \\omega^2/2}}")
        print(f"\\\\E(X) = e^{{{theta} + {omega_sq}/2}}")
        print(f"E(X) = {mean(theta, omega_sq)}")
        print("The variance of the lognormal random variable X can be calculated as")
        print(f"\\\\V(X) = e^{{2\\theta + \\omega^2}}(e^{{\\omega^2}} - 1)")
        print(f"\\\\V(X) = e^{{2*{theta} + {omega_sq}}}(e^{{{omega_sq}}} - 1)")
        print(f"\\\\V(X) = e^{{{(2*theta)+omega_sq}}}({math.exp(omega_sq)} - 1)")
        print(f"\\\\V(X) = {math.exp(2*theta+omega_sq)}({math.exp(omega_sq)- 1})")
        print(f"\\\\V(X) = {round((math.exp(2*theta+omega_sq))*(math.exp(omega_sq)- 1), 4)}")



print ("PS: you have to refer z score table to find the final probabilities.")
print ("Please hit thumps up if the answer helped you")
