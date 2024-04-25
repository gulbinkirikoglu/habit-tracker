from datetime import datetime 
from habit_tool import break_habit, gain_habit
import pandas as pd
from tabulate import tabulate


print("#####   #####   ##### WELCOME TO HABIT TRACKER #####   #####   #####")

break_habits = []
gain_habits = []

goal = int(input("Firstly enter your goal day?:"))

while True:
    print("If you want to make a habit, please enter '1'. \nIf you want to quit a habit, enter '2'. \nTo exit, enter '0'.")
    b_or_g = input("What do you want to do?: ")
    
    if b_or_g == '0':
        print("Exiting...")
        break
        
    if b_or_g.isdigit():
        b_or_g = int(b_or_g)
        if b_or_g == 1:
            habit = str(input("Enter the name of your habit:"))
            start_date = input("When is your first day? (dd.mm.yyyy):")
            cost_per_day = int(input("How much do you spend per a day?:"))
            minutes_wasted = int(input("How many minutes do you spend per a day?:"))

            result1 = break_habit(goal=goal, habit_name=habit, start_date=start_date, cost_per_day=cost_per_day, minutes_wasted=minutes_wasted)
            break_habits.append(result1)
        elif b_or_g == 2:
            habit = str(input("Enter the name of your habit:"))
            start_date = input("When is your first day? (dd.mm.yyyy):")

            result2 = gain_habit(goal=goal, habit_name=habit, start_date=start_date)
            gain_habits.append(result2)
        else:
            print("Please select 0, 1, or 2!")
    else:
        print("Invalid input! Please enter a number.")

df1 = pd.DataFrame(gain_habits)
df2 = pd.DataFrame(break_habits)

print(tabulate(df1, headers="keys", tablefmt="psql"))
print(tabulate(df2, headers="keys", tablefmt="psql"))
