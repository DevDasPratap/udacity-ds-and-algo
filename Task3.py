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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
class Solver:
    def __init__(self,texts,calls):
        self.calls = calls

    def codes (self):
        print('The numbers called by people in Bangalore have codes:')
        area_codes = {}
        for c in  self.calls : 
            if "(080)"  in c[0]: 
                if "(" in c[1]:
                    c_number = c[1].split(')')[0].replace('(','')
                    area_codes[c_number] = int(c_number)
                if c[1][0] in ['7','8','9'] :
                    c_num  = c[1][0:4]
                    area_codes[c_num] = int(c_num) 
       
        sorted_codes = sorted(area_codes.items(), key=lambda x: x[1])
        for s in sorted_codes:
            print (s[0])

    def percentage (self) :
        from_calls = [] 
        to_calls = []
        for c in  self.calls : 
            if c[0].find('(080)') != -1 : 
                from_calls.append(c[0])
                if  c[1].find('(080)') != -1 : 
                    to_calls.append(c[1])
        percent = len(to_calls) / len(from_calls) 
        two_bit = format(percent*100, '.2f') 
        print (f'{ two_bit} percent of calls from fixed lines in Bangalore are calls \n to other fixed lines in Bangalore.')
        

if __name__ == "__main__":
    solver = Solver(texts,calls)
    solver.codes()  ## the run time analysis is O(n). 
    solver.percentage()  ## the run time analysis is O(n). 
 