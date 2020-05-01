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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

class Solver:
    def __init__(self,texts,calls):
        self.texts = texts
        self.calls = calls

    def first_record (self):
        record = self.texts[0] 
        print (f'First record of texts, {record[0]} texts {record[1]} at time {record[2]}')
    
    def last_record (self):
        record = self.calls[len(self.calls)-1] 
        print (f'Last record of calls, {record[0]} calls {record[1]} at time {record[2]}, lasting {record[3]} seconds')

if __name__ == "__main__":
    solver = Solver(texts,calls)
    solver.first_record()  ## the run time analysis is O(1). 
    solver.last_record() ## the run time analysis is O(1). 

