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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing.
Create a set of possible telemarketers:
these are numbers that make outgoing calls but NEVER send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>

The list of numbers should be:
print out one per line 
in lexicographic order 
with no duplicates.
"""

def is_telemarketer(calls, texts):
    """ 
    Function takes data, fills set A and set B, 
    with respect to conditions given,
    return list of possible telemarketers;
    O(n) time 
    """
    telemarketers = set()
    not_telemarketers = set()


    for call in calls:
        callers_calls = call[0]
        receiver_calls = call[1]

        not_telemarketers.add(receiver_calls)

        if callers_calls not in receiver_calls:
            telemarketers.add(callers_calls)
            

    for text in texts:
        senders_texts = text[0]
        receiver_texts = text[1]

        if senders_texts in telemarketers:
            not_telemarketers.add(senders_texts)
        if receiver_texts in telemarketers:
            not_telemarketers.add(receiver_texts)

    intersection = telemarketers - not_telemarketers

    print("These numbers could be telemarketers: ")
    print(*sorted(intersection), sep='\n') # Timsort Worst case - O(n log(n)) time complexity
    print(len(intersection))
    
is_telemarketer(calls, texts)
