'''
Python homework - PyRamen
By Ying Fu

This script will analyze Ramen's financial performance by cross-referencing sales data with internal menu data to figure out revenues and costs for the year. 
'''
#Import from the pathlib library, the main class Path
from pathlib import Path
import csv

#Define a function to read the csv files
def read_csv(path):
    #Set the input file path
    csvpath = Path(path)
    #Initialize an empty list
    empty_list = []
    #Open the menu_data in "read"mode and store the contents in the variable "csvreader"
    with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        #Skip the the header and iterate the "csvreader" file line by line to append to empty list.
        header = next(csvreader)
        for data in csvreader:
            empty_list.append(data)
    return empty_list

#call read_csv function to read menu_data.csv and sales_data.csv and store in menu and sales seperately.         
menu = read_csv('./menu_data.csv')
sales = read_csv('./sales_data.csv')
        
#Initialize variables        
report={}
count = 0
row_count = 0
row_count_j = 0
item = []
price = []
cost = []
quantity = []
menu_item = []
sale_item = []

# Run a for loop in "sales"
for sale in sales:
    count += 1
    quantity.append(sale[3]) # to get "quantity" list
    menu_item.append(sale[4])# to get "menu_item" list
    #Create report dictionary to hold the future aggregated per_product results.
    if sale[4] not in report:
        sale_item.append(sale[4])
        report[sale[4]] = {
"01-count": 0,
"02-revenue": 0,
"03-cogs": 0,
"04-profit": 0,
}

print(f" Total number of records in sales data is {count}")
        
# Convert strings in quantity list to integers
quantity = [int(i) for i in quantity]

#Run a for loop in "menu" to get "item" list, "price" list and "cost" list
for row in menu:
    item.append(row[0])
    price.append(row[3])
    cost.append(row[4])
#Convert strings in "price" and "cost" lists to floats
price = [float(i) for i in price]
cost = [float(i) for i in cost]
#Create a nested loop if the sales_item in sales is equal to the item in menu, capture the quantity from the sales data and the price and cost from the menu data to calculate the profit for each item.
for i in sale_item:
    row_count_j = 0
    for j in item:
        row_count_j += 1
        row_count = 0
        if j == i:
             for k in menu_item:
                row_count += 1
                if k == j:
                    report[i]["01-count"] += quantity[(row_count-1)]
                    report[i]["02-revenue"] += price[(row_count_j-1)] *quantity[(row_count-1)]
                    report[i]["03-cogs"] += cost[(row_count_j-1)] * quantity[(row_count-1)]
                    report[i]["04-profit"] += (price[(row_count_j-1)]-cost[(row_count_j-1)]) *quantity[(row_count- 1)]      
                else:
                    pass
        else:
            print(f"{i} does not equal {j}!NO MATCH!")
              
print(report)

#Set the output file path
output_path = Path("./report.txt")
##open the output_path as a file object in "write" mode ('w')
#
with open(output_path, "w") as text:
    for info in report:
        text.write(f"{info} {report[info]}\n")
