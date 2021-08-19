# Modules
import os
import csv

#Set path for file
#csvpath = os.path.join("Resources", "budget_data.csv")
csvpath = r"C:\Users\Guest1\Documents\Bootcamp\Homework1\python-challenge\PyBank\Resources\budget_data.csv"

month_count = 0
total_prof_loss = 0
total_change = 0


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    

    for row in csvreader:
        
        prev_month = int(row[1])

        #Count of total months
        month_count += 1

        #Total of Profit/losses
        month_prof_loss = int(row[1])
        total_prof_loss += month_prof_loss    

        #Calculate total 'change'
        if month_count == 1:
            prev_month = int(row[1])
        else:
            current_month = int(row[1])
            month_change = current_month - prev_month
            total_change = month_change + total_change
            prev_month = current_month

average_change = total_change / month_count

        
print("Total Months: ", month_count)
print("Total Profit or Loss :", total_prof_loss)
print("Average Change :", average_change)
print(total_change)

    

