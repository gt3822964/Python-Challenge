import csv
import os

# Loading the file with the right path
file_path = os.path.join("Resources", "budget_data.csv")

# beginning value of the variables 
TotalMonths = 0
NetTotal = 0
changes = []  # To store the changes in "Profit/Losses"

# start variables to store the date and amount of the greatest increase and decrease in profits
greatest_increase_date = ""
greatest_increase_amount = 0  # beginning value
greatest_decrease_date = ""
greatest_decrease_amount = 0  # beginning value

# open the file with the mode read
with open(file_path, mode='r') as file:
    
    csv_reader = csv.reader(file)
    
    # Skip the header row because the data in header is useless
    next(csv_reader)
    
    # Initialize previous_value to None as there is no previous month for the first row
    previous_value = None
    previous_date = ""  # This variable will store the date of the previous row
    
    # beginning of the loop
    for row in csv_reader:
        TotalMonths += 1  # Increment the month count for every row
        date = row[0]  # Date is in the first column
        value = int(row[1])  # "Profit/Losses" is in the second column, [0] is the first column
        NetTotal += value  # Sum the "Profit/Losses"
        
        # If previous_value is not None, calculate the change and append to changes list
        if previous_value is not None:
            change = value - previous_value
            changes.append(change)
            
            # Update greatest increase and decrease variables as needed through each row
            # conditions are here
            if change > greatest_increase_amount:
                greatest_increase_date = previous_date
                greatest_increase_amount = change
            elif change < greatest_decrease_amount:
                greatest_decrease_date = previous_date
                greatest_decrease_amount = change
        
        # Update previous_value and previous_date for the next iteration
        previous_value = value
        previous_date = date

# Calculate the average change
average_change = sum(changes) / len(changes) if changes else 0

# display the final data as required
print("Financial Analysis")
print("----------------------------------")
print("Total Months: ", TotalMonths)
print("Total: ", NetTotal)
print("Average Change: ", round(average_change, 2))
print("Greatest Increase in Profits: ", greatest_increase_date, greatest_increase_amount)
print("Greatest Decrease in Profits: ", greatest_decrease_date, greatest_decrease_amount)
