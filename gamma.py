import math
import webbrowser

print ("""Legend for type
1 for mean and variance from lambda and r
2 for lambda and r from mean and variance""")


ty = int(input("Type of this part: "))

if ty == 2:
    print("If X has a gamma distribution with parameter \\lambda and r, the mean and variance of X are")
    print(f"\\mu = E(X) = \\frac{{r}}{{\\lambda}} and \\sigma^2 = V(X) = \\frac{{r}}{{\\lambda^2}}")
    print("Given")
    mean = float(input("\\\\\\mu = E(X) = "))
    variance = float(input("\\\\\\sigma^2 = V(X) = "))
    lamda = mean / variance
    print("So, this implies that")
    print(f"\\\\\\frac{{r}}{{\\lambda}} = {mean}")
    print(f"\\\\\\frac{{r}}{{\\lambda^2}} = {variance}")
    print(f"\\\\\\frac{{{mean}}}{{{variance}}} = \\lambda")
    print(f"\\\\\\lambda = {round(mean/variance, 4)}")
    print(f"\\\\r = \\mu * \\lambda")
    print(f"\\\\r = {mean} * {lamda}")
    print(f"\\\\r = {round(mean * lamda, 4)}")

elif ty ==1:
    print ("This is a gamma distribution question with")
    lamda = float(input("\\\\\\lambda= "))
    r= float(input("\\\\r= "))
    print("The mean of the gamma distribution X can be calculated as")
    print(f"\\\\\\mu = E(X) = \\frac{{r}}{{\\lambda}}")
    print(f"\\\\\\mu = E(X) = \\frac{{{r}}}{{{lamda}}}")
    print(f"\\\\\\mu = E(X) = {round(r/lamda, 4)}")
    print("The variance of the Weibull distribution X can be calculated as")
    print(f"\\\\\\sigma^2 = V(X) = \\frac{{r}}{{\\lambda^2}}")
    print(f"\\\\\\sigma^2 = V(X) = \\frac{{{r}}}{{{lamda}^2}}")
    print(f"\\\\\\sigma^2 = V(X) = \\frac{{{r}}}{{{lamda ** 2}}}")
    print(f"\\\\\\sigma^2 = V(X) = {round(r/(lamda ** 2), 4)}")

print ("PS: you have to refer z score table to find the final probabilities.")
print ("Please hit thumps up if the answer helped you")
