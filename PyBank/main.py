# Modules
import os
import csv

#Set path for file
#csvpath = os.path.join("Resources", "budget_data.csv")
csvpath = r"C:\Users\Guest1\Documents\Bootcamp\Homework1\python-challenge\PyBank\Resources\budget_data.csv"

month_changes = []
month_count = 0
total_prof_loss = 0
month_change = 0
greatest_increase = 0
greatest_decrease = 0


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    

    for row in csvreader:     
        
        #Count of total months
        month_count += 1

        #Total of Profit/losses
        month_prof_loss = int(row[1])
        total_prof_loss += month_prof_loss    

        #Calculate total 'change'
        if month_count == 1:
            prev_month = month_prof_loss
            continue

        else:
            month_change = month_prof_loss - prev_month
            month_changes.append(month_change)            
            prev_month = month_prof_loss
            
            #calculate greatest increase and decrease and define relative month
            if greatest_increase < month_change:
                greatest_increase = month_change
                month_of_greatest_increase = row[0]
            if greatest_decrease > month_change:
                greatest_decrease = month_change
                month_of_greatest_decrease = row[0]
        
#Calculate average change
total_change = sum(month_changes)
average_change = total_change / (month_count - 1)

#Define whether there was a profit or a loss
if total_prof_loss >0:
    profit_or_loss = str("Profit")
else:
    profit_or_loss = "Loss"

#Print outcomes
print(f"Total Months: {month_count} months")
print(f"Total {profit_or_loss}: ${total_prof_loss}")
print(f"Average profit/loss change: ${average_change}")
print(f"The month with the greatest increase is {month_of_greatest_increase} with an increase of ${greatest_increase}")
print(f"The month with the greatest decrease is {month_of_greatest_decrease} with a decrease of ${greatest_decrease}")
    

