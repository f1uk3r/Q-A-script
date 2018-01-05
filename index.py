print("Index: Which file have to be Executed \n1. Normal.py \n2.Binomial \n3. Binomial to normal/poisson \n4. Exponential \n5. Poisson \n6. List of x \n7. Frequency of an intervval \n8. Discrete pdf is given \n9. Linear Regression \n10. Confidence Interval \n11. Confidence Interval of variance \n12. Confidence interval of proportions \n13. Geometric Distribution")

which = int(input("Which script do you want to execute: "))

if which == 1:
	exec(open("normal.py").read())
elif which == 2:
	exec(open("binom.py").read())
elif which == 3:
	exec(open("binom_to_normal.py").read())
elif which == 4:
	exec(open("exponential.py").read())
elif which == 5:
	exec(open("poisson.py").read())
elif which == 6:
	exec(open("listox.py").read())
elif which == 7:
	exec(open("interval_mean_var.py").read())
elif which == 8:
	exec(open("pdf.py").read())
elif which == 9:
	exec(open("linear_regression.py").read())
elif which == 10:
	exec(open("confidence.py").read())
elif which == 11:
	exec(open("variance_confidence.py").read())
elif which == 12:
	exec(open("proportion_ci.py").read())
elif which == 13:
	exev(open("geometric.py").read())
