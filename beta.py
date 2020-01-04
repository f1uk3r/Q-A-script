import math
import webbrowser

print ("""Legend for type
1 for less than <
2 for greater than >
3 for between
6 for mode
7 for mean and variance""")
parts = int(input("How many parts: "))
print ("This is a beta distribution question with")
alpha = float(input("\\\\\\alpha= "))
beta = float(input("\\\\\\beta= "))
print("If X has a beta distribution with parameters \\alpha and \\beta, its probability density function is ")
print("\\\\f(x)=\\frac{\\Gamma(\\alpha + \\beta)}{\\Gamma(\\alpha) \\Gamma(\\beta)}x^{\\alpha - 1}(1-x)^{\\beta - 1}")


sec = 97
for i in range(parts):
    ty = int(input("Type of this part: "))

    if ty == 1:
        x1 = float(input("x = "))
        print (f"\\\\{chr(sec)}) P(x < {x1})=?")
        sec += 1 
        print (f"\\\\P(x < {x1})=\\int_0^{{{x1}}} \\frac{{\\Gamma({alpha} + {beta})}}{{\\Gamma({alpha}) \\Gamma({beta})}} x^{{{alpha} - 1}}(1-{x1})^{{{beta} - 1}}")
        print (f"\\\\P(x < {x1})=\\int_0^{{{x1}}} \\frac{{\\Gamma({alpha + beta})}}{{\\Gamma({alpha}) \\Gamma({beta})}} x^{{{alpha-1}}}(1-{x1})^{{{beta-1}}}")
        print (f"\\\\P(x < {x1})=\\frac{{\\Gamma({alpha + beta})}}{{\\Gamma({alpha}) \\Gamma({beta})}} \\int_0^{{{x1}}} x^{{{alpha-1}}}(1-{x1})^{{{beta-1}}}")
        print (f"\\\\P(x < {x1})=\\frac{{{math.gamma(alpha + beta)}}}{{({math.gamma(alpha)}) ({math.gamma(beta)})}} \\int_0^{{{x1}}} x^{{{alpha-1}}}(1-{x1})^{{{beta-1}}}")
        print (f"\\\\P(x < {x1})=\\frac{{{math.gamma(alpha + beta)}}}{{({math.gamma(alpha)*math.gamma(beta)})}} \\int_0^{{{x1}}} x^{{{alpha-1}}}(1-{x1})^{{{beta-1}}}")
        print (f"\\\\P(x < {x1})={round(math.gamma(alpha + beta)/(math.gamma(alpha)*math.gamma(beta)), 4)}\\int_0^{{{x1}}} x^{{{alpha-1}}}(1-{x1})^{{{beta-1}}}")


    if ty == 2:
        x1 = float(input("x = "))
        print (f"\\\\{chr(sec)}) P(x > {x1})=?")
        sec += 1 
        print (f"\\\\P(x > {x1})=\\int_{{{x1}}}^1 \\frac{{\\Gamma({alpha} + {beta})}}{{\\Gamma({alpha}) \\Gamma({beta})}} x^{{{alpha} - 1}}(1-{x1})^{{{beta} - 1}}")
        print (f"\\\\P(x > {x1})=\\int_{{{x1}}}^1 \\frac{{\\Gamma({alpha + beta})}}{{\\Gamma({alpha}) \\Gamma({beta})}} x^{{{alpha-1}}}(1-{x1})^{{{beta-1}}}")
        print (f"\\\\P(x > {x1})=\\frac{{\\Gamma({alpha + beta})}}{{\\Gamma({alpha}) \\Gamma({beta})}} \\int_{{{x1}}}^1 x^{{{alpha-1}}}(1-{x1})^{{{beta-1}}}")
        print (f"\\\\P(x > {x1})=\\frac{{{math.gamma(alpha + beta)}}}{{({math.gamma(alpha)}) ({math.gamma(beta)})}} \\int_{{{x1}}}^1 x^{{{alpha-1}}}(1-{x1})^{{{beta-1}}}")
        print (f"\\\\P(x > {x1})=\\frac{{{math.gamma(alpha + beta)}}}{{({math.gamma(alpha)*math.gamma(beta)})}} \\int_{{{x1}}}^1 x^{{{alpha-1}}}(1-{x1})^{{{beta-1}}}")
        print (f"\\\\P(x > {x1})={round(math.gamma(alpha + beta)/(math.gamma(alpha)*math.gamma(beta)), 4)}\\int_{{{x1}}}^1 x^{{{alpha-1}}}(1-{x1})^{{{beta-1}}}")

    if ty == 3:
        x1 = float(input("x1 = "))
        x2 = float(input("x2 = "))
        print (f"\\\\{chr(sec)}) P({x1}<X<{x2})=?")
        sec += 1 
        print (f"\\\\P({x1}<X<{x2})=\\int_{{{x1}}}^{{{x2}}} \\frac{{\\Gamma({alpha} + {beta})}}{{\\Gamma({alpha}) \\Gamma({beta})}} x^{{{alpha} - 1}}(1-{x1})^{{{beta} - 1}}")
        print (f"\\\\P({x1}<X<{x2})=\\int_{{{x1}}}^{{{x2}}} \\frac{{\\Gamma({alpha + beta})}}{{\\Gamma({alpha}) \\Gamma({beta})}} x^{{{alpha-1}}}(1-{x1})^{{{beta-1}}}")
        print (f"\\\\P({x1}<X<{x2})=\\frac{{\\Gamma({alpha + beta})}}{{\\Gamma({alpha}) \\Gamma({beta})}} \\int_{{{x1}}}^{{{x2}}} x^{{{alpha-1}}}(1-{x1})^{{{beta-1}}}")
        print (f"\\\\P({x1}<X<{x2})=\\frac{{{math.gamma(alpha + beta)}}}{{({math.gamma(alpha)}) ({math.gamma(beta)})}} \\int_{{{x1}}}^{{{x2}}} x^{{{alpha-1}}}(1-{x1})^{{{beta-1}}}")
        print (f"\\\\P({x1}<X<{x2})=\\frac{{{math.gamma(alpha + beta)}}}{{({math.gamma(alpha)*math.gamma(beta)})}} \\int_{{{x1}}}^{{{x2}}} x^{{{alpha-1}}}(1-{x1})^{{{beta-1}}}")
        print (f"\\\\P({x1}<X<{x2})={round(math.gamma(alpha + beta)/(math.gamma(alpha)*math.gamma(beta)), 4)}\\int_{{{x1}}}^{{{x2}}} x^{{{alpha-1}}}(1-{x1})^{{{beta-1}}}")



    elif ty == 6:
        print("The mode of the beta distribution X can be calculated as")
        print(f"\\\\\\mu = E(X) = \\frac{{\\alpha - 1}}{{\\alpha + \\beta - 2}}")
        print(f"\\\\\\mu = E(X) = \\frac{{{alpha} - 1}}{{{alpha} + {beta} - 2}}")
        print(f"\\\\\\mu = E(X) = \\frac{{{alpha - 1}}}{{{alpha+beta-2}}}")
        print(f"\\\\\\mu = E(X) = {round((alpha-1)/(alpha+beta-2), 4)}")

    elif ty ==7:
        print("The mean of the beta distribution X can be calculated as")
        print(f"\\\\\\mu = E(X) = \\frac{{\\alpha}}{{\\alpha + \\beta}}")
        print(f"\\\\\\mu = E(X) = \\frac{{{alpha}}}{{{alpha} + {beta}}}")
        print(f"\\\\\\mu = E(X) = \\frac{{{alpha}}}{{{alpha+beta}}}")
        print(f"\\\\\\mu = E(X) = {round(alpha/(alpha+beta), 4)}")
        print("The variance of the beta distribution X can be calculated as")
        print(f"\\\\\\sigma^2 = V(X) = \\frac{{\\alpha \\beta}}{{(\\alpha+\\beta)^2(\\alpha+\\beta+1)}}")
        print(f"\\\\\\sigma^2 = V(X) = \\frac{{{alpha}* {beta}}}{{({alpha}+{beta})^2({alpha}+{beta}+1)}}")
        print(f"\\\\\\sigma^2 = V(X) = \\frac{{{alpha*beta}}}{{({alpha+beta})^2({alpha+beta+1})}}")
        print(f"\\\\\\sigma^2 = V(X) = \\frac{{{alpha*beta}}}{{({(alpha+beta) ** 2})({alpha+beta+1})}}")
        print(f"\\\\\\sigma^2 = V(X) = \\frac{{{alpha*beta}}}{{{((alpha+beta) ** 2)*(alpha+beta+1)}}}")
    
        print(f"\\\\\\sigma^2 = V(X) = {round((alpha*beta)/(((alpha+beta) ** 2)*(alpha+beta+1)), 4)}")


print ("PS: you have to refer z score table to find the final probabilities.")
print ("Please hit thumps up if the answer helped you")
