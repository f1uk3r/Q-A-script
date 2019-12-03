import matplotlib.pyplot as plt
a = [28,48,56,38,30,26,43,47,50,34, 56, 41, 41, 25, 47]
b = [24,25,42,33,38,30,46,37,19,28,23,40,36,50,42]
xs = [a,b]
plt.boxplot(xs)
plt.savefig('chegg-boxplot.png', patch_artist=True, labels=["Ramp Meters On", "Ramp Meters Off"])
plt.close()