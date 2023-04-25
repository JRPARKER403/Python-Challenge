import os
import csv

#budget_data_csv ='"C:\Users\JMARS\OneDrive\Desktop\Bootcamp\HOMEWORK\python-challenge\PyBank\analysis\budget_data.csv"'

# Open and read csv
with open(budget_data.csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")

total_volume = 0
total_months = 0
previous_value = 0
total_changes = 0

greatest_increase = 0
greatest_decrease = 99999999

total_profit = 0
monthly_profit_change = 0

for row in csv_reader:
        
        print(row)
        print(row[0])

        first_name = row[0]
        phone_number = row[2]

        total_months += 1
        total_volume +=float(row[1])

        current_value = float(row[1])
        change = current_value - Previous_value

        if change > greatest_increase:
              greatest_increase = change
              greatest_increase_month = row[0]

        if change < greatest_decrease:
              greatest_decrease = change
              greatest_decrease_month = row[0]     

        previous_value = float(row[1])

        total_changes=+change

average_volume = total_changes / total_months - 1

#print out greatest increase and greatest_increase_month





    