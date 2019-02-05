import os
import csv

print("Financial Analysis")
print("-----------------------------")

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    monthcount = 0
    for row in csvreader:
        monthcount = monthcount + 1
        
    print("Total Months: " + str(monthcount))


        
        