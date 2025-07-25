"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? So, only for calls; 
Don't forget that time spent answering a call is
also time spent on the phone.

Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016." 
"""
"""
PROBLEM DECOMPOSITION:
Get a tel_num that spent the longest time;
	for loop through data and implement logic of cum.sum
return the tel_num that spent max of total time (cum.sum);
during September 2016 - data is 2016, and all are 09/September
"""

def cum_sum_duration(dictionary, phone_number, call_duration):
    """ 
	Complement function performs cummulative sum of call_duration per phone_number;
    O(n) time 
    """
    # if there is not phone_number in dictionary add it;
    if dictionary.get(phone_number) == None:
        dictionary[phone_number] = call_duration
        
    # if it is present cummulate the sum;
    else:
        dictionary[phone_number] = int(dictionary.get(phone_number)) + int(call_duration)

    return dictionary

def get_result(data):
    """ 
    Function returns phone number which spent the longest time on the phone,
    and also the time spent in seconds;
    O(n) time 
    """
    dictionary = {}
    for col in data:
        caller_number = col[0]
        reciever_number = col[1]
        call_duration = col[3]
        
        dictionary = cum_sum_duration(dictionary, caller_number, call_duration)
        dictionary = cum_sum_duration(dictionary, reciever_number, call_duration)
    
    max_call = max(dictionary.items(), key = lambda x: int(x[1]))
    
    return print("{} spent the longest time, {} seconds, on the phone during September 2016."
                	.format(max_call[0], max_call[1]))

get_result(calls)

