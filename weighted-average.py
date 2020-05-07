import math
from tabulate import tabulate
import matplotlib.pyplot as plt
import scipy.stats as st

def mul(list1, list2):
	multiplied_list = []
	for i in range(len(list1)):
		multiplied_list.append(round(list1[i] * list2[i], 4))
	return multiplied_list

score_list = list(map(float, input("Input all the values of scores: ").split()))
weight_list = list(map(float, input("Input all the values of weights: ").split()))
weighted_scores_list = mul(score_list, weight_list)
category_question = int(input("Do you want to insert category names(1 for yes): "))
if category_question == 1:
    category_list = list(map(str, input("enter categories (space seperated): ").split()))
    print(category_list)
    header = ["Category", "Weights", "Score", "Weighted Score"]
    table = zip(category_list, weight_list, score_list, weighted_scores_list)
    print(tabulate((table), header, tablefmt="latex"))
else:
    header = ["Weights", "Score", "Weighted Score"]
    table = zip(weight_list, score_list, weighted_scores_list)
    print(tabulate((table), header, tablefmt="latex"))

sum_weights = round(sum(weight_list), 4)
sum_weighted_scores = round(sum(weighted_scores_list), 4)

print("Since we know that")
print(f"\\\\Weighted\ Average\ =\ \\frac{{\\sum_{{i=1}}^{{n}} (scores * weights)}}{{\\sum_{{i=1}}^{{n}} weights}}")
print("\\\\Summing\\ the\\ relevant\\ columns\\ in\\ the\\ table,\\ we\\ get")
print(f"\\\\\\sum_{{i=1}}^{{n}} (scores * weights) = {sum_weighted_scores}")
print(f"\\\\\\sum_{{i=1}}^{{n}} weights = {sum_weights}")
print(f"\\\\Weighted\ Average\ =\ \\frac{{{sum_weighted_scores}}}{{{sum_weights}}}")
print(f"\\\\Weighted\ Average\ =\ {round(sum_weighted_scores/sum_weights, 4)}")
print("Please hit thumbs up if the answer helped you")