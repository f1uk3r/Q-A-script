import math

principal = float(input("Principal or amount of money deposited (P) = "))
rate = float(input("annual interest rate (r) = "))
n = int(input("number of times compounded per year (n) = "))
t = float(input("time in years (t) = "))

print("Since we know that")
print("\\\\FV = P\\left(1 + \\frac{r}{n}\\right)^{nt}")
print("where FV = future value of the deposit")
print(f"\\\\FV = {principal}\\left(1 + \\frac{{{rate}}}{{{n}}}\\right)^{{{n}({t})}}")
print(f"\\\\FV = {principal} ({round(1 + (rate/n), 4)})^{{{n*t}}}")
print(f"\\\\FV = {principal} ({round((1 + (rate/n))**(n*t), 4)})")
print(f"\\\\FV = {round(principal * ((1 + (rate/n))**(n*t)), 4)}")
print("Please hit thumbs up if the answer helped you")