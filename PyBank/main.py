import os
import csv

print("Financial Analysis")
print("-----------------------------")

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #eliminate header
    csv_header = next(csvfile)

    monthcount = 0
    total = 0
    delta = 0
    totaldelta = 0
    for x, y in csvreader:
        monthcount += 1

        total += int(y)

       


            
        #if int(y) != int(next_y):
         #   delta = int(next_y) - int(y)
          #  totaldelta += delta                
           # print(str(delta))
        
            
    
        
    print("Total Months: " + str(monthcount))
    print("Total:" + str(total))
    print(totaldelta)






        
        