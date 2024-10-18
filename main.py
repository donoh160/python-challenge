
import pandas as pd
from pathlib import Path
import statistics


# reads in the budget_data.csv as a pandas data frame
budget_data = Path("Resources/budget_data.csv")
budget_data = pd.read_csv(budget_data)
budget_df = pd.DataFrame(budget_data)

# creates list full month-to-month change in profit
monthly_change = []
prev_month_profit = 0
for index, row in budget_df.iterrows():
    profit = row['Profit/Losses']
    monthly_change.append(profit - prev_month_profit)
    prev_month_profit = profit
# removes first month since there is zero change
monthly_change.pop(0)

# all print statements will be exported into following txt file
f = open("analysis/financial_analysis.txt", "w")
print("Financial Analysis \n ----------------------------", file=f)

# calculates number of entries
total_months = len(budget_df["Date"])
print(f"Total Months: {total_months}", file=f)

# sums all profits from each month
net_profit = budget_df["Profit/Losses"].sum()
print(f"Total: {net_profit}", file=f)

# calculates the average change per month
avg_change = statistics.mean(monthly_change)
print(f"Average Change: {avg_change}", file=f)

# calculates the greatest change in monthly profits
max_increase = max(monthly_change)
print(f"Greatest Increase in Profits: {max_increase}", file=f)

# calculates the greatest decrease change in monthly profits
max_decrease = min(monthly_change)
print(f"Greatest Decrease in Profits: {max_decrease}", file=f)

# comic_df.to_csv("Output/comic_updated.csv", index=False, header=True)
financial_analysis = {"Total_Months:": total_months,
                      "Total:": net_profit,
                      "Average Change:": avg_change}

f.close()
