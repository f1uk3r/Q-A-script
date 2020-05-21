import math
import scipy.stats as st
from tabulate import tabulate

null = str(input("Statement of null hypothesis (don't use any latex signs): "))
alternative = str(input("statement of alternative hypothesis (don't use any latex signs): "))
number_row = int(input("How many rows? "))
number_column = int(input("How many column? "))
alpha = float(input("alpha = "))

observed_data = []
for i in range(number_row):
    temp_row_list = list(map(float, input(f"Input all the values in row {i+1}: ").split()))
    observed_data.append(temp_row_list)

observed_data_with_sums = observed_data[:]
sum_column_temp_list = [0 for i in range(number_column+1)]
for i in range(number_row):
    observed_data_with_sums[i].append(sum(observed_data_with_sums[i]))
    for j in range(number_column+1):
        sum_column_temp_list[j] += observed_data_with_sums[i][j]
observed_data_with_sums.append(sum_column_temp_list)


expected_data = [[] for i in range(number_row)]
for i in range(number_row):
    for j in range(number_column):
        temp_expected_frequency = round((observed_data_with_sums[i][-1]/observed_data_with_sums[-1][-1])*observed_data_with_sums[-1][j], 4)
        expected_data[i].append(temp_expected_frequency)


observed_minus_expected_data = [[] for i in range(number_row)]
for i in range(number_row):
    for j in range(number_column):
        temp_observed_minus_expected = round(observed_data_with_sums[i][j]-expected_data[i][j], 4)
        observed_minus_expected_data[i].append(temp_observed_minus_expected)


observed_minus_expected_squared_data = [[] for i in range(number_row)]
for i in range(number_row):
    for j in range(number_column):
        temp_observed_minus_expected_squared = round(observed_minus_expected_data[i][j]**2, 4)
        observed_minus_expected_squared_data[i].append(temp_observed_minus_expected_squared)


observed_minus_expected_squared_by_expected_data = [[] for i in range(number_row)]
for i in range(number_row):
    for j in range(number_column):
        temp_observed_minus_expected_squared_by_expected = round(observed_minus_expected_squared_data[i][j]/expected_data[i][j], 4)
        observed_minus_expected_squared_by_expected_data[i].append(temp_observed_minus_expected_squared_by_expected)


test_statistic = 0
for i in range(len(observed_minus_expected_squared_by_expected_data)):
    test_statistic += sum(observed_minus_expected_squared_by_expected_data[i])
test_statistic = round(test_statistic, 4)


critical_value = round(st.chi2.ppf(round(1-alpha, 4), round((number_row-1)*(number_column-1), 4)), 4)


print(f"Rows (r) = {number_row}")
print(f"Column (c) = {number_column}")
print(f"\\\\\\text{{Null Hypothesis: }}H_0: \\text{{{null}}}")
print(f"\\\\\\text{{Alternate Hypothesis: }}H_1: \\text{{{alternative}}}")
print(f"\\\\\\alpha = {alpha}")
print(f"\\\\\\text{{Observed data with sums (O)}}")
print("\\\\" + tabulate((observed_data_with_sums), tablefmt="latex"))
print(f"\\\\\\text{{Expected frequencies(E)}}")
print("\\\\" + tabulate((expected_data), tablefmt="latex"))
print(f"\\\\\\text{{O - E}}")
print("\\\\" + tabulate((observed_minus_expected_data), tablefmt="latex"))
print("\\\\\\text{(O - E)}^2")
print("\\\\" + tabulate((observed_minus_expected_squared_data), tablefmt="latex"))
print(f"\\\\\\frac{{\\text{{(O - E)}}^2}}{{\\text{{E}}}}")
print("\\\\" + tabulate((observed_minus_expected_squared_by_expected_data), tablefmt="latex"))
print("The test statistic is: ")
print("\\\\\\chi_0^2 = \\sum_{i=1}^r\\sum_{j=1}^c\\frac{(O_{ij}-E_{ij})^2}{E_{ij}}")
print(f"\\\\\\chi_0^2 = ", end="")
for each_list in observed_minus_expected_squared_by_expected_data:
    for every_element in each_list:
        print(f"{every_element} + ", end="")
print("")
print(f"\\\\\\chi_0^2 = {test_statistic}")
print(f"The critical value is:")
print(f"\\\\\\chi_{{\\alpha, (r-1)(c-1)}}^2 = \\chi_{{{alpha}, {round((number_row-1)*(number_column-1), 4)}}}^2 = {critical_value}")
print(f"\\\\\\text{{Decision Rule: Reject the null hypothesis if test statistic is greater than critical value i.e., at }}\\chi_0^2 > \\chi_{{{alpha}, {round((number_row-1)*(number_column-1), 4)}}}")
if test_statistic < critical_value:
    print(f"\\\\\\text{{Since, }} \\chi_0^2 < \\chi_{{{alpha}, {round((number_row-1)*(number_column-1), 4)}}}\\text{{, do not reject the null hypothesis and conclude that the data provides insufficient evidence to claim the alternate hypothesis at }}\\alpha\\text{{ = {alpha}}}")
else:
    print(f"\\\\\\text{{Since, }} \\chi_0^2 > \\chi_{{{alpha}, {round((number_row-1)*(number_column-1), 4)}}}\\text{{, reject the null hypothesis and conclude that the data provides sufficient evidence to claim the alternate hypothesis at }}\\alpha\\text{{ = {alpha}}}")

print ("Please hit thumbs up if the answer helped you.")