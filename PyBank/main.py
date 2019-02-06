import os
import csv

print("Financial Analysis")
print("-----------------------------")

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #eliminate header
    csv_header = next(csvfile)

    firstrow = next(csvreader)
    monthcount = 1
    total = int(firstrow[1])
    previous = int(firstrow[1])
    delta = 0
    maxdelta = 0
    mindelta = 0
    totaldelta = 0
    maxdate = None
    mindate = None
    for x, y in csvreader:
        monthcount += 1

        total += int(y)

       
        delta = int(y) - previous 
        totaldelta += delta
        previous = int(y)
        if delta > maxdelta:
            maxdelta = delta
            maxdate = x
        if delta < mindelta:
            mindelta = delta
            mindate = x

            
        #if (y) != (y+1):
         #   delta = (y+1) - (y)
          #  totaldelta += delta                
           # print(delta)

    averagedelta = totaldelta/monthcount
    
        
            
    
        
    print("Total Months: " + str(monthcount))
    print("Total:" + str(total))
    print("Total Change " + str(totaldelta))
    print("Average Change: $" + str(averagedelta))
    print("Greatest Increase In Profits: " + str(maxdate) + " $" + str(maxdelta))
    print("Greatest Decrease In Profits: " + str(mindate) + " $" + str(mindelta))






        
        