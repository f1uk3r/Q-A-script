import matplotlib.pyplot as plt
a = [5, 12, 12, 15, 15, 22, 25, 30, 35, 45]
b = [10, 12, 14, 15, 15, 20, 22, 24, 25, 30]
xs = [a,b]
plt.boxplot(xs)
plt.savefig('chegg-boxplot.png', patch_artist=True, labels=["Ramp Meters On", "Ramp Meters Off"])
plt.close()
