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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

class Solver:
    def __init__(self,texts,calls):
        self.texts = texts
        self.calls = calls

    def number_of_telemarketers (self):
        print (f'These numbers could be telemarketers:')
        call_sending_telephone = [] 
        exclude = [] 
        for t in self.texts :
            exclude.append(t[0]) 
            exclude.append(t[1]) 
        for c in self.calls :
            call_sending_telephone.append(c[0]) 
            exclude.append(c[1]) 

        call_set = list(set(call_sending_telephone))

        lexicographic = [] 
        for o in call_set : 
            if o not in exclude :
                lexicographic.append(o)
        sortedL = sorted(lexicographic)
        for l in sortedL: 
            print (l)

if __name__ == "__main__":
    solver = Solver(texts,calls)
    solver.number_of_telemarketers()  ## the run time analysis is O(n). 
