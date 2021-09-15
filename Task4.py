"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.
- Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.


Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
teleHellSet = set()
telemarketersPrefix = re.compile("^140")

for number in calls:
    if telemarketersPrefix.match(number[0]):
        teleHellSet.add(number[0])

teleHellList = list(teleHellSet)
teleHellList.sort()

print("These numbers could be telemarketers: ")
for teleNumber in teleHellList:
    print(teleNumber)







