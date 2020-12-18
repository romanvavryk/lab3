from tabulate import tabulate
import pandas as pd

f_string = [i.strip('\n').split(',') for i in open('data.txt')]

for i in range(0 ,5):
	for j in range(0, 1):
		f_string[i][j] = int(f_string[i][j])

def condorce():
	headers = ['Name', 'AB', 'AC', 'BA', 'BC', 'CA', 'CB', 'Winner']

	ab = 0
	ac = 0
	ba = 0
	bc = 0
	ca = 0
	cb = 0

	value = f_string[0]
	for i in range(0, 5):
		for j in range(1, 4):
			if f_string[i][j] == 'A':
				A_index = f_string[i].index('A')
			elif f_string[i][j] == 'B':
				B_index = f_string[i].index('B')
			if f_string[i][j] == 'C':
				C_index = f_string[i].index('C')

		if A_index < B_index:
			ab += f_string[i][0]
		else:
			ba += f_string[i][0]
		if A_index < C_index:
			ac += f_string[i][0]
		else:
			ca += f_string[i][0]

		if B_index < C_index:
			bc += f_string[i][0]
		else:
			cb += f_string[i][0]
	
	
	A_vote = ab + ac
	B_vote = ba + bc
	C_vote = ca + cb

	results = [A_vote, B_vote, C_vote]
	variety = ['A', 'B', 'C']
	
	result = max(results)
	result_index = results.index(result)
	result_name = variety[result_index] 

	results = ['Condorce', ab, ac, ba, bc, ca, cb, result_name]

	print(tabulate([results], headers=headers, tablefmt='orgtbl'))

def bord_method():
	headers = ['Name', 'A', 'B', 'C', 'Winner']
	candidate_A_votes = []
	candidate_B_votes = []
	candidate_C_votes = []
	total_votes = [candidate_A_votes, candidate_B_votes, candidate_C_votes] 
	results = []

	def counter():
		for i in range(0, 5):
			for j in range(1, 4):  
				if f_string[i][j] == 'A':
					candidate_A_votes.append(f_string[i].index('A'))
				elif f_string[i][j] == 'B':
					candidate_B_votes.append(f_string[i].index('B'))
				elif f_string[i][j] == 'C':
					candidate_C_votes.append(f_string[i].index('C'))

		for i in range(0, 3):
			for j in range(0, 5):
				if total_votes[i][j] == 1:
					total_votes[i][j] = 2
				elif total_votes[i][j] == 2:
					total_votes[i][j] = 1
				elif total_votes[i][j] == 3:
					total_votes[i][j] = 0

		for votes in total_votes:
			for j in range (0, 5):
				votes[j] *= f_string[j][0]

		for i in total_votes:
			results.append(sum(i))

	counter()

	win_result = max(results)
	result_index = results.index(win_result) + 1
	result_name = headers[result_index]

	results.append(result_name)
	results.insert(0, 'Bord')

	print(tabulate([results], headers=headers, tablefmt='orgtbl'))

bord_method()
print()
condorce()