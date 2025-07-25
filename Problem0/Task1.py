"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
"""
TASK 1:
How many different telephone numbers are there in the records?

Print a message:
"There are <count> different telephone numbers in the records."
"""
def unique_records(data1, data2): 
	""" O(n) time """
	numbers = []
	for i in range(len(data1)): 
		numbers.append(data1[i][0])
		numbers.append(data1[i][1])
	for j in range(len(data2)):
		numbers.append(data2[j][0])
		numbers.append(data2[j][1]) 
	return print("There are {} different telephone numbers in the records."
			.format(len(set(numbers))))


unique_records(calls, texts)

