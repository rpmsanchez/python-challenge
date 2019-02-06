import os
import csv

print("Election Results")
print("-----------------------------")

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #eliminate header
    csv_header = next(csvfile)

    totalvotes = 0
    khan = 0
    correy = 0
    li = 0
    otooley = 0
    for row in csvreader:
        totalvotes += 1

        if str(row[2]) == "Khan":
            khan += 1
        if str(row[2]) == "Correy":
            correy += 1
        if str(row[2]) == "Li":
            li += 1
        if str(row[2]) == "O'Tooley":
            otooley += 1


    khanper = (khan/totalvotes) * 100
    correyper = (correy/totalvotes) * 100
    liper = (li/totalvotes) * 100
    otooleyper = (otooley/totalvotes) * 100

    winner = ""
    if khan > correy and khan > li and khan > otooley:
        winner = "Khan"
    if correy > khan and correy > li and correy > otooley:
        winner = "Correy"
    if li > khan and li > correy and li > otooley:
        winner = "Li"
    if otooley > khan and otooley > correy and otooley > li:
        winner = "O'Tooley"
    

    
    print("Total Votes: " + str(totalvotes))
    print("----------------------------------")
    print("Khan: " + str(round(khanper,5)) + "% (" + str(khan) + ")")
    print("Correy: " + str(round(correyper,5)) + "% (" + str(correy) + ")")
    print("Li: " + str(round(liper,5)) + "% (" + str(li) + ")")
    print("O'Tooley: " + str(round(otooleyper,5)) + "% (" + str(otooley) + ")")
    print("Winner: " + winner)


#round(,2)
