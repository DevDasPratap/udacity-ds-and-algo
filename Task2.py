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
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

class Solver:
    def __init__(self,texts,calls):
        self.texts = texts
        self.calls = calls

    def number_spent_the_longest_time (self):
        
        number_dict = {}
        for c in self.calls: 
            if c[0] in number_dict :
                number_dict[c[0]] += int(c[3])
            else :
                number_dict[c[0]] = int(c[3])
            if c[1] in number_dict :
                number_dict[c[1]] += int(c[3])
            else:
                number_dict[c[1]] = int(c[3])

        longestKey = max(number_dict, key=number_dict.get)

        print (f'{longestKey} spent the longest time, {number_dict[longestKey]} seconds, on the phone during  September 2016.')
  

if __name__ == "__main__":
    solver = Solver(texts,calls)
    solver.number_spent_the_longest_time()  ## the run time analysis is O(n). 