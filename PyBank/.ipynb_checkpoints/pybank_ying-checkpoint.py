'''
Python homework - Pybank
By Ying Fu

This script will analyzes the budget_data.csv to calculate the following:
- The total number of months included in the dataset.
- The net total amount of Profit/Losses over the entire period.
- The average of the changes in Profit/Losses over the entire period.
- The greatest increase in profits (date and amount) over the entire period.
- The greatest decrease in losses (date and amount) over the entire period.
Then print the analysis results and export the analysis to a text file. 
'''
#Import from the pathlib library, the main class Path 
from pathlib import Path
import csv

#Set the input file path
csvpath = Path('./budget_data.csv')

#Initialize variables  
rows = []
count = 0
netpnl_amount = 0
change = 0
total_change = 0
greatest_increase = 0
greatest_decrease = 0

#Open the file in "read" mode and store the contents in the variable "csvreader"
with open(csvpath, 'r') as  csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #Skip the the header and iterate the "csvreader" file line by line to append to "rows"
    header = next(csvreader)                                      
    for row in csvreader:
        rows.append(row)
        #count rows to get the number of months
        count += 1
        #To calculate the net total profit and loss amout
        count_1 = count-1
        rows[count_1][1] = int(rows[count_1][1]) 
        netpnl_amount += rows[count_1][1]
        #To calculate average changes in Profit/Loss
        if count >1:
            count_2 = count-2
            change =(rows[count_1][1]-rows[count_2][1])
            total_change += change
            avg_change = round((total_change/count_1), 2)
            #To get the greatest _increase and the greatest_decrease and the corresponding dates for them
            if change >= greatest_increase:
                greatest_increase = change
                date_increase = rows[count_1][0]
            elif change <= greatest_decrease:
                greatest_decrease = change
                date_decrease = rows[count_1][0]
 #Print out the analysis results
    print("Financial Analysis")
    print("--------------------------------")
    print(f"The total number of months: {count}")
    print(f"The net total amount of Profit/Losses is ${netpnl_amount}")
    print(f"The average of the changes in Porfit/Losses is ${avg_change}")
    print(f"Greatest increase in Profits: {date_increase} (${greatest_increase})")
    print(f"Greatest decrease in Profits: {date_decrease} (${greatest_decrease})")

#Set the output file path
output_path = Path("./analysis.txt")
#open the output_path as a file object in "write" mode ('w')
#Write a header line and write the contents to the file
with open(output_path, 'w') as analysis:
    analysis.write("Financial Analysis\n")
    analysis.write("--------------------------------\n")
    analysis.write(f"The total number of months: {count}\n")
    analysis.write(f"The net total amount of Profit/Losses is ${netpnl_amount}\n")
    analysis.write(f"The average of the changes in Porfit/Losses is ${avg_change}\n")
    analysis.write(f"Greatest increase in Profits: {date_increase} (${greatest_increase})\n")
    analysis.write(f"Greatest decrease in Profits: {date_decrease} (${greatest_decrease})\n")
