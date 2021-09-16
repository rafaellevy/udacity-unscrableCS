"""
Read file into texts and calls.
It's ok if you don't understand how to read files

TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

times = {}

for call in calls:
    if call[0] not in times.keys():
        times[call[0]] = int(call[3])
    if call[1] not in times.keys():
        times[call[1]] = int(call[3])
    else:
        times[call[0]] = times[call[0]] + int(call[3])
        times[call[1]] = times[call[1]] + int(call[3])

    
duration = (max(times.values()))

phoneNumber = max(times,key=times.get)


print('''%s spent the longest time, %s seconds, on the phone during 
September 2016.'''%(phoneNumber,duration))

"""Time complexity is O(n)"""


