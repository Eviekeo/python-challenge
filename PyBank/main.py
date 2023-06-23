#import the csv and os modules
import os
import csv


# Path to collect data from the Resources folder
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store data
date = []
profit_loss = []
change = []


# Open and read csv 
with open(budget_data_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Read the header row first 
    csv_header = next(csv_file)
    
    for row in csv_reader:
        date.append(row[0])
        profit_loss.append(int(row[1]))
        

    # Count the number of rows in the date column
    total_months = len(date)

    # fill in the empty 'change' list with the change in profit for each month
    for i in range(1,len(profit_loss)):
        change.append(profit_loss[i] - profit_loss[i-1])
        #calculate the average, max and min change
        average_change=sum(change)/len(change)
        max_change=max(change)
        min_change=min(change) 
        
        # obtain the corresponding date for max and min change - add 1 to the value as there is less values in the change data than in the profit_loss data
        max_change_date=str(date[change.index(max(change))+1])
        min_change_date=str(date[change.index(min(change))+1])


#save the output file path
output_file = os.path.join("Analysis","output.txt")

#open the output file, and print the output
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    #print the results
    output_1 = (f"Financial Analysis\n\n"
    f"---------------------------------------------------\n\n"
    f"Total Months:{str(total_months)}\n\n"
    f"Total: ${str(sum(profit_loss))}\n\n"
    f"Average Change: ${round(average_change,2)}\n\n"
    f"Greatest Increase in Revenue: {max_change_date} (${max_change})\n\n"
    f"Greatest Decrease in Revenue: {min_change_date} (${min_change})")
    print(output_1)
    datafile.write(output_1)
