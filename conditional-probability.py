legend2 = '''
1. A, B and (A or B) are given
2. A, B and (A and B) are given
3. A, B and (A|B) are given
'''

print("Which of the following case is given?")
case = int(input(str(legend2)))
if case == 1:
	print(''' Subcase2:
		1. Find (A and B)
		2. Find (A|B)
		3. Find (B|A)
		''')
	parts = int(input("How many parts?"))
	for i in range(parts):
		subcase = int(input("Select one of the subcase2: "))
		if subcase == 1:
			pa = float(input("P(A) = "))
			pb = float(input("P(B) = "))
			pAorB = float(input("\\\\P(A \cup B) = "))
			print("Since we know that,")
			print("\\\\P(A \cup B)= P(A) + P(B) - P(A \cap B)")
			print("\\\\" + str(pAorB) + " = " + str(pa) + " + " + str(pb) + " - P(A \cap B")
			print("P(A \cap B) = " + str(round(pa+pb-pAorB, 4)))
		elif subcase == 2:
			pa = float(input("P(A) = "))
			pb = float(input("P(B) = "))
			pAandB = float(input("\\\\P(A \cap B) = "))
			print("Since we know that, ")
			print("P(A|B) = \\frac{P(A \cap B)}{P(B)}")
			print("P(A|B) = \\frac{" + str(pAandB) + "}{" + str(pb) + "}")
			print("P(A|B) = " + str(round(pAandB/pb, 4)))
		elif subcase == 3:
			pa = float(input("P(A) = "))
			pb = float(input("P(B) = "))
			pAgivenB = float(input("\\\\P(A|B) = "))
			print("Since we know that.")
			print("P(A \cap B) = P(A|B) * P(B)")