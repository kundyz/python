# Dependencies
import os
import csv

# Path to csv
budget_data_csv = os.path.join('Resources', 'budget_data.csv')
budgetList = list()

# Openning csv
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile) 
    for row in csvreader:
        dateValueTuple = (row[0], int(row[1]))
        budgetList.append(dateValueTuple)

monthCounter = 0
netTotalAmount = 0
previousValue = 0
totalChange = 0
greatestIncrease = ('',0)
greatestDecrease = ('',0)
for i, dateValueTuple in enumerate(budgetList):
    currentDate = dateValueTuple[0]
    currentValue = dateValueTuple[1]
    # The total number of months included in the dataset
    monthCounter = monthCounter + 1
    # The net total amount of "Profit/Losses" over the entire period
    netTotalAmount = netTotalAmount + currentValue
    # The average of the changes in "Profit/Losses" over the entire period
    changeInProfit = currentValue - previousValue
    if i != 0:
        totalChange = totalChange + changeInProfit
    previousValue = currentValue
    # The greatest increase in profits (date and amount) over the entire period
    if greatestIncrease[1] < changeInProfit:
        greatestIncrease = (currentDate, changeInProfit)
    # The greatest decrease in losses (date and amount) over the entire period
    if greatestDecrease[1] > changeInProfit:
        greatestDecrease = (currentDate, changeInProfit)

# Printing output
print('Financial Analysis')
print('----------------------')
print(f"Total Months: {monthCounter}")
print(f'Total: ${netTotalAmount}')
print(f'Average Change: ${round(totalChange/(monthCounter-1),2)}')
print(f'Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})')
print(f'Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})')