import math
import scipy.stats as st

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
print(observed_data_with_sums)

expected_data = [[] for i in range(number_row)]
for i in range(number_row):
    for j in range(number_column):
        temp_expected_frequency = round((observed_data_with_sums[i][-1]/observed_data_with_sums[-1][-1])*observed_data_with_sums[-1][j], 4)
        expected_data[i].append(temp_expected_frequency)
print(expected_data)

observed_minus_expected_data = [[] for i in range(number_row)]
for i in range(number_row):
    for j in range(number_column):
        temp_observed_minus_expected = round(observed_data_with_sums[i][j]-expected_data[i][j], 4)
        observed_minus_expected_data[i].append(temp_observed_minus_expected)
print(observed_minus_expected_data)

observed_minus_expected_squared_data = [[] for i in range(number_row)]
for i in range(number_row):
    for j in range(number_column):
        temp_observed_minus_expected_squared = round(observed_minus_expected_data[i][j]**2, 4)
        observed_minus_expected_squared_data[i].append(temp_observed_minus_expected_squared)
print(observed_minus_expected_squared_data)

observed_minus_expected_squared_by_expected_data = [[] for i in range(number_row)]
for i in range(number_row):
    for j in range(number_column):
        temp_observed_minus_expected_squared_by_expected = round(observed_minus_expected_squared_data[i][j]/expected_data[i][j], 4)
        observed_minus_expected_squared_by_expected_data[i].append(temp_observed_minus_expected_squared_by_expected)
print(observed_minus_expected_squared_by_expected_data)

test_statistic = 0
for i in range(len(observed_minus_expected_squared_by_expected_data)):
    test_statistic += sum(observed_minus_expected_squared_by_expected_data[i])
print(test_statistic)
test_statistic = round(test_statistic, 4)

critical_value = st.chi2.ppf(round(1-alpha, 4), round((number_row-1)*(number_column-1), 4))

