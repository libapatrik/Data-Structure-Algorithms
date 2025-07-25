"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from functools import reduce
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: 
Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line 
in lexicographic order 
with no duplicates.
"""

def extract_code(phone_number):
	""" O(n) time 
	Given the phone number, the function extracts classifies:
	if its Fixed line, Mobile, Telemarketer;
	"""
	# Fixed line;
	if phone_number.startswith('('):
		return phone_number[1:phone_number.find(')')]
	# Mobile;
	elif phone_number.startswith('7') or phone_number.startswith('8') or phone_number.startswith('9'):
		return phone_number[0:4]
	# Telemarketer;
	else:
		return '140'


def reducer(acc, tup):
	""" O(n) time
	Function creates a list of
	If call is made from Bangalore:
	append it with extraction to the end - O(1) time.
	if receiver is not in list:
	append it with extraction to the end
	return numbers called by Bangalore people;
	"""
	caller_number = tup[0]
	receiver_number = tup[1]
	if caller_number.startswith('(080)'):
		acc.append(extract_code(caller_number))
		if receiver_number not in acc:
			acc.append(extract_code(receiver_number))
	return acc

codes = reduce(reducer, calls, [])

print("The numbers called by people in Bangalore have codes:")
print(*sorted(set(codes)), sep='\n') # Worst case - O(n log(n)) time complexity

"""
Part B: 
What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore?
In other words, 
of all the calls made
from a number starting with "(080)" = caller, 
what percentage of these calls
were made to a number also starting with "(080)"?
(080) -> (080); within Bangalore

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# All calls made starting (080); caller (080) to wherever
def reducer_caller_from_Bangalore(acc, tup):
	""" O(n) time """
	caller_number = tup[0] 
	if caller_number.startswith('(080)'):
		acc.append(caller_number)
	return acc

# All calls within Bangalore
def reducer_from_Bangalore_to_Bangalore(acc, tup):
	""" O(n) time """
	caller_number = tup[0]
	receiver_number = tup[1] 
	if caller_number.startswith('(080)') & receiver_number.startswith('(080)'):
		acc += 1
	return acc

code_caller_from_Bangalore = reduce(reducer_caller_from_Bangalore, calls, []) 
code_from_Bangalore_to_Bangalore = reduce(reducer_from_Bangalore_to_Bangalore, calls, 0) 

# Get the percentage and print it out; 
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
		.format(round((code_from_Bangalore_to_Bangalore/len(code_caller_from_Bangalore)*100), 2)))

