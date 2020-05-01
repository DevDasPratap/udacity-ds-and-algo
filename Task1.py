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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."

The text data (text.csv) has the following columns: sending telephone number (string), receiving telephone number (string), timestamp of text message (string).

The call data (call.csv) has the following columns: calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)


"""

class Solver:
    def __init__(self,texts,calls):
        self.texts = texts
        self.calls = calls

    def different_telephone_numbers (self):
        numbers=[]
        for i in self.texts :
            numbers.append(i[0])
            numbers.append(i[1])
        for i in self.calls :
            numbers.append(i[0])
            numbers.append(i[1])
        print (f'There are {len(list(dict.fromkeys(numbers)))} different telephone numbers in the records.')
  

if __name__ == "__main__":
    solver = Solver(texts,calls)
    solver.different_telephone_numbers()  ## the run time analysis is O(n). 