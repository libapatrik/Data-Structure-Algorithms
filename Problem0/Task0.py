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
The text data (text.csv) has the following columns: 
sending telephone number (string), - odosielatel spravy - incoming number 1st ele
receiving() telephone number (string), - prijemca spravy - answering number 2nd ele
timestamp of text message (string). - v casovom bode - time last ele

The call data (call.csv) has the following columns: 
calling telephone number (string),
receiving telephone number (string),
start timestamp of telephone call (string),
duration of telephone call in seconds (string), 

TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls,  calls <answering number> at time <time>, lasting <during> seconds"
"""

def texts_task(data):
	""" O(1) time """
	FirstRecord = data[0][0]
	AnsweringNumber = data[0][1]
	Time = data[0][-1]
	return print("First record of texts, {}, texts {} at time {}"
	.format(FirstRecord, AnsweringNumber, Time))

def calls_task(data):
	""" O(1) time """
	LastRecord = data[-1][0]
	AnsweringNumber = data[-1][1]
	TimeStamp = data[-1][2]
	Seconds = data[-1][3]
	return print("Last record of calls, {}, calls {} at time {}, lasting {} seconds"
	.format(LastRecord, AnsweringNumber, TimeStamp, Seconds))

texts_task(texts)
calls_task(calls)
