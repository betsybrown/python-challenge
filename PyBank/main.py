import os
import csv


csvpath=os.path.join('..','PyBank','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    #first_row = next(csvreader)
    

    #print(f"CSV Header = {csv_header}")
    # print(first_row)

    # total_number_of_months = 0
    total_months = 0
    total_amount = 0
  
    #difference of previous row
    net_change = 0
    last_month_profit = 0
    greatestIncrease = 0
    greatestDecrease = 0
    profit_change_list =[]
    profit_change_date = []
 

    for rows in csvreader:
        #print(rows)
        total_months = total_months + 1
        
        total_amount = total_amount + int(rows[1])
        
        profit = rows[1]
        date = rows[0]
        change = int(profit) - int(last_month_profit)
        profit_change_list.append(change)
        profit_change_date.append(date)
        last_month_profit = profit
   

  
 
    for number in profit_change_list:
        if number > greatestIncrease:
             greatestIncrease = number
    
  
    for number in profit_change_list:
        if number < greatestDecrease:
            greatestDecrease = number

    avg_profit_change = sum(profit_change_list[1:]) /(len(profit_change_list)-1.0)
    ggindex = profit_change_list.index(greatestIncrease)
    gglindex = profit_change_list.index(greatestDecrease)


    
    summary = (
            "Financial Analysis\n" 
            "-----------------------------------\n" 
            f'Total Months: {total_months}\n'
            f'Total:  ${total_amount}\n' 
            f'Average Change: {avg_profit_change:.2f}\n'
            f'Greatest Increase in Profits: {profit_change_date[ggindex]}{" "} ${greatestIncrease}\n'
            f'Greatest Decrease in Profits: {profit_change_date[gglindex]}{" "} ${greatestDecrease}\n'
        )

print("========")
print(summary)
    
# import sys
import os.path
# import subprocess
# with open("Financial Analysis.txt", "w+") as output:
#     subprocess.call(["python", "./main.py"], stdout=output);
    
    
#orig = sys.stdout
with open(os.path.join('..','PyBank', "Financial Analysis2.txt"), "w") as f:
    f.write(summary)

    """sys.stdout = f
    try:
        execfile("main.py", {})
    finally:
        sys.stdout = orig"""