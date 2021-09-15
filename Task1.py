"""
Read file into texts and calls.
It's ok if you don't understand how to read files.

TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

callsList = set() 
textsList = set()

for call in calls:
    callsList.add(call[0])
    callsList.add(call[1])

for text in texts:
    textsList.add(text[0])
    textsList.add(text[1])

result = callsList | textsList

print("There are " + str(len(result)) + " different telephone numbers in the records.")




